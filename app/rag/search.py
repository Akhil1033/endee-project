from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

VECTOR_DB_PATH = "vectordb"


def get_vectorstore():
    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    vectorstore = Chroma(
        persist_directory=VECTOR_DB_PATH,
        embedding_function=embeddings
    )

    return vectorstore


def search(query, k=3):
    vectorstore = get_vectorstore()
    results = vectorstore.similarity_search(query, k=k)
    return results
