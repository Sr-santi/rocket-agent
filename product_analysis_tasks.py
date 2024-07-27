from textwrap import dedent

from crewai import Task

# Define the evaluation criteria for the conversations
evaluation_criteria = """
1. First Call Resolution (FCR): Was the issue resolved on the first interaction?
2. Average Handle Time (AHT): Was the conversation efficient?
3. Customer Satisfaction (CSAT): Was the customer satisfied with the interaction?
4. Net Promoter Score (NPS): Would the customer recommend the service?
5. Service Level: Was the response time within acceptable limits?
6. Call Abandonment Rate: Did the customer abandon the chat before resolution?
7. Transfer Rate: Was the conversation transferred to another agent or department?
8. Customer Effort Score (CES): How much effort did the customer have to put in to get their issue resolved?
"""

class VoiceAnalysisTasks():
  def results_evaluation(self, agent, results): 
    return Task(description=dedent(f"""
        Evaluate the quality of the results based on the following criteria:
        {evaluation_criteria}
        
        Results:
        {results}
      """),
      agent=agent,
      expected_output= "a boolean that represents if the evaluation is correct or not",
      context=[results]
    )
  def conversation_analysis_task(self, agent, transcript):
    return Task(
    description=f"""Evaluate the quality of the conversation between a chatbot and a 
    human based on the following criteria:
    {evaluation_criteria}
    
    conversation transcription:
    {transcript}
    """,
    expected_output='a bullet point of the concise details of the evaluation',
    agent=agent,
)
