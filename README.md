# RAG-app-using-CHAT-with-Multiple-PDFS
This is a RAG (Retrieval-Augmented Generation) PDF-based conversational AI application that allows users to upload multiple PDF documents, extract the text, and interact with the content through a chat interface. Users can ask questions based on the documents and get responses generated from the text. It leverages LangChain for document text processing, embeddings, and conversational retrieval, enabling efficient information retrieval. Additionally, it allows translating the extracted text into different languages.

The Technologies are Framework are as follows:
Frontend: Streamlit (for the interactive web interface)
Backend:
LangChain (for document text processing, embeddings, and conversational retrieval).
FAISS (for vector-based search and similarity retrieval).
PyPDF2 (for PDF text extraction).
HuggingFace Transformers (for generating embeddings and running language models(google-FLAN-T5) and translating Text).
