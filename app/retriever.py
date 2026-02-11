# app/retriever.py

from endee_client import EndeeClient
from ingest import load_documents
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")
endee = EndeeClient()

# One-time indexing
_docs = load_documents()
_embeddings = model.encode([d["text"] for d in _docs])
endee.insert(_embeddings, _docs)

def retrieve_documents(query_embedding, top_k=3):
    results = endee.search(query_embedding, top_k=top_k)
    return [r["metadata"] for r in results]