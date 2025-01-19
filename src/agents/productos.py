from src.tools.productos import consultar_productos,obtener_producto,actualizar_producto,eliminar_producto
from src.prompts.templates import TEMPLATE_AGENTE_PRODUCTOS
from src.utils.make_system_prompt import make_system_prompt
from src.models.model import llm
from langgraph.prebuilt import create_react_agent

tools = [consultar_productos,obtener_producto,actualizar_producto,eliminar_producto]
agente_productos = create_react_agent(llm, tools=tools, state_modifier=make_system_prompt(TEMPLATE_AGENTE_PRODUCTOS))
