import json
import os

import requests
from langchain.tools import tool
from dotenv import load_dotenv

load_dotenv()


class UtilityTools():
    
    @tool("jigsawstack web scraper")
    def jigsawstack_scraper(target: [str], web_url: str, ) -> str:
        """Useful to search information 
        related with the target in an specific web"""
        
        url = "https://api.jigsawstack.com/v1/ai/scrape"

        payload = {"url": web_url,
                "element_prompts":target}

        headers = {"content-type":"application/json",
                "x-api-key": os.getenv('JIGSAWSTACK_API_KEY')}

        response = requests.request("POST", url, data=payload, headers=headers)
        return response

    @tool("Analyze sentiment on a given piece of text")
    def sentiment_analysis(text: str):
        """Useful to analyze sentiment of a post
        , comment, review"""

        url = "https://api.jigsawstack.com/v1/ai/sentiment"

        payload = {"text": text}

        headers = {"content-type":"application/json",
        "x-api-key":os.getenv('JIGSAWSTACK_API_KEY')}

        response = requests.request("POST", url, data=payload, headers=headers)

        return response

    
