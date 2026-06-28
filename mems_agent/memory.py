from __future__ import annotations

import hashlib
import json
import re
import time
from pathlib import Path
from typing import Any, Dict, List, Optional, TypedDict

from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import MarkdownTextSplitter

from config import get_llm_config

_DOCS_DIR = Path(__file__).parent
_DOCS_FILE = _DOCS_DIR / "mems_api_docs.md"
_INDEX_CACHE_DIR = _DOCS_DIR / ".faiss_cache"
_MEMORY_DIR = _DOCS_DIR / ".memory"


class ConversationHistory(TypedDict, total=False):
    user_input: str
    agent_response: str
    tool_results: List[Dict[str, Any]]
    timestamp: float
    summary: str
    entities: Dict[str, List[str]]


class AgentState(TypedDict):
    user_input: str
    agent_info: str
    tool_results: List[Dict[str, Any]]
    is_finished: bool
    final_answer: str
    conversation_history: List[ConversationHistory]
    max_steps: int
    relevant_tool_names: List[str]
    docs_content: str
    memory_context: str
    search_query: str
    attachments: List[Dict[str, Any]]
    trace_events: List[Dict[str, Any]]
    require_confirmation: bool
    pending_confirmation: Dict[str, Any]
    subtasks: List[str]
    subtask_status: Dict[str, str]
    completion_retries: int
    completion_feedback: List[str]


