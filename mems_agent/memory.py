from typing import List, Dict, Any, Optional, TypedDict
from pathlib import Path
from langchain_text_splitters import MarkdownTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from config import get_llm_config

_DOCS_DIR = Path(__file__).parent
_DOCS_FILE = _DOCS_DIR / "mems_api_docs.md"


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
    def __init__(self):
        self.conversation_history: List[ConversationHistory] = []
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

    def get_conversation_history_copy(self) -> List[ConversationHistory]:
        return self.conversation_history.copy()

    def reset_conversation(self):
        self.conversation_history = []
