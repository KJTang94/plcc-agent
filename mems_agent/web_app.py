from __future__ import annotations

import json
import mimetypes
import os
import re
import shutil
import sys
import threading
import time
import uuid
from email import policy
from email.parser import BytesParser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse

if str(BASE_DIR := Path(__file__).parent) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from mems_agent.mems_agent import MemsAgent

WEB_DIR = BASE_DIR / "web"
UPLOAD_DIR = BASE_DIR / "uploads"

_agents: dict[str, MemsAgent] = {}
_pending_runs: dict[str, dict] = {}
_agents_lock = threading.Lock()


def _safe_session_id(value: str | None) -> str:
    raw = value or f"web-{uuid.uuid4().hex[:12]}"
    safe = re.sub(r"[^A-Za-z0-9_.-]+", "_", raw).strip("._")
    return safe or "default"


def _get_agent(session_id: str) -> MemsAgent:
    session_id = _safe_session_id(session_id)
    with _agents_lock:
        agent = _agents.get(session_id)
        if agent is None:
            agent = MemsAgent(session_id=session_id)
            _agents[session_id] = agent
        return agent


def _json_response(handler: BaseHTTPRequestHandler, status: int, payload: dict) -> None:
    body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    handler.send_response(status)
    handler.send_header("Content-Type", "application/json; charset=utf-8")
    handler.send_header("Content-Length", str(len(body)))
    handler.end_headers()
    handler.wfile.write(body)


def _parse_multipart(content_type: str, body: bytes) -> tuple[dict[str, str], list[dict]]:
    message = BytesParser(policy=policy.default).parsebytes(
        b"Content-Type: " + content_type.encode("utf-8") + b"\r\nMIME-Version: 1.0\r\n\r\n" + body
    )
    fields: dict[str, str] = {}
    files: list[dict] = []
    for part in message.iter_parts():
        disposition = part.get("Content-Disposition", "")
        if "form-data" not in disposition:
            continue
        name = part.get_param("name", header="content-disposition")
        filename = part.get_filename()
        payload = part.get_payload(decode=True) or b""
        if filename:
            files.append({"field": name, "filename": filename, "content": payload})
        elif name:
            fields[name] = payload.decode(part.get_content_charset() or "utf-8", errors="replace")
    return fields, files


def _save_upload(file_item: dict, session_id: str) -> dict:
    filename = Path(file_item.get("filename") or "attachment").name
    session_dir = UPLOAD_DIR / _safe_session_id(session_id) / time.strftime("%Y%m%d-%H%M%S")
    session_dir.mkdir(parents=True, exist_ok=True)
    unique_name = f"{uuid.uuid4().hex[:8]}-{filename}"
    target = session_dir / unique_name
    with target.open("wb") as output:
        output.write(file_item.get("content", b""))
    return {
        "name": filename,
        "stored_name": unique_name,
        "path": str(target.resolve()),
        "size": target.stat().st_size,
    }


