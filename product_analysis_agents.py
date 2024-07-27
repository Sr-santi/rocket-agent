import os

from crewai import Agent, Crew, Task
from crewai_tools import SerperDevTool
from dotenv import load_dotenv
from langchain_groq import ChatGroq

search_tool = SerperDevTool()

# Load environment variables from .env file
load_dotenv()

default_llm = ChatGroq(
    temperature=0.5,
    # model="llama3-70b-8192",
    model="llama-3.1-70b-versatile",
    api_key=os.getenv('GROQ_API_KEY')
)

class ConversationAnalysisAgents():
    # I need to compare good evaluations here, i don't have that data
    # TODO: Create dataset with good conversations
    def process_evaluator(self):
        return Agent(
            role='Conversation Evaluator',
            goal="""Evaluate the quality of the evaluation result to check
            if it's accurate.""",
            backstory="""You are an expert in customer service analysis. 
            You are responsible for evaluating and providing insights on 
            the quality of the evaluation.""",
            verbose=False,
            llm=default_llm,
        )
    # WE NEED CONTEXT OF BOTH due to the row data not separated
    def voice_call_evaluator(self):
        return Agent(
            role='Voice call analyzer',
            goal="""Determine the effectiveness of the conversation and provide
            insights for improving the prompts used to sell auto insurance policies""",
            backstory="""You're a researcher at a large insurance company.
            You're responsible for analyzing data and providing insights
            to the business.""",
            verbose=False,
            llm=default_llm, 
        )