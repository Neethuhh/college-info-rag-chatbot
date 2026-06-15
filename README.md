# College Information Assistant (RAG Chatbot)

A Streamlit-based Retrieval-Augmented Generation (RAG) application that allows users to ask questions about college-related information and get instant answers from uploaded documents.

---

## Project Overview

The *College Information Assistant* is an AI-powered chatbot that retrieves relevant information from a local knowledge base (text documents) using embeddings and vector search.

Instead of manually searching through documents, users can simply ask questions and get accurate answers instantly.

---

## Features

- Loads college-related information from `.txt` files  
- Splits documents into meaningful chunks  
- Converts text into embeddings using HuggingFace model  
- Stores embeddings in Chroma vector database  
- Retrieves most relevant information using similarity search  
- Chat-like Streamlit interface  
- Handles unknown queries gracefully  

---

## Project Structure

rag_application/
│
├── app.py              # Main Streamlit application
├── documents/          # Knowledge base (.txt files)
├── vector_store/       # Chroma DB storage
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation

---

## Technologies Used

- Python  
- Streamlit  
- LangChain  
- HuggingFace Embeddings  
- Chroma Vector Database  

---

## How It Works

1. Load text documents from the `documents/` folder  
2. Split documents into small chunks  
3. Convert chunks into vector embeddings  
4. Store embeddings in Chroma DB  
5. When user asks a question:
   - Convert query into embedding  
   - Find most similar document chunk  
   - Return the answer  

---

## Chunking Strategy

- Chunk size: **300 characters**  
- Overlap: **50 characters**

This ensures context is preserved between chunks.

---

## Embedding Model

sentence-transformers/all-MiniLM-L6-v2

- Lightweight and fast  
- Good semantic understanding  
- Suitable for small RAG applications  

---

## Vector Database

- Chroma DB  
- Stores document embeddings  
- Performs similarity search efficiently  
- Supports persistent storage (`vector_store/`)  

---

## How to Run the Project

### 1. Install dependencies
```bash
pip install -r requirements.txt

streamlit run app.py
```
---

## Example Usage

User: What courses are available in CSE department?
Bot: Returns relevant information from documents.

User: What is the fee structure?
Bot: Returns fee details from knowledge base.

---

## Limitations
- Works only on provided .txt documents
- Does not generate new answers (retrieval-based only)
- Accuracy depends on chunk quality and embeddings

---

## Future Improvements
- Add PDF support
- Integrate LLM for better answer generation
- Improve UI with better chat memory handling

---

## Author

Neethu O S
B.Tech Computer Science and Engineering
Interests: Data Analysis, AI, Machine Learning, Web Development