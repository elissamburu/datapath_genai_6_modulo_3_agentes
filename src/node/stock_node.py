from typing import Literal
from langchain_core.messages import HumanMessage
from langgraph.graph import MessagesState
from langgraph.types import Command
from src.agents.stock import agente_stock
from src.utils.functions import get_next_node

def stock_nodo(
    state: MessagesState,
) -> Command[Literal["supervisor_nodo"]]:
    result = agente_stock.invoke(state)
    #goto = get_next_node(result["messages"][-1], "__end__")
    # wrap in a human message, as not all providers allow
    # AI message at the last position of the input messages list
    
    result["messages"][-1] = HumanMessage(
        content=result["messages"][-1].content, name="stock"
    )

    return Command(
        update={
            # share internal message history of research agent with other agents
            "messages": result["messages"],
        },
        goto="supervisor_nodo",
    )