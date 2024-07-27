import os

from crewai import Agent, Crew, Task
from crewai_tools import SerperDevTool
from dotenv import load_dotenv
from langchain_groq import ChatGroq

from tools.browser_tools import BrowserTools
from tools.search_tools import SearchTools
from tools.utils import UtilityTools

search_tool = SerperDevTool()

# Load environment variables from .env file
load_dotenv()

default_llm = ChatGroq(
    temperature=0.5,
    # model="llama3-70b-8192",
    model="llama-3.1-70b-versatile",
    api_key=os.getenv('GROQ_API_KEY')
)

class MarketAnalysisAgents():
    # TODO: Create Social media analyzer agent
    def e_commerce_analyzer(self):
        return Agent(
            role='E-commerce analyzer',
            goal="""Use the tools to scrap the web and extract price and keywords
            related with the product service you need to search.""",
            backstory="""Develop an advanced e-commerce web scraping agent capable of 
            autonomously navigating through various e-commerce sites and relevant web pages. 
            This agent should be equipped with tools like Selenium for browser automation 
            and Beautiful Soup for parsing HTML content. The core functionalities should 
            include extracting prices, detecting keywords for SEO analysis, and aggregating customer comments for sentiment analysis. 
            Integrate proxy management to handle IP blocking and CAPTCHA-solving services to manage site access challenges. 
            The agent should also incorporate a simple user interface where users can input target URLs and receive structured 
            data outputs (like CSV files) containing the extracted information. Optionally, implement machine learning algorithms 
            to refine keyword extraction and sentiment analysis based on evolving data trends.""",
            tools=[
                BrowserTools.scrape_and_summarize_website,
                SearchTools.search_internet,
                UtilityTools.sentiment_analysis,
                UtilityTools.jigsawstack_scraper
            ],
            verbose=True,
            llm=default_llm,
        )