# Endee RAG Document QA System

A Retrieval-Augmented Generation (RAG) based document question-answering system built using:

- Streamlit (Web UI)
- LangChain
- Chroma Vector Database
- Hugging Face Embeddings
- Hugging Face LLM API

---

## 🚀 Features

- Upload PDF or TXT documents
- Automatic document chunking
- Vector embedding & storage
- Semantic similarity search
- Context-based answer generation
- Clean Streamlit web interface

---

## 🧠 How It Works

1. Documents are uploaded
2. Text is split into chunks
3. Embeddings are generated
4. Stored in Chroma vector database
5. Relevant chunks retrieved based on question
6. LLM generates final answer using retrieved context

---

## 🛠 Tech Stack

- Python
- Streamlit
- LangChain
- ChromaDB
- Hugging Face Transformers
- SentenceTransformers

---

## ▶️ Run Locally

```bash
pip install -r requirements.txt
streamlit run app_ui.py
