import streamlit as st
import os
from utils.loader import load_codebase
from utils.embeddings import create_vectorstore
from utils.retriever import get_relevant_chunks
from utils.llm import ask_llm

st.set_page_config(page_title="AI Codebase Chat", layout="wide")

st.title("💻 AI Codebase Chat")

uploaded_file = st.file_uploader("Upload Codebase (ZIP)", type=["zip"])

if uploaded_file:
    with open("data/code.zip", "wb") as f:
        f.write(uploaded_file.read())

    st.success("Uploaded successfully!")

    if st.button("Process Codebase"):
        with st.spinner("Processing..."):
            docs = load_codebase("data/code.zip")
            vectorstore = create_vectorstore(docs)
            st.session_state["vectorstore"] = vectorstore

        st.success("Codebase ready!")

query = st.text_input("Ask a question about the codebase")

if query and "vectorstore" in st.session_state:
    docs = get_relevant_chunks(st.session_state["vectorstore"], query)
    answer = ask_llm(query, docs)

    st.subheader("💡 Answer")
    st.write(answer)
