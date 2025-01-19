# from models.embeddings.openai import getModelInstance
import inspect
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os
load_dotenv()

def get_embedding_model_instance():
    # Llamar a la función para obtener la instancia del modelo
    return OpenAIEmbeddings(model="text-embedding-3-small")

