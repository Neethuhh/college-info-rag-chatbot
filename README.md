# College Information Assistant (RAG Chatbot)

A Streamlit-based Retrieval-Augmented Generation (RAG) application that answers college-related questions by retrieving information from a local knowledge base of documents.

## Overview

This AI-powered chatbot uses embeddings and vector search to retrieve relevant information from text documents (admissions, attendance, hostel, library, fee structure, etc.) and answer user queries instantly — no manual searching required.

## Features

- Loads and processes college-related `.txt` documents
- Splits documents into chunks for efficient retrieval
- Generates embeddings using HuggingFace's `all-MiniLM-L6-v2` model
- Stores and searches embeddings using ChromaDB
- Simple chat-based Streamlit interface
- Gracefully handles queries with no matching information

## Tech Stack

- **Python**
- **Streamlit** – chat interface
- **LangChain** – document loading and chunking
- **HuggingFace Embeddings** – semantic vector representations
- **ChromaDB** – vector storage and similarity search

## Project Structure

```
rag_application/
├── app.py              # Main Streamlit application
├── documents/          # Knowledge base (.txt files)
├── vector_store/       # ChromaDB storage
├── requirements.txt    # Python dependencies
└── README.md
```

## How to Run

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Example

**User:** What is the minimum attendance required for exams?
**Bot:** Minimum attendance required is 75% for exams.

## Future Improvements

- Add PDF support
- Integrate an LLM for more natural answer generation
- Improve chat memory and UI

---

**Author:** Neethu O S — B.Tech CSE | Interests: AI, Machine Learning, Data Analysis
