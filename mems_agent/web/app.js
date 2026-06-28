const state = {
  files: [],
  lastTrace: null,
  busy: false,
  pendingRunId: null,
  pendingConfirmation: null,
  sessionId: null,
};

const els = {
  messages: document.querySelector("#messages"),
  form: document.querySelector("#chatForm"),
  input: document.querySelector("#messageInput"),
  fileInput: document.querySelector("#fileInput"),
  attachmentList: document.querySelector("#attachmentList"),
  sendBtn: document.querySelector("#sendBtn"),
  resetBtn: document.querySelector("#resetBtn"),
  sessionId: document.querySelector("#sessionId"),
  healthText: document.querySelector("#healthText"),
  stepCount: document.querySelector("#stepCount"),
  planPanel: document.querySelector("#planPanel"),
  apiPanel: document.querySelector("#apiPanel"),
  rawPanel: document.querySelector("#rawPanel"),
  rawJson: document.querySelector("#rawJson"),
  confirmModal: document.querySelector("#confirmModal"),
  confirmForm: document.querySelector("#confirmForm"),
  confirmFields: document.querySelector("#confirmFields"),
  confirmTitle: document.querySelector("#confirmTitle"),
  confirmSubtitle: document.querySelector("#confirmSubtitle"),
  confirmCloseBtn: document.querySelector("#confirmCloseBtn"),
  confirmCancelBtn: document.querySelector("#confirmCancelBtn"),
};

