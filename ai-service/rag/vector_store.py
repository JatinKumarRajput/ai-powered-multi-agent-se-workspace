from pathlib import Path

from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings


CHROMA_DIR = Path(__file__).resolve().parent.parent / "chroma_db"

COLLECTION_NAME = "project_context"


class ProjectVectorStore:
    """
    Persistent vector store for shared software project context.
    """

    def __init__(self):
        self.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

        self.vector_store = Chroma(
            collection_name=COLLECTION_NAME,
            embedding_function=self.embeddings,
            persist_directory=str(CHROMA_DIR),
        )

    def add_context(self, text: str, metadata: dict | None = None):
        """
        Add project context to the vector store.
        """

        self.vector_store.add_texts(
            texts=[text],
            metadatas=[metadata or {}],
        )

    def search(self, query: str, k: int = 3):
        """
        Retrieve the most relevant project context.
        """

        return self.vector_store.similarity_search(
            query,
            k=k,
        )