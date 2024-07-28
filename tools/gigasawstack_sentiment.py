
import os

import requests
from crewai_tools import BaseTool
from dotenv import load_dotenv


load_dotenv()

class GigsawstackSentiment(BaseTool):
    name: str = "Analyze sentiment on a given piece of text"
    description: str =  """Useful to analyze sentiment of a post
        , comment, review"""

    def _run(self, text: str):
        url = "https://api.jigsawstack.com/v1/ai/sentiment"

        payload = {"text": text}

        headers = {"content-type":"application/json",
        "x-api-key":os.getenv('JIGSAWSTACK_API_KEY')}
        print('payload',payload)
        response = requests.post(url, headers=headers, json=headers)
        print(' response', response.json())
        return response.json()

    
