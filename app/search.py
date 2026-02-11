import os
import json
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

INDEX_DIR = "data/index"
EMBED_FILE = os.path.join(INDEX_DIR, "embeddings.npy")
META_FILE = os.path.join(INDEX_DIR, "metadata.json")


class EndeeClient:
    """
    Disk-backed vector store (production-safe).
    """

    def __init__(self):
        os.makedirs(INDEX_DIR, exist_ok=True)

        if os.path.exists(EMBED_FILE) and os.path.exists(META_FILE):
            self.embeddings = list(np.load(EMBED_FILE))
            with open(META_FILE, "r", encoding="utf-8") as f:
                self.metadatas = json.load(f)
        else:
            self.embeddings = []
            self.metadatas = []

    def _persist(self):
        np.save(EMBED_FILE, np.array(self.embeddings))
        with open(META_FILE, "w", encoding="utf-8") as f:
            json.dump(self.metadatas, f, indent=2)

    def add(self, embedding, content, source):
        self.embeddings.append(np.array(embedding))
        self.metadatas.append({
            "content": content,
            "source": source
        })
        self._persist()

    def search(self, query_embedding, top_k=2):
        if not self.embeddings:
            raise ValueError(
                "No vectors found in Endee. Run ingest.py first."
            )

        vectors = np.vstack(self.embeddings)
        query = np.array(query_embedding).reshape(1, -1)

        scores = cosine_similarity(query, vectors)[0]
        top_indices = scores.argsort()[::-1][:top_k]

        results = []
        for idx in top_indices:
            results.append({
                "content": self.metadatas[idx]["content"],
                "source": self.metadatas[idx]["source"],
                "score": float(scores[idx])
            })

        return results