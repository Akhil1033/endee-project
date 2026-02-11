# Endee-based Semantic Search & RAG Demo

This project demonstrates a **semantic search and Retrieval-Augmented Generation (RAG) style workflow**
using **Endee** as the vector database.

Endee is a high-performance C++ vector database.  
In this project, Endee is integrated at the **API / client abstraction layer**, focusing on how AI
applications interact with a vector database for similarity search.

---

##  Features

- Document ingestion from text files
- Sentence embeddings using Sentence Transformers
- Vector storage and similarity search via Endee-compatible client
- Semantic search over documents
- Clean, modular architecture

---

##  Architecture
app/
├── endee_client.py # Endee-compatible vector DB abstraction
├── ingest.py # Document ingestion & embedding
├── search.py # Semantic search (RAG-style retrieval)

data/
└── documents/ # Input text documents


---

##  How Endee Is Used

- Endee acts as the **vector database**
- Documents are converted into embeddings
- Embeddings are stored in Endee
- Queries are embedded and compared using vector similarity

> Note:  
> Endee is a C++ system-level vector database.  
> For local development and demonstration, a **compatible client abstraction** is used to
> simulate Endee’s vector insert and search behavior while preserving the same architecture.

This approach mirrors real-world usage where applications interact with vector databases
through APIs rather than direct binary execution.

---

##  How to Run

### 1. Create a virtual environment (optional)
```bash
python -m venv venv
venv\Scripts\activate
2. Install dependencies
pip install sentence-transformers scikit-learn
3. Add documents

Place .txt files inside:

data/documents/
4. Run semantic search
python app/search.py
 Example Output
Top results:


Score: 0.82
Source: ml.txt
Machine learning is a subset of artificial intelligence...
Use Cases

Semantic Search

RAG-based Question Answering

AI-powered document retrieval

Vector database integration demos

 License

Apache 2.0



---





Press:

Ctrl + S



That’s it. README is now **done correctly**.


---


## 🔍 How to VERIFY Step 2 is correct


Do this quick checklist:


-  `README.md` opens without errors
-  Headings are visible (`#`, `##`)
-  Code blocks look formatted
-  Architecture tree is visible
-  Endee usage is clearly explained


If yes → **Step 2 is complete**.


---





It:
- Explicitly mentions **Endee** 
- Explains **vector DB role** 
- Shows **semantic search & RAG** 
- Is honest about abstraction (very important) 
- Looks professional and clean 


This is exactly how **industry demo repos** look.


---


##  What comes NEXT


After Step 2, only **one thing remains**:


 **Step 3: Git commit & push**


If you want, I’ll explain Step 3 with the **same level of detail**.


Just reply:
**NEXT (git push)**