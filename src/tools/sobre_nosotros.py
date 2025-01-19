from src.utils.vectorStore import create_retriever_tool_instance
from langgraph.graph import MessagesState

def sobre_nosotros_retriever_tool(state:MessagesState):
    """
        Contiene información de la empresa, preguntas frecuentes, garantías, redes sociales, etc.
    """
    try:
        retriever =  create_retriever_tool_instance("sobre_nosotros","Herramienta para obtener información de la empresa, preguntas frecuentes, redes sociales, garantías, etc.","about_us")
        restultado = retriever.invoke(state["messages"][-1].content)
        return restultado
    except Exception as e:
        print(e)
        raise e

