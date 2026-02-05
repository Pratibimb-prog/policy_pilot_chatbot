from langchain_community.vectorstores import Chroma
from config.settings import COLLECTION_NAME
from embeddings.hf_embeddings import get_embeddings

def create_vectorstore(documents):
    embeddings = get_embeddings()
    return Chroma.from_documents(
        documents,
        embeddings,
        collection_name=COLLECTION_NAME
    )