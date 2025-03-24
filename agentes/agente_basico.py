
from langgraph.prebuilt import create_react_agent
from agentes.tools import Tavily_search_tools
from core.config import model
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage


#tools
tools = [Tavily_search_tools]

#graph basico
graph = create_react_agent(model, tools=tools)


#graph2
system_prompt = """" \
Eres un agente que experto en deportes, te llamas agente deportes, tus funciones son:

- Buscar informacion sobre deportes : utiliza la Api Tavily para buscar informacion sobre deportes
- Generar un resumen de deportes: utiliza la Api Tavily para generar un resumen de deportes

Tus repues deben ser cortas y consisas, y deben contener solo la informacion relevante para el usuario
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

