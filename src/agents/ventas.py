
from src.tools.ventas import crear_venta,consultar_venta,obtener_reporte_ventas
from src.prompts.templates import TEMPLATE_AGENTE_VENTAS
from src.utils.make_system_prompt import make_system_prompt
from src.models.model import llm
from langgraph.prebuilt import create_react_agent


tools = [crear_venta,consultar_venta,obtener_reporte_ventas]
agente_ventas = create_react_agent(llm, tools=tools, state_modifier=make_system_prompt(TEMPLATE_AGENTE_VENTAS))
