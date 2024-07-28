from crewai import Crew
from dotenv import load_dotenv

from product_analysis_agents import MarketAnalysisAgents
from product_analysis_tasks import MarketAnalysisTasks

from crewai import Crew
from dotenv import load_dotenv

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
  voice_qa_crew = VoiceAnalysisCrew()
  result = voice_qa_crew.run("razors in the market")
  
  print("\n\n########################")
  print("## Here is the Report")
  print("########################\n")
  print(result)
