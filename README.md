# RAG-app-using-CHAT-with-Multiple-PDFS and provides Language Translation
This is a RAG (Retrieval-Augmented Generation) PDF-based conversational AI application that allows users to upload multiple PDF documents, extract the text, and interact with the content through a chat interface. Users can ask questions based on the documents and get responses generated from the text. It leverages LangChain for document text processing, embeddings, and conversational retrieval, enabling efficient information retrieval. Additionally, it allows translating the extracted text into different languages.

The Technologies are Framework are as follows:
Frontend: Streamlit (for the interactive web interface)
Backend:
LangChain (for document text processing, embeddings, and conversational retrieval).
FAISS (for vector-based search and similarity retrieval).
PyPDF2 (for PDF text extraction).
HuggingFace Transformers (for generating embeddings and running language models(google-FLAN-T5) and translating Text).


This is how the Frontend Looks like
![chat1](https://github.com/user-attachments/assets/3a5b405d-cfb5-45f9-a930-d6d880fc35d6)

Here the user Can upload multiple pdf files at once
![chat2](https://github.com/user-attachments/assets/d910a4a5-de19-4af0-b300-f49c1e5d67ea)

Then the user can chat and ask questions about the pdf to the interface and it will extract the text and give the response
![chat3](https://github.com/user-attachments/assets/81766e5d-bdf9-4067-be5b-a2547e4316b2)

As mentioned Earlier, the application provides language translation, ATQ to the user choice they can choose the Translation language
![chat4](https://github.com/user-attachments/assets/cdb8f98b-e8bc-4b9e-b34e-0a6ab900f54b)

