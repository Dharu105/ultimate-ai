from langchain_community.document_loaders import PyPDFLoader

from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_community.vectorstores import FAISS

from utils.embeddings import embedding_model

from langchain_groq import ChatGroq

from dotenv import load_dotenv

import os

load_dotenv()

llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.3-70b-versatile"
)

def pdf_qa(pdf_path, question):

    loader = PyPDFLoader(pdf_path)

    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    split_docs = splitter.split_documents(docs)

    vectorstore = FAISS.from_documents(
        split_docs,
        embedding_model
    )

    docs_found = vectorstore.similarity_search(question)

    context = "\n".join(
        [doc.page_content for doc in docs_found]
    )

    prompt = f"""
    Answer the question based on the PDF context.

    Context:
    {context}

    Question:
    {question}
    """

    response = llm.invoke(prompt)

    return response.content