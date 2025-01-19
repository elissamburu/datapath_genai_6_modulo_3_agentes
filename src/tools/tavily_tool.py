import os
from langchain_community.tools.tavily_search import TavilySearchResults
from dotenv import load_dotenv

load_dotenv()


tavily_tool = TavilySearchResults(max_results=5, tavily_api_key=os.getenv("TAVILY_API_KEY"))