function escapeHtml(value) {
  return String(value ?? "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
}

function pretty(value) {
  if (typeof value === "string") {
    try {
      return JSON.stringify(JSON.parse(value), null, 2);
    } catch {
      return value;
    }
  }
  return JSON.stringify(value ?? {}, null, 2);
}

function shortSize(bytes) {
  if (!bytes) return "0 B";
  const units = ["B", "KB", "MB", "GB"];
  let size = bytes;
  let index = 0;
  while (size >= 1024 && index < units.length - 1) {
    size /= 1024;
    index += 1;
  }
  return `${size.toFixed(index ? 1 : 0)} ${units[index]}`;
}

function addMessage(role, text) {
  const node = document.createElement("div");
  node.className = `message ${role}`;
  node.textContent = text;
  els.messages.appendChild(node);
  els.messages.scrollTop = els.messages.scrollHeight;
  return node;
}

function initSession() {
  const stored = window.localStorage.getItem("mems-agent-session-id");
  state.sessionId = stored || `web-${Date.now().toString(36)}-${Math.random().toString(36).slice(2, 8)}`;
  window.localStorage.setItem("mems-agent-session-id", state.sessionId);
  els.sessionId.value = state.sessionId;
}

function currentSessionId() {
  const value = els.sessionId.value.trim() || state.sessionId;
  state.sessionId = value;
  window.localStorage.setItem("mems-agent-session-id", value);
  return value;
}

function setBusy(value) {
  state.busy = value;
  els.sendBtn.disabled = value;
  els.input.disabled = value;
  els.fileInput.disabled = value;
  els.sendBtn.textContent = value ? "Working" : "Send";
}

function renderAttachments() {
  els.attachmentList.innerHTML = "";
  state.files.forEach((file, index) => {
    const chip = document.createElement("div");
    chip.className = "attachment-chip";
    chip.innerHTML = `
      <span>${escapeHtml(file.name)}</span>
      <span>${shortSize(file.size)}</span>
      <button type="button" title="Remove attachment" aria-label="Remove attachment">x</button>
    `;
    chip.querySelector("button").addEventListener("click", () => {
      state.files.splice(index, 1);
      renderAttachments();
    });
    els.attachmentList.appendChild(chip);
  });
}

function emptyTrace() {
  const template = document.querySelector("#emptyTraceTemplate");
  return template.content.cloneNode(true);
}

function renderPlan(payload) {
  els.planPanel.innerHTML = "";
  const subtasks = payload?.subtasks || [];
  if (!subtasks.length) {
    els.planPanel.appendChild(emptyTrace());
    return;
  }
  subtasks.forEach((task, index) => {
    const status = payload.subtask_status?.[task] || "pending";
    const card = document.createElement("article");
    card.className = "step-card";
    card.innerHTML = `
      <div class="step-head">
        <span class="step-index">${index + 1}</span>
        <div class="step-title">${escapeHtml(task)}</div>
        <span class="badge">${escapeHtml(status)}</span>
      </div>
    `;
    els.planPanel.appendChild(card);
  });
}

function methodFromEvent(event) {
  return event.method || event.http_method || event.parsed_result?.method || "API";
}

function renderApi(payload) {
  els.apiPanel.innerHTML = "";
  const events = payload?.trace_events || [];
  const apiEvents = events.filter((event) => event.type === "tool_result");
  els.stepCount.textContent = `${apiEvents.length} API call${apiEvents.length === 1 ? "" : "s"}`;
  if (!apiEvents.length) {
    els.apiPanel.appendChild(emptyTrace());
    return;
  }
  apiEvents.forEach((event, index) => {
    const card = document.createElement("article");
    card.className = "api-card";
    const ok = event.success !== false;
    const method = methodFromEvent(event);
    card.innerHTML = `
      <div class="api-head">
        <div class="api-name"><span class="method-badge">${escapeHtml(method)}</span>${index + 1}. ${escapeHtml(event.tool_name || "unknown")}</div>
        <div>
          <span class="badge ${ok ? "ok" : "bad"}">${ok ? "success" : "failed"}</span>
          <span class="badge">${Number(event.duration_ms || 0)} ms</span>
          <button type="button" class="details-toggle">Details</button>
        </div>
      </div>
      <div class="api-body collapsed">
        <div>
          <div class="kv-title">Input arguments</div>
          <pre>${escapeHtml(pretty(event.args || {}))}</pre>
        </div>
        <div>
          <div class="kv-title">Output result</div>
          <pre>${escapeHtml(pretty(event.parsed_result || event.result || {}))}</pre>
        </div>
      </div>
    `;
    const body = card.querySelector(".api-body");
    card.querySelector(".details-toggle").addEventListener("click", () => {
      body.classList.toggle("collapsed");
    });
    els.apiPanel.appendChild(card);
  });
}

function renderRaw(payload) {
  els.rawJson.textContent = JSON.stringify(payload || {}, null, 2);
}

function renderTrace(payload) {
  state.lastTrace = payload;
  renderPlan(payload);
  renderApi(payload);
  renderRaw(payload);
}

function openConfirmation(payload) {
  state.pendingRunId = payload.run_id;
  state.pendingConfirmation = payload.pending_confirmation;
  const pending = state.pendingConfirmation || {};
  const stepText = pending.step_total
    ? `Planning step ${pending.step_index || 1}/${pending.step_total}`
    : "Planning step";
  els.confirmTitle.textContent = `${stepText}: ${pending.step_task || pending.tool_name || "API call"}`;
  els.confirmSubtitle.textContent = `${pending.method || "API"} ${pending.path || pending.tool_name || ""}`;
  els.confirmFields.innerHTML = "";

  (pending.fields || []).forEach((field) => {
    const row = document.createElement("div");
    row.className = "field-row";
    row.dataset.name = field.name;
    row.dataset.type = field.type || "string";
    row.dataset.multiple = field.multiple ? "1" : "0";
    const value = field.value == null ? "" : field.value;
    const source = field.source || "agent";
    let control = "";
    if (field.type === "file") {
      const selectedText = Array.isArray(value) ? value.join("\n") : value;
      control = `
        <input class="field-file" type="file" ${field.multiple ? "multiple" : ""} />
        <textarea class="field-value" rows="2" placeholder="File path">${escapeHtml(selectedText)}</textarea>
      `;
    } else if (typeof value === "boolean" || field.type === "boolean") {
      control = `
        <select class="field-value">
          <option value="true" ${value === true ? "selected" : ""}>true</option>
          <option value="false" ${value === false ? "selected" : ""}>false</option>
        </select>
      `;
    } else if (typeof value === "object" && value !== null) {
      control = `<textarea class="field-value" rows="5">${escapeHtml(JSON.stringify(value, null, 2))}</textarea>`;
    } else {
      control = `<input class="field-value" type="${field.type === "integer" || field.type === "number" ? "number" : "text"}" value="${escapeHtml(value)}" />`;
    }
    row.innerHTML = `
      <div class="field-label">
        <span>${escapeHtml(field.label || field.name)}${field.required ? " *" : ""}</span>
        <span class="badge ${field.needs_confirmation ? "bad" : "ok"}">${escapeHtml(field.needs_confirmation ? "needs confirmation" : source)}</span>
      </div>
      ${control}
      <div class="field-help">${escapeHtml(field.description || "")}</div>
    `;
    els.confirmFields.appendChild(row);
  });

  els.confirmModal.classList.remove("hidden");
}

function closeConfirmation() {
  els.confirmModal.classList.add("hidden");
}

function collectConfirmationArgs(formData) {
  const args = {};
  const fileInputs = [];
  els.confirmFields.querySelectorAll(".field-row").forEach((row) => {
    const name = row.dataset.name;
    const type = row.dataset.type;
    const multiple = row.dataset.multiple === "1";
    const valueControl = row.querySelector(".field-value");
    const fileControl = row.querySelector(".field-file");
    if (fileControl && fileControl.files.length) {
      Array.from(fileControl.files).forEach((file) => {
        formData.append("files", file);
        fileInputs.push(name);
      });
      return;
    }
    let value = valueControl ? valueControl.value : "";
    if (type === "file" && multiple) {
      args[name] = value.split(/\r?\n|,/).map((item) => item.trim()).filter(Boolean);
    } else if (type === "file") {
      args[name] = value.trim();
    } else if (type === "boolean") {
      args[name] = value === "true";
    } else if (type === "integer") {
      args[name] = value === "" ? null : Number.parseInt(value, 10);
    } else if (type === "number") {
      args[name] = value === "" ? null : Number.parseFloat(value);
    } else if (type === "object" || type.startsWith("array") || value.trim().startsWith("{") || value.trim().startsWith("[")) {
      try {
        args[name] = value.trim() ? JSON.parse(value) : null;
      } catch {
        args[name] = value;
      }
    } else {
      args[name] = value;
    }
  });
  return args;
}

function handlePayload(payload, placeholder) {
  renderTrace(payload);
  if (payload.status === "awaiting_confirmation") {
    placeholder.textContent = "An API call needs your confirmation before execution.";
    openConfirmation(payload);
    return;
  }
  placeholder.textContent = payload.answer || "Completed without a text response.";
}

async function sendMessage(event) {
  event.preventDefault();
  if (state.busy) return;

  const message = els.input.value.trim();
  if (!message && !state.files.length) return;

  const filesForRequest = [...state.files];
  addMessage("user", message || "Uploaded attachments");
  const placeholder = addMessage("agent", "Planning the task...");
  setBusy(true);

  try {
    const form = new FormData();
    form.append("message", message);
    form.append("session_id", currentSessionId());
    filesForRequest.forEach((file) => form.append("files", file));

    const response = await fetch("/api/chat", { method: "POST", body: form });
    const payload = await response.json();
    if (!response.ok || payload.ok === false) throw new Error(payload.error || "Request failed");

    handlePayload(payload, placeholder);
    els.input.value = "";
    state.files = [];
    renderAttachments();
  } catch (error) {
    placeholder.className = "message error";
    placeholder.textContent = `Failed: ${error.message}`;
  } finally {
    setBusy(false);
    autoSizeInput();
  }
}

async function confirmApi(event) {
  event.preventDefault();
  if (!state.pendingRunId || state.busy) return;
  const placeholder = addMessage("agent", "Executing confirmed API call...");
  closeConfirmation();
  setBusy(true);
  try {
    const form = new FormData();
    form.append("run_id", state.pendingRunId);
    const args = collectConfirmationArgs(form);
    form.append("args", JSON.stringify(args));
    const response = await fetch("/api/confirm", { method: "POST", body: form });
    const payload = await response.json();
    if (!response.ok || payload.ok === false) throw new Error(payload.error || "Confirmation failed");
    handlePayload(payload, placeholder);
  } catch (error) {
    placeholder.className = "message error";
    placeholder.textContent = `Failed: ${error.message}`;
  } finally {
    setBusy(false);
  }
}

function autoSizeInput() {
  els.input.style.height = "0px";
  els.input.style.height = `${Math.min(els.input.scrollHeight, 160)}px`;
}

async function checkHealth() {
  try {
    const response = await fetch("/api/health");
    const payload = await response.json();
    els.healthText.textContent = payload.ok ? "Backend online" : "Backend unavailable";
  } catch {
    els.healthText.textContent = "Backend offline";
    document.querySelector(".status-item .dot").className = "dot error";
  }
}

async function resetSession() {
  if (state.busy) return;
  await fetch("/api/reset", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ session_id: currentSessionId() }),
  });
  els.messages.innerHTML = "";
  renderTrace(null);
  addMessage("agent", "Session reset.");
}

