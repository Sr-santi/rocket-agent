import json
import os

import requests

from dotenv import load_dotenv
from crewai_tools import BaseTool
load_dotenv()


class GigsawstackScraper(BaseTool):
    
    name: str = "jigsawstack web scraper"
    description: str =  """Useful to search information 
        related with the target in an specific web
        
        web_url: url of the website
        """

    def _run(self, web_url: str) -> str:
        url = "https://api.jigsawstack.com/v1/ai/scrape"
        # print("target >>>>", target)
        
        # listOftargets = eval(target)
        
        # if not isinstance(listOftargets, list):
        #     raise ValueError("target must be a list")
        
        payload = {"url": web_url, "element_prompts": ['Price', 'Quality', 'Reviews']}

        headers = {"content-type":"application/json",
                "x-api-key": os.getenv('JIGSAWSTACK_API_KEY')}

        response = requests.request("POST", url, data=payload, headers=headers)
        return response