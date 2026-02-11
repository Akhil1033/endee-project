import os
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

from app.utils.file_loader import load_document
from app.utils.hash_checker import get_file_hash, load_registry, save_registry
from app.rag.chunker import chunk_text


DATA_PATH = "data"
VECTOR_DB_PATH = "vectordb"


def ingest_documents():

    # Load local embedding model
    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    # Initialize persistent vector database
    vectorstore = Chroma(
        persist_directory=VECTOR_DB_PATH,
        embedding_function=embeddings
    )

    registry = load_registry()

    for root, _, files in os.walk(DATA_PATH):
        for file in files:
            path = os.path.join(root, file)

            # Compute file hash
            current_hash = get_file_hash(path)

            # Skip if unchanged
            if file in registry and registry[file] == current_hash:
                print(f"Skipping {file} (no changes)")
                continue

            print(f"Processing {file}")

            text = load_document(path)
            if not text:
                continue

            chunks = chunk_text(text)

            # Add chunks to vector database
            vectorstore.add_texts(
                texts=chunks,
                metadatas=[
                    {"source": file, "chunk_id": i}
                    for i in range(len(chunks))
                ]
            )

            # Update registry
            registry[file] = current_hash

    vectorstore.persist()
    save_registry(registry)

    print("Ingestion complete.")