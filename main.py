import os
from crewai import Crew
from dotenv import load_dotenv

from product_analysis_agents import MarketAnalysisAgents
from product_analysis_tasks import MarketAnalysisTasks

from crewai import Crew
import yaml
from dotenv import load_dotenv
from pathlib import Path
from crewai import Agent, Task, Crew, Process
from langchain_groq import ChatGroq

import agentops
load_dotenv()
agentops.init()

class VoiceAnalysisCrew:

  def run(self, product):
    agents = MarketAnalysisAgents()
    tasks = MarketAnalysisTasks()
    web_agent = agents.e_commerce_analyzer()
    social_media_agent = agents.social_media_analyzer()
    validator_agent = agents.validator_agent()
    print('web_agent', web_agent)

    ecommerce_analysis = tasks.e_commerce_evaluation(web_agent,
                                                             product)
    social_media_analysis = tasks.social_media_analysis_task(social_media_agent,
                                                             product)
    web_results_evaluation = tasks.web_search_analysis_task(web_agent, 
                                                        product)
    validator_evaluation = tasks.verify_results_task(validator_agent)
    
    

    crew = Crew(
      agents=[
        web_agent,
        social_media_agent,
        validator_agent,
      ],
      tasks=[
        ecommerce_analysis,
        web_results_evaluation,
        social_media_analysis,
        validator_evaluation
      ],
      verbose=True
    )

    result = crew.kickoff()
    return result

if __name__ == "__main__":
  print("## Welcome to Market Analysis Crew")
  print('-------------------------------')
  company = input("Enter the company name: ")
  product = input("Enter the product name: ")
  voice_qa_crew = VoiceAnalysisCrew()
  report = voice_qa_crew.run(product)
  
  print("\n\n########################")
  print("## Here is the Report")
  print("########################\n")
  
  # Use Path for file locations
  current_dir = Path.cwd()
  agents_config_path = current_dir / "config" / "agents.yaml"
  tasks_config_path = current_dir / "config" / "tasks.yaml"

  # Load YAML configuration files
  with open(agents_config_path, "r") as file:
      agents_config = yaml.safe_load(file)

  with open(tasks_config_path, "r") as file:
      tasks_config = yaml.safe_load(file)

  ## Define Agents
  BriefIntakeAgent = Agent(
      config=agents_config["BriefIntakeAgent"], allow_delegation=False, verbose=True, llm=ChatGroq(
    temperature=0.5,
    model="llama3-70b-8192",
    api_key=os.getenv("GROQ_API_KEY")
  ))

  BriefAnalysisAgent = Agent(config=agents_config["BriefAnalysisAgent"], allow_delegation=False, verbose=True, llm=ChatGroq(
    temperature=0.5,
    model="llama3-70b-8192",
    api_key=os.getenv("GROQ_API_KEY")
  ))


  ContentCreationAgent = Agent(config=agents_config["ContentCreationAgent"], allow_delegation=False, verbose=True, llm=ChatGroq(
    temperature=0.5,
    model="llama3-70b-8192",
    api_key=os.getenv("GROQ_API_KEY"),
  ))




  # Take in marketing brief
  intake = Task(
      description=tasks_config["intake"]["description"],
      expected_output=tasks_config["intake"]["expected_output"],
      agent=BriefIntakeAgent,
  )
  result = intake.execute_sync()
  if "STOP" in result:
      # stop here and proceed to next post
      print("Issue #1")

  #Analyse the info collected
  analysis = Task(
      description=tasks_config["analysis"]["description"],
      expected_output=tasks_config["analysis"]["expected_output"],
      agent=BriefAnalysisAgent,
  )

  creation = Task(
      description=tasks_config["creation"]["description"],
      expected_output=tasks_config["creation"]["expected_output"],
      agent=ContentCreationAgent,
  )

  crew = Crew(
      agents=[BriefIntakeAgent, BriefAnalysisAgent, ContentCreationAgent],
      tasks=[intake, analysis, creation],
      verbose=2,  # Crew verbose more will let you know what tasks are being worked on, you can set it to 1 or 2 to different logging levels
      process=Process.sequential,  # Sequential process will have tasks executed one after the other and the outcome of the previous one is passed as extra content into this next.
  )

  result = crew.kickoff(inputs={"brief": report.raw, "company": company})
  print(result)
