
from src.prompts.templates import SYSTEM_DEFAULT_PROMPT
from src.utils.make_system_prompt import make_system_prompt
from src.models.model import llm
from langgraph.prebuilt import create_react_agent

supervisor = create_react_agent(
    llm,
    tools=[],
    state_modifier=make_system_prompt(
       SYSTEM_DEFAULT_PROMPT
    ),
)

agents = ["productos_nodo","stock_nodo","ventas_nodo"]

system_prompt = (
    "Eres un supervisor encargado de gestionar una conversación entre los"
    f" siguientes Agentes: {agents}. Dada la siguiente solicitud del usuario,"
    " responde indicando qué Agente debe actuar a continuación. Cada Agente"
    " realizará una tarea y responderá con sus resultados y estado. Cuando todos"
    #" storekeeper encargado de brindar información sobre  el inventario."
    #" buyer encargado de agregar productos al inventario"
    " hayan terminado, responde con FINISH."

)