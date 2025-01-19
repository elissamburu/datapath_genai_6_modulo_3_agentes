from langgraph.graph import StateGraph, START
from langgraph.graph import MessagesState, END
from src.node.productos_node import productos_nodo
from src.node.ventas_node import ventas_nodo
from src.node.stock_node import stock_nodo

from src.node.supervisor_node import supervisor_node
from langgraph.checkpoint.memory import MemorySaver


workflow = StateGraph(MessagesState)

workflow.add_node("supervisor_nodo", supervisor_node)
workflow.add_node("productos_nodo", productos_nodo)  
workflow.add_node("stock_nodo", stock_nodo) 
workflow.add_node("ventas_nodo", ventas_nodo) 

"""
def decide_next_nodes(context):
    next_nodes = []
    if context.get('necesita_ventas_stock', False):
        next_nodes.append("ventas_stock_nodo")
    # Agrega más condiciones para otros nodos según sea necesario
    return next_nodes if next_nodes else [END]
"""

workflow.add_edge(START, "supervisor_nodo")
checkpointer = MemorySaver()

graph = workflow.compile(checkpointer=checkpointer)



