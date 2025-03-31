
from langgraph.prebuilt import create_react_agent

from agentes.tools import Tavily_search_tools
from core.config import model
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langgraph.graph import MessagesState
from langgraph.managed import IsLastStep
from langchain_core.messages import BaseMessage
from typing import Annotated, TypedDict, Optional
from langgraph.graph import add_messages
from langgraph.checkpoint.memory import MemorySaver
#tools
tools = [Tavily_search_tools]

#graph basico
graph = create_react_agent(model, tools=tools)


#graph2
system_prompt = """" \
Eres un agente que experto en deportes, te llamas agente deportes, tus funciones son:

- Buscar informacion sobre deportes : utiliza la Api Tavily para buscar informacion sobre deportes.
- Generar un resumen de deportes: utiliza la Api Tavily para generar un resumen de deportes.

Tus repuestas deben ser cortas y consisas, y deben contener solo la informacion relevante para el usuario. No incluya información que no este relacionada con el tema.
"""

chat_template_prompt = ChatPromptTemplate.from_messages(
    [
        SystemMessage(content=system_prompt),
        MessagesPlaceholder(variable_name="messages"),
    ]
)
    
    

graph2 = create_react_agent(
    model, 
    tools=tools,
    prompt=chat_template_prompt
    )


# agente #3

system_propmt3 = """
Eres un agente que experto en cocina y  te llamas Angel, tus funciones son:

- Buscar recetas: Utiliza la API Tavily para buscar recetas.
- Generar un resumen de cocina: Utiliza la información obtenida de la API Tavily para generar un resumen de cocina.
- Hazme un paso a paso: Utiliza la API Tavily para generar un resumen de cocina.
- La respuesta debe ser en formato Markdown.
Tus repuestas deben ser cortas y consisas, y deben contener solo la informacion relevante para el usuario. No incluya información que no este relacionada con el tema.
"""

chat_template_prompt_3 = ChatPromptTemplate.from_messages(
    [
        SystemMessage(content=system_propmt3),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

# state
class CustomState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]
    is_last_step: IsLastStep
    remaining_steps:  Optional[int] = None





graph3 = create_react_agent(
    model,
    tools=tools,
    prompt=chat_template_prompt_3,
    state_schema=CustomState,
    checkpointer=MemorySaver()
    )
