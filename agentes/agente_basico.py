
from langgraph.prebuilt import create_react_agent
from agentes.tools import Tavily_search_tools
from core.config import model


#tools
tools = [Tavily_search_tools]

graph = create_react_agent(model, tools=tools)

