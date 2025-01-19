# pip install langchain_community lanchain_openai
#https://python.langchain.com/docs/how_to/#document-loaders
from langchain.document_loaders import (
    UnstructuredMarkdownLoader,
    TextLoader,  
    CSVLoader,  
    JSONLoader,  
    PyPDFLoader,  
    UnstructuredHTMLLoader,  
    DirectoryLoader
) 
from langchain_community.document_loaders import AzureAIDocumentIntelligenceLoader # https://python.langchain.com/docs/how_to/document_loader_office_file/

from langchain_chroma import Chroma
from langchain_openai import ChatOpenAI
from src.models.embeddings import get_embedding_model_instance
from dotenv import load_dotenv
import os
from langchain.tools.retriever import create_retriever_tool

load_dotenv()
from pathlib import Path

database_path =  str(Path(os.environ["VECTOR_DATABASE_PATH"]).absolute()) #"./store/vector_dababase.db"

def create_retriever_tool_instance(name, description, collection_name):
    vectorstores  = Chroma(
        collection_name=collection_name,
        embedding_function=get_embedding_model_instance(),
        persist_directory=database_path
    )

    retriever = vectorstores.as_retriever()
    return create_retriever_tool(retriever=retriever,
        name=name,
        description=description
    )


def get_file_extension(file_path: str):
    extension = os.path.splitext(file_path)
    # file_extension = os.path.splitext(file_path)[1]
    return extension[1].lower()

def get_loader(file_path):  
    _, ext = os.path.splitext(file_path)  
    ext = ext.lower()  # Normalize to lowercase  

    if ext == '.md':  
        return UnstructuredMarkdownLoader(file_path)  
    elif ext == '.txt':  
        return TextLoader(file_path)  
    elif ext == '.csv':  
        return CSVLoader(file_path)  
    elif ext == '.json':  
        return JSONLoader(file_path)  
    elif ext == '.pdf':  
        return PyPDFLoader(file_path)  
    elif ext == '.html':  
        return UnstructuredHTMLLoader(file_path)  
    #elif ext == '.docx':  
    #    return AzureAIDocumentIntelligenceLoader(file_path)  
    else:  
        raise ValueError(f"No loader available for file extension: {ext}")  

def upload_data_from_path(file_path: str, collection_name: str):
    extension = get_file_extension(file_path)
    loader = get_loader(file_path)  
    docs = loader.load()  
    return upload_data(docs,collection_name)
    
def upload_data_from_directory(path: str, collection_name: str):
    # loader = DirectoryLoader("../", glob="**/*.md")
    
    loader = DirectoryLoader(path, glob="**/*.*")
    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print(path)
    docs = loader.load()
    print(docs)
    return upload_data(docs,collection_name)

def upload_data(docs: list[any], collection_name: str):
    print(database_path)
    vectorstores = Chroma.from_documents(
    documents=docs,
    collection_name=collection_name,
    embedding=get_embedding_model_instance(),
    persist_directory=database_path
)
    

## TOOLS
