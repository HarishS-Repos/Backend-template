from app.services.llm_client import LLMClient
from app.infra.vector_store import VectorStore

class RAGService:
    def __init__(self, tenant_id: str):
        self.tenant_id = tenant_id
        self.vector_store = VectorStore(tenant_id)
        self.llm = LLMClient()

    def run(self, query: str) -> str:
        context = self.vector_store.retrieve(query)
        return self.llm.generate(query, context)
