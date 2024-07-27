import random
from textwrap import dedent

from crewai import Crew
from dotenv import load_dotenv

from tools.readCSV import read_and_display_csv
from product_analysis_agents import ConversationAnalysisAgents
from product_analysis_tasks import VoiceAnalysisTasks

load_dotenv()

class VoiceAnalysisCrew:

  def run(self, transcription):
    agents = ConversationAnalysisAgents()
    tasks = VoiceAnalysisTasks()

    process_evaluator_agent = agents.process_evaluator()
    voice_call_evaluator_agent = agents.voice_call_evaluator()

    conversation_analysis = tasks.conversation_analysis_task(process_evaluator_agent,
                                                             transcription)
    conversation_results_evaluation = tasks.results_evaluation(voice_call_evaluator_agent, 
                                                        conversation_analysis)

    crew = Crew(
      agents=[
        voice_call_evaluator_agent,
        process_evaluator_agent,
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
  print("## Welcome to Financial Analysis Crew")
  print('-------------------------------')
  file_path = 'example_files/interesse_information_rows.csv'
  transcriptions = read_and_display_csv(file_path)
  qa_results = []
  random_transcriptions = random.sample(transcriptions, 5)
  for transcription in random_transcriptions:
    voice_qa_crew = VoiceAnalysisCrew()
    result = voice_qa_crew.run(transcription)
    qa_results.append(result)
  
  print("\n\n########################")
  print("## Here is the Report")
  print("########################\n")
  print(qa_results)
