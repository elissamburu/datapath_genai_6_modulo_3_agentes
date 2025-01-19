from typing import Literal
from typing_extensions import TypedDict
from langchain_core.messages import HumanMessage
from langgraph.graph import StateGraph, START, END, MessagesState
from langgraph.types import Command
from src.agents.supervisor import supervisor
from src.utils.functions import get_next_node
from src.models.model import llm
from src.agents.supervisor import system_prompt

"""def supervisor_nodo(state: MessagesState,) -> Command[Literal["__end__"]]:
    print(supervisor)
    result = supervisor.invoke(state)
    goto = get_next_node(result["messages"][-1], "__end__")
    print(f'goto: {goto}')
    # wrap in a human message, as not all providers allow
    # AI message at the last position of the input messages list
    result["messages"][-1] = HumanMessage(
        content=result["messages"][-1].content, name="supervisor"
    )
    return Command(
        update={
            # share internal message history of research agent with other agents
            "messages": result["messages"],
        },
        goto=goto,
    )"""

class RouterOutput(TypedDict):
    """Agente al que se debe dirigir a continuación. Si no se necesitan más Agente, dirigir a FINISH."""
    next: Literal["productos_nodo","stock_nodo","ventas_nodo", "FINISH"]

def supervisor_node(state: MessagesState): #-> Command[Literal["ventas_stock_nodo",  "__end__"]]:
    messages = [
        {"role": "system", "content": system_prompt},
    ] + state["messages"]
    print("############### SUPERVISOR_NODE ######################")
    print(RouterOutput)
    print(messages)
    response = llm.with_structured_output(RouterOutput).invoke(messages)
    goto = response["next"]
    if goto == "FINISH":
        goto = END
    print(goto)
    print(response)
    print("############### SUPERVISOR_NODE ######################")

    return Command(update={
            #"respuesta_final":state["messages"][-1].content
            "messages": state["messages"][-1].content,
            }, goto=goto)
