import os
from sentence_transformers import SentenceTransformer
from endee_client import EndeeClient

# -----------------------------
# Configuration
# -----------------------------
MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
DOCUMENTS_DIR = "data/documents"
CHUNK_SIZE = 300
CHUNK_OVERLAP = 50


# -----------------------------
# Chunking logic
# -----------------------------
def chunk_text(text, chunk_size=300, overlap=50):
    chunks = []
    start = 0
    length = len(text)

    while start < length:
        end = start + chunk_size
        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        start += chunk_size - overlap

    return chunks


# -----------------------------
# Ingestion pipeline
# -----------------------------
def ingest_documents():
    print("Loading embedding model...")
    model = SentenceTransformer(MODEL_NAME)

    print("Initializing Endee client...")
    endee = EndeeClient()

    files = [
        f for f in os.listdir(DOCUMENTS_DIR)
        if f.endswith(".txt")
    ]

    print(f"Found {len(files)} documents")

    total_chunks = 0

    for filename in files:
        path = os.path.join(DOCUMENTS_DIR, filename)

        with open(path, "r", encoding="utf-8") as f:
            text = f.read().strip()

        if not text:
            print(f"Skipping empty file: {filename}")
            continue

        chunks = chunk_text(text)
        print(f"Ingesting {filename} → {len(chunks)} chunks")

        for chunk in chunks:
            embedding = model.encode(chunk)

            # ✅ Correct Endee API usage
            endee.add(
                embedding=embedding,
                content=chunk,
                source=filename
            )

            total_chunks += 1

    print(f"\nIngestion completed: {total_chunks} chunks stored.")


# -----------------------------
# Entry point
# -----------------------------
if __name__ == "__main__":
    ingest_documents()