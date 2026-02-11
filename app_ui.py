import streamlit as st
import os

from app.rag.ingest import ingest_documents
from app.rag.search import search
from app.rag.generator import generate_answer

st.set_page_config(page_title="Endee RAG QA System", layout="wide")

st.title("📄 Endee RAG Document QA System")
st.write("Upload PDF or TXT documents, index them, and ask questions.")

# ==============================
# Upload Section
# ==============================

st.header("📤 Upload Documents")

uploaded_files = st.file_uploader(
    "Upload PDF or TXT files",
    type=["pdf", "txt"],
    accept_multiple_files=True
)

if uploaded_files:
    for file in uploaded_files:
        file_path = os.path.join("data", file.name)
        with open(file_path, "wb") as f:
            f.write(file.getbuffer())

    st.success("Files uploaded successfully!")

if st.button("🔄 Re-index Documents"):
    ingest_documents()
    st.success("Documents indexed successfully!")

# ==============================
# Question Section
# ==============================

st.header("❓ Ask a Question")

query = st.text_input("Enter your question")

if st.button("Get Answer"):
    if query:
        results = search(query)
        answer = generate_answer(query, results)

        st.subheader("Answer")
        st.write(answer)
    else:
        st.warning("Please enter a question.")