class MemoryManager:
    """Conversation memory plus retrieval support for MEMS agent sessions."""

    MAX_HISTORY_TURNS = 50
    RECENT_CONTEXT_TURNS = 4
    SUMMARY_AFTER_TURNS = 8
    MAX_FACTS = 80
    MAX_ENTITY_VALUES = 20

    ENTITY_PATTERNS = {
        "lcc_id": re.compile(r"\blcc[_\s-]?id\s*[:=]?\s*([A-Za-z0-9_.:-]+)", re.IGNORECASE),
        "version": re.compile(r"(?:version|版本)\s*[:=]?\s*([A-Za-z0-9_.:-]+)", re.IGNORECASE),
        "point_id": re.compile(r"(?:point[_\s-]?id|测点)\s*[:=]?\s*([A-Za-z0-9_.:-]+)", re.IGNORECASE),
        "device_id": re.compile(r"(?:device[_\s-]?id|dev[_\s-]?id|设备)\s*[:=]?\s*([A-Za-z0-9_.:-]+)", re.IGNORECASE),
        "flow_id": re.compile(r"(?:flow[_\s-]?id|流程|报表)\s*[:=]?\s*([A-Za-z0-9_.:-]+)", re.IGNORECASE),
        "aoe_id": re.compile(r"(?:aoe[_\s-]?id|aoe)\s*[:=]?\s*([A-Za-z0-9_.:-]+)", re.IGNORECASE),
    }

    def __init__(self, session_id: str = "default", persist_dir: Path | str = _MEMORY_DIR):
        self.session_id = self._sanitize_session_id(session_id)
        self.persist_dir = Path(persist_dir)
        self.memory_file = self.persist_dir / f"{self.session_id}.json"
        self.conversation_history: List[ConversationHistory] = []
        self.running_summary = ""
        self.structured_memory: Dict[str, Any] = {"entities": {}, "facts": [], "last_tool_calls": []}
        self.history_index: Optional[FAISS] = None
        self.history_index_dirty = True
        self.embeddings = self._init_embeddings()
        self.rag_system = self._init_rag_system()
        self.tool_index: Optional[FAISS] = None
        self._load_session()
        self._rebuild_history_index()

    def _sanitize_session_id(self, session_id: str) -> str:
        safe = re.sub(r"[^A-Za-z0-9_.-]+", "_", session_id or "default").strip("._")
        return safe or "default"

    def _init_embeddings(self) -> Optional[OpenAIEmbeddings]:
        try:
            llm_config = get_llm_config()
            return OpenAIEmbeddings(
                model="text-embedding-3-small",
                api_key=llm_config.get("api_key"),
                base_url=llm_config.get("base_url", "https://yunwu.ai/")
            )
        except Exception as e:
            print(f"Warning: embedding init failed: {e}")
            return None

    def _embedding_signature(self) -> str:
        model = getattr(self.embeddings, "model", "unknown")
        return str(model)

    def _load_or_build_index(self, cache_name: str, content_hash: str, build_fn) -> Optional[FAISS]:
        cache_path = _INDEX_CACHE_DIR / cache_name
        fingerprint = hashlib.md5(f"{self._embedding_signature()}:{content_hash}".encode("utf-8")).hexdigest()
        fingerprint_file = cache_path / "fingerprint.txt"

        if cache_path.exists() and fingerprint_file.exists():
            try:
                if fingerprint_file.read_text(encoding="utf-8").strip() == fingerprint:
                    return FAISS.load_local(
                        str(cache_path), self.embeddings, allow_dangerous_deserialization=True
                    )
            except Exception as e:
                print(f"Warning: failed to load index cache {cache_name}, rebuilding: {e}")

        db = build_fn()
        if db is None:
            return None
        try:
            cache_path.mkdir(parents=True, exist_ok=True)
            db.save_local(str(cache_path))
            fingerprint_file.write_text(fingerprint, encoding="utf-8")
        except Exception as e:
            print(f"Warning: failed to save index cache {cache_name}: {e}")
        return db

    def _init_rag_system(self) -> Optional[FAISS]:
        if not self.embeddings:
            return None
        try:
            docs_content = _DOCS_FILE.read_text(encoding="utf-8")
            text_splitter = MarkdownTextSplitter(chunk_size=1000, chunk_overlap=200)
            docs = text_splitter.split_text(docs_content)
            documents = [Document(page_content=doc, metadata={"source": "mems_api_docs.md"}) for doc in docs]
            content_hash = hashlib.md5(docs_content.encode("utf-8")).hexdigest()
            return self._load_or_build_index(
                "docs_index",
                content_hash,
                lambda: FAISS.from_documents(documents, self.embeddings),
            )
        except FileNotFoundError:
            print("Warning: mems_api_docs.md not found")
            return None

    def _load_session(self) -> None:
        if not self.memory_file.exists():
            return
        try:
            data = json.loads(self.memory_file.read_text(encoding="utf-8"))
            self.conversation_history = data.get("conversation_history", [])[-self.MAX_HISTORY_TURNS:]
            self.running_summary = data.get("running_summary", "")
            self.structured_memory = data.get("structured_memory", self.structured_memory)
            self.history_index_dirty = True
        except Exception as e:
            print(f"Warning: failed to load memory session {self.session_id}: {e}")

    def _save_session(self) -> None:
        try:
            self.persist_dir.mkdir(parents=True, exist_ok=True)
            data = {
                "session_id": self.session_id,
                "running_summary": self.running_summary,
                "structured_memory": self.structured_memory,
                "conversation_history": self.conversation_history[-self.MAX_HISTORY_TURNS:],
                "updated_at": time.time(),
            }
            self.memory_file.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        except Exception as e:
            print(f"Warning: failed to save memory session {self.session_id}: {e}")

    def build_tool_index(self, tools: List[Any]) -> None:
        if not self.embeddings:
            return
        try:
            documents = [
                Document(
                    page_content=f"{tool.name}: {tool.description}",
                    metadata={"name": tool.name},
                )
                for tool in tools
            ]
            content_hash = hashlib.md5(
                "\n".join(doc.page_content for doc in documents).encode("utf-8")
            ).hexdigest()
            self.tool_index = self._load_or_build_index(
                "tools_index",
                content_hash,
                lambda: FAISS.from_documents(documents, self.embeddings),
            )
        except Exception as e:
            print(f"Warning: failed to build tool index: {e}")
            self.tool_index = None

    def _turn_to_document(self, turn: ConversationHistory, index: int) -> Document:
        tool_lines = []
        for result in turn.get("tool_results", [])[-8:]:
            result_text = self._compact_text(str(result.get("result", "")), 600)
            tool_lines.append(
                json.dumps(
                    {
                        "tool_name": result.get("tool_name"),
                        "args": result.get("args", {}),
                        "result": result_text,
                    },
                    ensure_ascii=False,
                )
            )
        content = "\n".join(
            [
                f"User: {turn.get('user_input', '')}",
                f"Assistant: {turn.get('agent_response', '')}",
                "Tools: " + " | ".join(tool_lines) if tool_lines else "Tools: []",
                f"Summary: {turn.get('summary', '')}",
            ]
        )
        return Document(page_content=content, metadata={"turn_index": index, "timestamp": turn.get("timestamp", 0)})

    def _rebuild_history_index(self) -> None:
        self.history_index = None
        if not self.embeddings or not self.conversation_history:
            self.history_index_dirty = False
            return
        try:
            documents = [
                self._turn_to_document(turn, index)
                for index, turn in enumerate(self.conversation_history)
            ]
            self.history_index = FAISS.from_documents(documents, self.embeddings)
            self.history_index_dirty = False
        except Exception as e:
            print(f"Warning: failed to build history index: {e}")
            self.history_index = None
            self.history_index_dirty = False

    def _ensure_history_index(self) -> None:
        if self.history_index_dirty:
            self._rebuild_history_index()

    def search_tools(self, query: str, k: int = 12) -> List[str]:
        if not self.tool_index:
            return []
        results = self.tool_index.similarity_search(query, k=k)
        return [doc.metadata["name"] for doc in results]

    def search_docs(self, query: str, k: int = 3) -> List[str]:
        if not self.rag_system:
            return []
        results = self.rag_system.similarity_search(query, k=k)
        return [doc.page_content for doc in results]

    def search_history(self, query: str, k: int = 4) -> List[ConversationHistory]:
        self._ensure_history_index()
        if not self.history_index:
            return []
        try:
            docs = self.history_index.similarity_search(query, k=k)
            turns = []
            seen = set()
            for doc in docs:
                idx = doc.metadata.get("turn_index")
                if isinstance(idx, int) and 0 <= idx < len(self.conversation_history) and idx not in seen:
                    seen.add(idx)
                    turns.append(self.conversation_history[idx])
            return turns
        except Exception as e:
            print(f"Warning: failed to search history: {e}")
            return []

    def _compact_text(self, text: str, max_chars: int = 1200) -> str:
        text = re.sub(r"\s+", " ", text or "").strip()
        if len(text) <= max_chars:
            return text
        return text[:max_chars] + "...(truncated)"

    def _summarize_turn(self, user_input: str, agent_response: str, tool_results: List[Dict[str, Any]]) -> str:
        tool_names = []
        success_states = []
        for result in tool_results or []:
            name = result.get("tool_name")
            if name:
                tool_names.append(name)
            result_text = str(result.get("result", ""))
            success = "unknown"
            try:
                parsed = json.loads(result_text)
                if "success" in parsed:
                    success = "success" if parsed.get("success") else "failed"
                elif "message" in parsed:
                    success = self._compact_text(str(parsed.get("message")), 120)
            except Exception:
                pass
            success_states.append(success)
        tools_part = ", ".join(dict.fromkeys(tool_names)) if tool_names else "no tools"
        status_part = ", ".join(success_states[:5]) if success_states else "no tool status"
        return self._compact_text(
            f"User asked: {user_input}. Assistant answered: {agent_response}. Tools: {tools_part}. Status: {status_part}.",
            1500,
        )

    def _extract_entities(self, text: str) -> Dict[str, List[str]]:
        entities: Dict[str, List[str]] = {}
        for name, pattern in self.ENTITY_PATTERNS.items():
            values = []
            for match in pattern.findall(text or ""):
                value = str(match).strip(" ,;，。)）")
                if value and value not in values:
                    values.append(value)
            if values:
                entities[name] = values[: self.MAX_ENTITY_VALUES]
        return entities

    def _merge_entities(self, entities: Dict[str, List[str]]) -> None:
        memory_entities = self.structured_memory.setdefault("entities", {})
        for key, values in entities.items():
            current = list(memory_entities.get(key, []))
            for value in values:
                if value not in current:
                    current.append(value)
            memory_entities[key] = current[-self.MAX_ENTITY_VALUES:]

    def _remember_fact(self, fact: str) -> None:
        if not fact:
            return
        facts = self.structured_memory.setdefault("facts", [])
        if fact not in facts:
            facts.append(fact)
        self.structured_memory["facts"] = facts[-self.MAX_FACTS:]

    def _update_structured_memory(self, turn: ConversationHistory) -> None:
        text_parts = [turn.get("user_input", ""), turn.get("agent_response", "")]
        for result in turn.get("tool_results", [])[-8:]:
            text_parts.append(str(result.get("args", {})))
            text_parts.append(str(result.get("result", ""))[:1200])
        entities = self._extract_entities("\n".join(text_parts))
        turn["entities"] = entities
        self._merge_entities(entities)
        self._remember_fact(turn.get("summary", ""))
        self.structured_memory["last_tool_calls"] = [
            {
                "tool_name": result.get("tool_name"),
                "args": result.get("args", {}),
                "timestamp": result.get("timestamp", turn.get("timestamp")),
            }
            for result in turn.get("tool_results", [])[-10:]
        ]

    def _refresh_running_summary(self) -> None:
        if len(self.conversation_history) <= self.SUMMARY_AFTER_TURNS:
            return
        old_turns = self.conversation_history[: -self.RECENT_CONTEXT_TURNS]
        summaries = [turn.get("summary", "") for turn in old_turns if turn.get("summary")]
        if not summaries:
            return
        merged = "\n".join(summaries[-30:])
        self.running_summary = self._compact_text(merged, 5000)

    def add_conversation(self, user_input: str, agent_response: str, tool_results: List[Dict[str, Any]], timestamp: float):
        turn: ConversationHistory = {
            "user_input": user_input,
            "agent_response": agent_response,
            "tool_results": tool_results or [],
            "timestamp": timestamp,
            "summary": self._summarize_turn(user_input, agent_response, tool_results or []),
        }
        self.conversation_history.append(turn)
        if len(self.conversation_history) > self.MAX_HISTORY_TURNS:
            self.conversation_history = self.conversation_history[-self.MAX_HISTORY_TURNS:]
        self._update_structured_memory(turn)
        self._refresh_running_summary()
        self.history_index_dirty = True
        self._save_session()

    def _format_turn(self, turn: ConversationHistory, index_label: str, include_results: bool = False) -> str:
        parts = [
            f"{index_label}:",
            f"User: {turn.get('user_input', '')}",
            f"Assistant: {turn.get('agent_response', '')}",
        ]
        if turn.get("summary"):
            parts.append(f"Summary: {turn['summary']}")
        if turn.get("entities"):
            parts.append("Entities: " + json.dumps(turn["entities"], ensure_ascii=False))
        if include_results and turn.get("tool_results"):
            compact_results = []
            for result in turn["tool_results"][-5:]:
                compact_results.append({
                    "tool_name": result.get("tool_name"),
                    "args": result.get("args", {}),
                    "result": self._compact_text(str(result.get("result", "")), 800),
                })
            parts.append("Tool results: " + json.dumps(compact_results, ensure_ascii=False))
        return "\n".join(parts)

    def build_context(self, query: str, k_history: int = 4) -> str:
        sections = []
        if self.running_summary:
            sections.append("Long-term conversation summary:\n" + self.running_summary)

        entities = self.structured_memory.get("entities") or {}
        if entities:
            sections.append("Known entities:\n" + json.dumps(entities, ensure_ascii=False))

        facts = self.structured_memory.get("facts") or []
        if facts:
            sections.append("Relevant accumulated facts:\n" + "\n".join(f"- {fact}" for fact in facts[-12:]))

        recent = self.conversation_history[-self.RECENT_CONTEXT_TURNS:]
        if recent:
            sections.append(
                "Recent turns:\n"
                + "\n\n".join(self._format_turn(turn, f"Recent {i + 1}", include_results=True) for i, turn in enumerate(recent))
            )

        recalled = self.search_history(query, k=k_history)
        recent_ids = {id(turn) for turn in recent}
        recalled = [turn for turn in recalled if id(turn) not in recent_ids]
        if recalled:
            sections.append(
                "Semantically recalled older turns:\n"
                + "\n\n".join(self._format_turn(turn, f"Recall {i + 1}", include_results=True) for i, turn in enumerate(recalled))
            )

        if not sections:
            return ""
        return "\nMemory context, for reference only. Current user request has priority.\n" + "\n\n".join(sections)

    def build_search_query(self, user_input: str) -> str:
        parts = [user_input]
        if self.conversation_history:
            last = self.conversation_history[-1]
            parts.append(last.get("user_input", ""))
            parts.append(last.get("summary", ""))
        entities = self.structured_memory.get("entities") or {}
        if entities:
            parts.append(json.dumps(entities, ensure_ascii=False))
        return "\n".join(part for part in parts if part)

    def get_conversation_history_copy(self) -> List[ConversationHistory]:
        return [dict(item) for item in self.conversation_history]

    def reset_conversation(self):
        self.conversation_history = []
        self.running_summary = ""
        self.structured_memory = {"entities": {}, "facts": [], "last_tool_calls": []}
        self.history_index = None
        self.history_index_dirty = False
        try:
            if self.memory_file.exists():
                self.memory_file.unlink()
        except Exception as e:
            print(f"Warning: failed to delete memory session {self.session_id}: {e}")
