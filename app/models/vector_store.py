from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from config import Config


class VectorStore:
    def __init__(self, path: str):

        self.embeddings = OpenAIEmbeddings(
            model="text-embedding-3-small",
            api_key=Config.OPENAI_API_KEY
        )

        self.vector_store = Chroma(
            persist_directory=path,
            embedding_function=self.embeddings,
            collection_name="knowledge_base"
        )

    def add_documents(self, documents):
        self.vector_store.add_documents(documents)
        self.vector_store.persist()

    def similarity_search(self, query, k=4):
        return self.vector_store.similarity_search(query, k=k)

    def as_retriever(self):
        return self.vector_store.as_retriever()