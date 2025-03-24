import os
from dotenv import load_dotenv
from langchain_community.tools import TavilySearchResults


load_dotenv()
tavily_api_key = os.getenv("TAVILY_API_KEY")

Tavily_search_tools = TavilySearchResults(
    max_results=5,
    search_depth="advanced",
    include_answer=True,
    include_raw_content=False,
    include_images=False,
    )


