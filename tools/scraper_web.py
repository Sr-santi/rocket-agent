import os

import requests
from crewai_tools import tool
from dotenv import load_dotenv

load_dotenv()

@tool("jigsawstack web scraper")
def jigsawstack_scraper(target: str) -> str:
    """Useful to search information 
    related with the target in an specific web"""
    
    url = "https://api.jigsawstack.com/v1/ai/scrape"

    payload = {"url":"https://news.ycombinator.com/show",
            "element_prompts":[target]}

    headers = {"content-type":"application/json",
            "x-api-key": os.getenv('JIGSAWSTACK_API_KEY')}

    response = requests.request("POST", url, data=payload, headers=headers)
    return response