els.form.addEventListener("submit", sendMessage);
els.confirmForm.addEventListener("submit", confirmApi);
els.confirmCloseBtn.addEventListener("click", closeConfirmation);
els.confirmCancelBtn.addEventListener("click", closeConfirmation);
els.fileInput.addEventListener("change", () => {
  state.files.push(...Array.from(els.fileInput.files || []));
  els.fileInput.value = "";
  renderAttachments();
});
els.input.addEventListener("input", autoSizeInput);
els.input.addEventListener("keydown", (event) => {
  if (event.key === "Enter" && !event.shiftKey) {
    event.preventDefault();
    els.form.requestSubmit();
  }
});
els.resetBtn.addEventListener("click", resetSession);

document.querySelectorAll(".tab").forEach((tab) => {
  tab.addEventListener("click", () => {
    document.querySelectorAll(".tab").forEach((item) => item.classList.remove("active"));
    tab.classList.add("active");
    const active = tab.dataset.tab;
    els.planPanel.classList.toggle("hidden", active !== "plan");
    els.apiPanel.classList.toggle("hidden", active !== "api");
    els.rawPanel.classList.toggle("hidden", active !== "raw");
  });
});

initSession();
renderTrace(null);
addMessage("agent", "Ready. I will ask for confirmation before executing generated or default API parameters.");
checkHealth();