class MemsWebHandler(BaseHTTPRequestHandler):
    server_version = "MemsAgentWeb/1.0"

    def log_message(self, format: str, *args) -> None:
        print("[web] " + format % args)

    def do_GET(self) -> None:
        parsed = urlparse(self.path)
        if parsed.path == "/api/health":
            _json_response(self, 200, {"ok": True})
            return

        path = parsed.path
        if path == "/":
            path = "/index.html"
        file_path = (WEB_DIR / path.lstrip("/")).resolve()
        if not str(file_path).startswith(str(WEB_DIR.resolve())) or not file_path.is_file():
            self.send_error(404)
            return

        content_type = mimetypes.guess_type(str(file_path))[0] or "application/octet-stream"
        body = file_path.read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_POST(self) -> None:
        parsed = urlparse(self.path)
        if parsed.path == "/api/chat":
            self._handle_chat()
            return
        if parsed.path == "/api/confirm":
            self._handle_confirm()
            return
        if parsed.path == "/api/reset":
            self._handle_reset()
            return
        self.send_error(404)

    def _handle_chat(self) -> None:
        try:
            content_type = self.headers.get("Content-Type", "")
            if not content_type.startswith("multipart/form-data"):
                _json_response(self, 400, {"error": "multipart/form-data required"})
                return

            length = int(self.headers.get("Content-Length", "0") or 0)
            fields, files = _parse_multipart(content_type, self.rfile.read(length))
            message = (fields.get("message") or "").strip()
            session_id = _safe_session_id(fields.get("session_id"))
            if not message and not files:
                _json_response(self, 400, {"error": "message or files required"})
                return

            attachments = [
                _save_upload(item, session_id)
                for item in files
                if item.get("filename")
            ]

            agent = _get_agent(session_id)
            payload = agent.run_until_confirmation(message, attachments=attachments)
            run_id = None
            if payload.get("status") == "awaiting_confirmation":
                run_id = uuid.uuid4().hex
                _pending_runs[run_id] = {
                    "session_id": session_id,
                    "state": payload.pop("_state"),
                    "effective_input": payload.pop("_effective_input"),
                    "created_at": time.time(),
                }
            payload.pop("_state", None)
            payload.pop("_effective_input", None)
            _json_response(self, 200, {"ok": True, "run_id": run_id, **payload})
        except Exception as exc:
            _json_response(self, 500, {"ok": False, "error": str(exc)})

    def _handle_confirm(self) -> None:
        try:
            content_type = self.headers.get("Content-Type", "")
            length = int(self.headers.get("Content-Length", "0") or 0)
            if content_type.startswith("multipart/form-data"):
                fields, files = _parse_multipart(content_type, self.rfile.read(length))
                args = json.loads(fields.get("args") or "{}")
                run_id = fields.get("run_id", "")
            else:
                raw = self.rfile.read(length) if length else b"{}"
                data = json.loads(raw.decode("utf-8") or "{}")
                args = data.get("args") or {}
                run_id = data.get("run_id", "")
                files = []

            pending = _pending_runs.pop(run_id, None)
            if not pending:
                _json_response(self, 404, {"ok": False, "error": "pending run not found"})
                return

            session_id = pending["session_id"]
            uploaded = [_save_upload(item, session_id) for item in files if item.get("filename")]
            file_paths = [item["path"] for item in uploaded]
            pending_state = pending["state"]
            pending_confirmation = pending_state.get("pending_confirmation") or {}
            for field in pending_confirmation.get("fields", []):
                name = field.get("name")
                if field.get("type") == "file" and uploaded:
                    args[name] = file_paths if field.get("multiple") else file_paths[0]

            agent = _get_agent(session_id)
            payload = agent.continue_after_confirmation(
                pending_state,
                confirmed_args=args,
                effective_input=pending.get("effective_input", ""),
            )
            next_run_id = None
            if payload.get("status") == "awaiting_confirmation":
                next_run_id = uuid.uuid4().hex
                _pending_runs[next_run_id] = {
                    "session_id": session_id,
                    "state": payload.pop("_state"),
                    "effective_input": payload.pop("_effective_input"),
                    "created_at": time.time(),
                }
            payload.pop("_state", None)
            payload.pop("_effective_input", None)
            _json_response(self, 200, {"ok": True, "run_id": next_run_id, **payload})
        except Exception as exc:
            _json_response(self, 500, {"ok": False, "error": str(exc)})

    def _handle_reset(self) -> None:
        try:
            length = int(self.headers.get("Content-Length", "0") or 0)
            raw = self.rfile.read(length) if length else b"{}"
            data = json.loads(raw.decode("utf-8") or "{}")
            session_id = _safe_session_id(data.get("session_id"))
            agent = _get_agent(session_id)
            agent.reset_conversation()
            _json_response(self, 200, {"ok": True})
        except Exception as exc:
            _json_response(self, 500, {"ok": False, "error": str(exc)})


def run(host: str = "127.0.0.1", port: int = 7860) -> None:
    server = ThreadingHTTPServer((host, port), MemsWebHandler)
    url = f"http://{host}:{port}"
    print(f"MEMS Agent web console running at {url}")
    server.serve_forever()


if __name__ == "__main__":
    host = os.environ.get("MEMS_AGENT_HOST", "127.0.0.1")
    port = int(os.environ.get("MEMS_AGENT_PORT", "7860"))
    run(host=host, port=port)
