from src.tools.stock import obtener_stock_alerts,obtener_producto_stock,registrar_movimiento,obtener_movimientos_stock
from src.prompts.templates import TEMPLATE_AGENTE_STOCK
from src.utils.make_system_prompt import make_system_prompt
from src.models.model import llm
from langgraph.prebuilt import create_react_agent

tools = [obtener_stock_alerts,obtener_producto_stock,registrar_movimiento,obtener_movimientos_stock]
agente_stock = create_react_agent(llm, tools=tools, state_modifier=make_system_prompt(TEMPLATE_AGENTE_STOCK))
