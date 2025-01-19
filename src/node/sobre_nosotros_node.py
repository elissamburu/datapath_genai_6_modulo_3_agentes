from typing import Literal
from langchain_core.messages import HumanMessage
from langgraph.graph import MessagesState
from langgraph.types import Command
from src.agents.sobre_nosotros import agente_sobre_nosotros
from src.utils.functions import get_next_node

def sobre_nosotros_nodo(
    state: MessagesState,
) -> Command[Literal["supervisor_nodo"]]:
    #print("############### SOBRE_NOSOTROS_NODE ######################")
    #from src.tools.sobre_nosotros import sobre_nosotros_retriever_tool
    #tool = sobre_nosotros_retriever_tool()
    #resultas = tool.invoke(state["messages"][-1].content)
    #print ("Retrieval")
    #print(resultas)
    #print("############### SOBRE_NOSOTROS_NODE ######################")

    result = agente_sobre_nosotros.invoke(state)

    #goto = get_next_node(result["messages"][-1], "__end__")
    # wrap in a human message, as not all providers allow
    # AI message at the last position of the input messages list
    
    result["messages"][-1] = HumanMessage(
        content=result["messages"][-1].content, name="sobre_nosotros"
    )

    return Command(
        update={
            # share internal message history of research agent with other agents
            "messages": result["messages"],
        },
        goto="supervisor_nodo",
    )