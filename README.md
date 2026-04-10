# 💻 AI Codebase Chat

---

## 📌 Overview

**AI Codebase Chat** is an AI-powered developer tool that enables users to interact with entire codebases using natural language.

Instead of manually searching through files, developers can simply ask questions and get intelligent, context-aware answers powered by **Retrieval-Augmented Generation (RAG)** and **Large Language Models (LLMs)**.

---

## ✨ Features

* 📂 Upload codebase (ZIP file)
* 🔍 Ask questions about code
* 🧠 Context-aware answers using RAG
* 📄 Supports multiple file types (.py, .js, .md, .txt)
* ⚡ Fast semantic search using FAISS
* 💬 Natural language interaction with code

---

## 🧠 Tech Stack

* **Python**
* **Streamlit** (UI)
* **LangChain**
* **OpenAI API (LLM)**
* **FAISS (Vector Database)**
* **tiktoken**

---

## 🏗️ Architecture

```id="arch1"
Codebase (ZIP)
   ↓
Code Loader (extract + read files)
   ↓
Text Chunking
   ↓
Embeddings (OpenAI)
   ↓
FAISS Vector Store
   ↓
User Query
   ↓
Similarity Search (Top K chunks)
   ↓
LLM (Context + Query)
   ↓
Final Answer
```

---

## 📂 Project Structure

```id="arch2"
ai-codebase-chat/
│
├── app.py
├── requirements.txt
├── README.md
│
├── utils/
│   ├── loader.py
│   ├── embeddings.py
│   ├── retriever.py
│   └── llm.py
│
└── data/
```

---

## ▶️ How to Run Locally

### 1️⃣ Clone Repository

```bash id="run1"
git clone https://github.com/your-username/ai-codebase-chat.git
cd ai-codebase-chat
```

---

### 2️⃣ Install Dependencies

```bash id="run2"
pip install -r requirements.txt
```

---

### 3️⃣ Set OpenAI API Key

#### 🔹 Mac/Linux:

```bash id="run3"
export OPENAI_API_KEY=your_api_key
```

#### 🔹 Windows:

```bash id="run4"
set OPENAI_API_KEY=your_api_key
```

---

### 4️⃣ Run Application

```bash id="run5"
streamlit run app.py
```

---

## 💡 Example Use Cases

* Understand unfamiliar codebases quickly
* Debug and analyze code
* Assist in code reviews
* Learn open-source projects faster
* Improve developer productivity

---

## 🚀 Future Improvements

* 🔗 GitHub repository URL support
* 💬 Chat-based UI with conversation memory
* 📁 File-level context display
* 🧠 Multi-agent code reasoning
* 🌐 Deployment (Streamlit Cloud / Render)
* 🔍 Syntax-aware code parsing

## AUTHOR : Joncy Keda | AI Developer
---
