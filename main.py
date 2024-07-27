from textwrap import dedent

from crewai import Crew
from dotenv import load_dotenv

from product_analysis_agents import MarketAnalysisAgents
from product_analysis_tasks import MarketAnalysisTasks

import agentops
load_dotenv()
agentops.init()

class VoiceAnalysisCrew:

  def run(self, product):
    agents = MarketAnalysisAgents()
    tasks = MarketAnalysisTasks()

    web_agent = agents.e_commerce_analyzer()

    conversation_analysis = tasks.e_commerce_evaluation(web_agent,
                                                             product)
    conversation_results_evaluation = tasks.web_search_analysis_task(web_agent, 
                                                        product)

    crew = Crew(
      agents=[
        web_agent
      ],
      tasks=[
        conversation_analysis,
        conversation_results_evaluation,
      ],
      verbose=True
    )

    result = crew.kickoff()
    return result

if __name__ == "__main__":
  print("## Welcome to Market Analysis Crew")
  print('-------------------------------')
  voice_qa_crew = VoiceAnalysisCrew()
  result = voice_qa_crew.run("Razer")
  
  print("\n\n########################")
  print("## Here is the Report")
  print("########################\n")
  print(result)
