from typing import List, Dict, Any, Optional, TypedDict
from pathlib import Path
from langchain_text_splitters import MarkdownTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from config import get_llm_config
import json
import re

_DOCS_DIR = Path(__file__).parent
_DOCS_FILE = _DOCS_DIR / "mems_api_docs.md"
_LONG_TERM_MEMORY_FILE = _DOCS_DIR / "long_term_memory.json"


class ConversationHistory(TypedDict):
    user_input: str
    agent_response: str
    tool_results: List[Dict[str, Any]]
    timestamp: float


class LongTermMemory(TypedDict):
    preferences: List[str]
    tool_experience: List[str]
    conversation_notes: List[str]


class AgentState(TypedDict):
    user_input: str
    agent_info: str
    tool_results: List[Dict[str, Any]]
    is_finished: bool
    final_answer: str
    token: Optional[str]
    base_url: str
    conversation_history: List[ConversationHistory]
    max_steps: int


class MemoryManager:
    def __init__(self):
        self.conversation_history: List[ConversationHistory] = []
        self.long_term_memory: LongTermMemory = self._load_long_term_memory()
        self.rag_system = self._init_rag_system()

    def _init_rag_system(self) -> Optional[FAISS]:
        try:
            with open(_DOCS_FILE, 'r', encoding='utf-8') as f:
                docs_content = f.read()

            text_splitter = MarkdownTextSplitter(chunk_size=1000, chunk_overlap=200)
            docs = text_splitter.split_text(docs_content)

            documents = [Document(page_content=doc, metadata={"source": "mems_api_docs.md"}) for doc in docs]

            llm_config = get_llm_config()
            embeddings = OpenAIEmbeddings(
                model="text-embedding-3-small",
                api_key=llm_config.get("api_key"),
                base_url=llm_config.get("base_url", "https://yunwu.ai/")
            )

            db = FAISS.from_documents(documents, embeddings)
            return db

        except FileNotFoundError:
            print("警告：未找到mems_api_docs.md文件")
            return None

    def _load_long_term_memory(self) -> LongTermMemory:
        default_memory: LongTermMemory = {
            "preferences": [],
            "tool_experience": [],
            "conversation_notes": []
        }

        if not _LONG_TERM_MEMORY_FILE.exists():
            self._save_long_term_memory(default_memory)
            return default_memory

        try:
            with open(_LONG_TERM_MEMORY_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
            return {
                "preferences": data.get("preferences", []),
                "tool_experience": data.get("tool_experience", []),
                "conversation_notes": data.get("conversation_notes", [])
            }
        except Exception:
            return default_memory

    def _save_long_term_memory(self, memory: Optional[LongTermMemory] = None):
        data = memory or self.long_term_memory
        with open(_LONG_TERM_MEMORY_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def _append_unique_memory_item(self, key: str, item: str, max_items: int = 30):
        item = item.strip()
        if not item:
            return
        if item not in self.long_term_memory[key]:
            self.long_term_memory[key].append(item)
            self.long_term_memory[key] = self.long_term_memory[key][-max_items:]

    def _extract_preferences(self, user_input: str, agent_response: str):
        preference_patterns = [
            r"请用([\u4e00-\u9fa5A-Za-z]+)回答",
            r"希望用([\u4e00-\u9fa5A-Za-z]+)回答",
            r"以后.*?用([\u4e00-\u9fa5A-Za-z]+)",
            r"尽量([\u4e00-\u9fa5A-Za-z]+)"
        ]
        for pattern in preference_patterns:
            matches = re.findall(pattern, user_input)
            for match in matches:
                self._append_unique_memory_item("preferences", f"用户偏好：{match}")

        if "中文" in user_input:
            self._append_unique_memory_item("preferences", "用户偏好：使用中文回答")
        if "简洁" in user_input:
            self._append_unique_memory_item("preferences", "用户偏好：回答尽量简洁")
        if "详细" in user_input:
            self._append_unique_memory_item("preferences", "用户偏好：回答可以更详细")

    def _extract_tool_experience(self, tool_results: List[Dict[str, Any]]):
        for item in tool_results:
            tool_name = item.get("tool_name", "")
            result = item.get("result", "")
            if not tool_name or not result:
                continue

            if isinstance(result, str):
                if "登录配置缺失" in result:
                    self._append_unique_memory_item("tool_experience", f"工具经验：{tool_name} 依赖 config.json 中的 mems_api 登录配置")
                elif "重复调用工具" in result:
                    self._append_unique_memory_item("tool_experience", f"工具经验：{tool_name} 在相同参数下重复调用可能触发循环保护")
                elif '"success": true' in result.lower() or '"success": true' in result:
                    self._append_unique_memory_item("tool_experience", f"工具经验：{tool_name} 曾成功调用")

    def _extract_conversation_notes(self, user_input: str, agent_response: str):
        if user_input.strip():
            self._append_unique_memory_item("conversation_notes", f"用户近期关注：{user_input.strip()[:120]}")
        if agent_response.strip():
            self._append_unique_memory_item("conversation_notes", f"系统近期结论：{agent_response.strip()[:120]}")

    def update_long_term_memory(self, user_input: str, agent_response: str, tool_results: List[Dict[str, Any]]):
        self._extract_preferences(user_input, agent_response)
        self._extract_tool_experience(tool_results)
        self._extract_conversation_notes(user_input, agent_response)
        self._save_long_term_memory()

    def get_long_term_memory_text(self) -> str:
        sections = []
        if self.long_term_memory["preferences"]:
            sections.append("用户偏好：\n- " + "\n- ".join(self.long_term_memory["preferences"][-10:]))
        if self.long_term_memory["tool_experience"]:
            sections.append("工具调用经验：\n- " + "\n- ".join(self.long_term_memory["tool_experience"][-10:]))
        if self.long_term_memory["conversation_notes"]:
            sections.append("长期对话记录：\n- " + "\n- ".join(self.long_term_memory["conversation_notes"][-10:]))
        if not sections:
            return ""
        return "\n长期记忆：\n" + "\n\n".join(sections)

    def search_docs(self, query: str, k: int = 3) -> List[str]:
        if not self.rag_system:
            return []

        results = self.rag_system.similarity_search(query, k=k)
        return [doc.page_content for doc in results]

    def add_conversation(self, user_input: str, agent_response: str, tool_results: List[Dict[str, Any]], timestamp: float):
        self.conversation_history.append({
            "user_input": user_input,
            "agent_response": agent_response,
            "tool_results": tool_results,
            "timestamp": timestamp
        })
        self.update_long_term_memory(user_input, agent_response, tool_results)

    def get_conversation_history_copy(self) -> List[ConversationHistory]:
        return self.conversation_history.copy()

    def reset_conversation(self):
        self.conversation_history = []
