# 🎓 College Information Assistant
### *Ask. Retrieve. Know Instantly.*

An AI-powered RAG (Retrieval-Augmented Generation) chatbot built with **LangChain**, **ChromaDB**, and **Streamlit** that helps students instantly find college-related information — no more digging through PDFs or notice boards.

---

## 🚀 Live Demo

> Ask questions like:
> - *"What is the minimum attendance required?"*
> - *"What are the library timings?"*
> - *"Who approves attendance shortage applications?"*

...and get precise answers in seconds.

---

## 📌 The Problem This Solves

Students waste valuable time hunting for information scattered across multiple documents — attendance policies, hostel rules, fee deadlines, exam schedules. This assistant puts all of it at their fingertips through a simple chat interface.

---

## ✨ Features

- 💬 **Conversational chat interface** built with Streamlit
- 📄 **Retrieves answers** from a local knowledge base of `.txt` documents
- 🧠 **Semantic search** using HuggingFace sentence transformers
- 🗃️ **ChromaDB** for fast, persistent vector storage
- 🚫 **Graceful fallback** — tells users when information isn't available
- ⚡ **Lightweight** — no expensive LLM API calls needed for retrieval

---

## 🗂️ Project Structure

```
college-info-assistant/
│
├── app.py                  # Main Streamlit application
├── requirements.txt        # Python dependencies
├── README.md               # You're reading it!
│
├── documents/              # 📚 Knowledge base
│   ├── admission.txt
│   ├── attendance.txt
│   ├── exam_rules.txt
│   ├── fees.txt
│   ├── hostel.txt
│   ├── library.txt
│   ├── placement.txt
│   └── transport.txt
│
└── vector_store/           # 🗄️ ChromaDB persistent storage (auto-generated)
```

---

## 🧱 Tech Stack

| Layer | Technology |
|---|---|
| **UI** | Streamlit |
| **Orchestration** | LangChain |
| **Embeddings** | HuggingFace `sentence-transformers/all-MiniLM-L6-v2` |
| **Vector DB** | ChromaDB |
| **Language** | Python 3.x |

---

## ⚙️ How It Works

```
User Question
     │
     ▼
Convert to Embedding (MiniLM-L6-v2)
     │
     ▼
Similarity Search in ChromaDB
     │
     ▼
Retrieve Most Relevant Chunk
     │
     ▼
Display Answer to User
```

1. All `.txt` files from `documents/` are loaded at startup
2. Text is split into **300-character chunks** with **50-character overlap** for context continuity
3. Each chunk is converted into a vector embedding and stored in ChromaDB
4. On each user query, the question is embedded and compared against stored vectors
5. The most semantically similar chunk is returned as the answer

---

## 📦 Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/college-info-assistant.git
cd college-info-assistant
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your documents

Place your `.txt` knowledge base files inside the `documents/` folder. Each file should cover a single topic for best retrieval quality.

### 5. Run the app

```bash
streamlit run app.py
```

The app will open at `http://localhost:8501` in your browser.

---

## 🧪 Sample Test Results

| Question | Retrieved Topic | Answer | Correct? |
|---|---|---|---|
| What is the minimum attendance required? | Attendance Policy | Minimum attendance required is 75% | ✅ |
| What are the library timings? | Library Policy | Library operates from 9 AM to 5 PM on weekdays | ✅ |
| Does the college provide free gym membership? | Not Found | *"I could not find this information in the provided documents."* | ✅ |
| Who approves attendance shortage applications? | Attendance Policy | Attendance shortage applications must be approved by the HoD | ✅ |

---

## 🧠 Embedding Model

**`sentence-transformers/all-MiniLM-L6-v2`**

- Lightweight and fast — ideal for local deployment
- Strong semantic understanding for Q&A tasks
- No API key required — runs entirely offline

---

## 📚 Knowledge Base Topics

The current knowledge base covers:

- 📋 Admission Policy
- 📅 Attendance Policy
- 📝 Exam Rules
- 💰 Fee Structure
- 🏠 Hostel Information
- 📖 Library Policy
- 💼 Placement Policy
- 🚌 Transport Policy

> **Adding new topics?** Just drop a new `.txt` file into the `documents/` folder and restart the app.

---

## ⚠️ Limitations

- Works only with `.txt` documents (no PDF support yet)
- Retrieves chunks as-is — does not synthesize or summarize answers
- Retrieval accuracy depends on chunk quality and document organization
- No chat memory between sessions

---

## 🔮 Future Improvements

- [ ] Integrate an LLM (OpenAI / LLaMA / Gemini) for generated, natural-language answers
- [ ] Add PDF document support
- [ ] Implement semantic reranking for better retrieval precision
- [ ] Add conversation memory for multi-turn Q&A
- [ ] Deploy to cloud (Streamlit Cloud / HuggingFace Spaces)
- [ ] Support multilingual queries

---

## 👩‍💻 Author

**Neethu O S**
B.Tech — Computer Science and Engineering

Interests: Data Analysis · Artificial Intelligence · Machine Learning · Web Development

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

> *Built as part of a GenAI learning project — demonstrating RAG architecture with local embeddings and vector search.*
