import os

from crewai import Agent, Crew, Task
from crewai_tools import SerperDevTool
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from crewai_tools import WebsiteSearchTool

from tools.browser_tools import BrowserTools
from tools.gigasawstack_sentiment import GigsawstackSentiment
from tools.gigsawstack_scraper import GigsawstackScraper
from tools.search_tools import SearchTools

search_tool = SerperDevTool()

# Load environment variables from .env file
load_dotenv()

default_llm = ChatGroq(
    temperature=0,
    # model="llama3-70b-8192",
    # model="llama-3.1-70b-versatile",
    # model="llama3-groq-70b-8192-tool-use-preview",
    # model="llama3-groq-70b-8192-tool-use-preview",
    model="mixtral-8x7b-32768",
    api_key=os.getenv('GROQ_API_KEY')
)

tool = WebsiteSearchTool()

class MarketAnalysisAgents:

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
                tool,
                SearchTools.search_internet,
                GigsawstackSentiment(),
                # GigsawstackScraper(),
            ],
            max_iter=2,
            verbose=True,
            llm=default_llm,
        )
        
    def social_media_analyzer(self):
        return Agent(
            role='Social Media analyzer',
            goal="""Use the tools to scrap the web and extract social media trends
            that can help to sell and change the marketing strategy
            for a product service you need to search.""",
            backstory="""Develop a social media analyzer agent to monitor current trends 
            and news, ensuring up-to-date awareness of popular topics. This tool should 
            continuously scan major social media platforms and news outlets to gather data 
            on trending hashtags, viral news stories, and widely discussed topics. 
            It should use natural language processing (NLP) to analyze sentiment and relevance,
            providing real-time insights into public perception and interest trends. Additionally, 
            the agent should offer customizable alerts and reports, allowing users to 
            focus on specific areas of interest or sudden shifts in public discourse.""",
            tools=[
                BrowserTools.scrape_and_summarize_website,
                tool,
                SearchTools.search_internet,
                GigsawstackSentiment(),
                # SearchTools.search_news,
            ],
            max_iter=2,
            verbose=True,
            llm=default_llm,
        )

    def validator_agent(self):
        return Agent(
            role='Validator Agent',
            goal="""accurately validate and analyze reports of hallucinations to 
            distinguish between real experiences and hallucinatory perceptions.""",
            backstory="""evaluate reports of hallucinations and verify the accuracy of 
     the information provided. The agent will employ machine 
     learning models and data triangulation techniques to differentiate 
     between real experiences and hallucinations. This agent will also be 
     equipped to assess the contextual and emotional content of the reports, 
     providing insights into common patterns and triggers""",
            tools=[
                BrowserTools.scrape_and_summarize_website,
                tool,
                SearchTools.search_internet,
            ],
            verbose=True,
            max_iter=2,
            llm=default_llm,
        )