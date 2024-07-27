import json
import os

import requests
from langchain.tools import tool
from dotenv import load_dotenv
from crewai_tools import BaseTool
load_dotenv()


class GigsawstackScraper(BaseTool):
    
    name: str = "jigsawstack web scraper"
    description: str =  """Useful to search information 
        related with the target in an specific web"""

    def _run(self, target: [str], web_url: str) -> str:
        url = "https://api.jigsawstack.com/v1/ai/scrape"

        payload = {"url": web_url,
                "element_prompts":target}

        headers = {"content-type":"application/json",
                "x-api-key": os.getenv('JIGSAWSTACK_API_KEY')}

        response = requests.request("POST", url, data=payload, headers=headers)
        return response