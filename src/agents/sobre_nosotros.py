from src.tools.sobre_nosotros import sobre_nosotros_retriever_tool
from src.prompts.templates import TEMPLATE_AGENTE_SOBRE_NOSOTROS
from src.utils.make_system_prompt import make_system_prompt
from src.models.model import llm
from langgraph.prebuilt import create_react_agent


tools = [sobre_nosotros_retriever_tool]
agente_sobre_nosotros = create_react_agent(llm, tools=tools, state_modifier=make_system_prompt(TEMPLATE_AGENTE_SOBRE_NOSOTROS))
