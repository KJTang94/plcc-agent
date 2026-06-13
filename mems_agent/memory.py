from typing import List, Dict, Any, Optional, TypedDict
from pathlib import Path
import hashlib
from langchain_text_splitters import MarkdownTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from config import get_llm_config

_DOCS_DIR = Path(__file__).parent
_DOCS_FILE = _DOCS_DIR / "mems_api_docs.md"
_INDEX_CACHE_DIR = _DOCS_DIR / ".faiss_cache"


class ConversationHistory(TypedDict):
    user_input: str
    agent_response: str
    tool_results: List[Dict[str, Any]]
    timestamp: float


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
    # 对话历史最多保留的轮数，避免长会话下内存无限增长
    MAX_HISTORY_TURNS = 20

    def __init__(self):
        self.conversation_history: List[ConversationHistory] = []
        self.embeddings = self._init_embeddings()
        self.rag_system = self._init_rag_system()
        self.tool_index: Optional[FAISS] = None

    def _init_embeddings(self) -> Optional[OpenAIEmbeddings]:
        try:
            llm_config = get_llm_config()
            return OpenAIEmbeddings(
                model="text-embedding-3-small",
                api_key=llm_config.get("api_key"),
                base_url=llm_config.get("base_url", "https://yunwu.ai/")
            )
        except Exception as e:
            print(f"警告：Embedding 初始化失败: {e}")
            return None

    def _embedding_signature(self) -> str:
        """用于缓存键的 embedding 标识，模型变化时使旧缓存失效。"""
        model = getattr(self.embeddings, "model", "unknown")
        return str(model)

    def _load_or_build_index(self, cache_name: str, content_hash: str, build_fn) -> Optional[FAISS]:
        """加载持久化的 FAISS 索引；内容或 embedding 变化时重建并落盘。
        build_fn 返回构建好的 FAISS 实例。"""
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
                print(f"警告：加载索引缓存 {cache_name} 失败，将重建: {e}")

        db = build_fn()
        if db is None:
            return None
        try:
            db.save_local(str(cache_path))
            fingerprint_file.write_text(fingerprint, encoding="utf-8")
        except Exception as e:
            print(f"警告：保存索引缓存 {cache_name} 失败: {e}")
        return db

    def _init_rag_system(self) -> Optional[FAISS]:
        if not self.embeddings:
            return None
        try:
            with open(_DOCS_FILE, 'r', encoding='utf-8') as f:
                docs_content = f.read()

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
            print("警告：未找到mems_api_docs.md文件")
            return None

    def build_tool_index(self, tools: List[Any]) -> None:
        """基于工具的名称与描述构建向量索引，用于按需检索相关工具。"""
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
            print(f"警告：工具索引构建失败: {e}")
            self.tool_index = None

    def search_tools(self, query: str, k: int = 12) -> List[str]:
        """检索与查询最相关的工具名称列表，索引不可用时返回空列表。"""
        if not self.tool_index:
            return []
        results = self.tool_index.similarity_search(query, k=k)
        return [doc.metadata["name"] for doc in results]

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
        # 超出上限时丢弃最早的轮次，避免内存无限增长
        if len(self.conversation_history) > self.MAX_HISTORY_TURNS:
            self.conversation_history = self.conversation_history[-self.MAX_HISTORY_TURNS:]

    def get_conversation_history_copy(self) -> List[ConversationHistory]:
        return self.conversation_history.copy()

    def reset_conversation(self):
        self.conversation_history = []
