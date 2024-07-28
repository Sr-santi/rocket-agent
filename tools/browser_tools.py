import json
import os
from langchain_groq import ChatGroq

import requests
from crewai import Agent, Task
from langchain.tools import tool
from unstructured.partition.html import partition_html
from dotenv import load_dotenv

# Load environment variables from .env file
# load_dotenv()
# default_llm = ChatGroq(
#     temperature=0,
#     # model="llama3-70b-8192",
#     # model="llama-3.1-70b-versatile",
#     # model="llama3-groq-70b-8192-tool-use-preview",
#     model="llama3-groq-70b-8192-tool-use-preview",
#     # model="mixtral-8x7b-32768",
#     api_key=os.getenv('GROQ_API_KEY')
# )
class BrowserTools():

  @tool("Scrape website content")
  def scrape_and_summarize_website(website):
    """Useful to scrape and summarize a website content"""
    url = f"https://chrome.browserless.io/content?token={os.environ['BROWSERLESS_API_KEY']}"
    payload = json.dumps({"url": website})
    headers = {'cache-control': 'no-cache', 'content-type': 'application/json'}
    response = requests.request("POST", url, headers=headers, data=payload)
    elements = partition_html(text=response.text)
    content = "\n\n".join([str(el) for el in elements])
    content = [content[i:i + 8000] for i in range(0, len(content), 8000)]
    return content
