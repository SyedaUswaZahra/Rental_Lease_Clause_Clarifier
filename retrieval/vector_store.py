from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS


class ResumeVectorStore:
    def __init__(self, embeddings: OpenAIEmbeddings) -> None:
        self.embeddings = embeddings
        self.index = None

    def build_index(self, bullets: list[str]) -> None:
        self.index = FAISS.from_texts(bullets, self.embeddings)

    def retrieve(self, query: str, k: int = 3) -> list[str]:
        if self.index is None:
            raise ValueError("Index has not been built. Call build_index() first.")
        docs = self.index.similarity_search(query, k=k)
        return [doc.page_content for doc in docs]


class BulletRetriever:
    def __init__(self, vector_store: ResumeVectorStore) -> None:
        self.vector_store = vector_store

    def retrieve_for_requirements(self, requirements: list[str], k: int = 3) -> dict[str, list[str]]:
        results = {}
        for requirement in requirements:
            results[requirement] = self.vector_store.retrieve(requirement, k=k)
        return results
