

import os
import streamlit as st

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

# Page title
st.title("College Information Assistant")

# Load documents
documents = []

folder_path = "documents"

for file in os.listdir(folder_path):
    if file.endswith(".txt"):
        loader = TextLoader(os.path.join(folder_path, file))
        documents.extend(loader.load())

# Split documents
splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50
)

docs = splitter.split_documents(documents)

# Embedding model
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Vector database
vector_db = Chroma.from_documents(
    docs,
    embedding_model,
    persist_directory="vector_store"
)

# Retriever
retriever = vector_db.as_retriever(search_kwargs={"k": 1})

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display old messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])
# User input
prompt = st.chat_input("Ask your question")

if prompt:

    # Show user message
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # Retrieve context
    result = vector_db.similarity_search_with_score(prompt, k=1)

    doc, score = result[0]

    # Tune threshold (adjust later if needed)
    if score > 1.0:
        response = "I could not find this information in the provided documents."
    else:
        response = doc.page_content

    # Show assistant response
    with st.chat_message("assistant"):
        st.markdown(response)

    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )
