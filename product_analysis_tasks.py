from textwrap import dedent

from crewai import Task

# Define the evaluation criteria for the conversations
evaluation_criteria = """
	1.	Keyword Relevance: Prioritize keywords that directly relate to the core products or services.
	2.	Search Volume: Include keywords with a high search volume to maximize visibility.
	3.	Competition Level: Identify low-competition keywords to increase the chances of ranking higher.
	4.	Trend Analysis: Utilize tools to detect trending keywords and include them in the search process.
	5.	Contextual Fit: Ensure keywords fit naturally within the content to improve SEO and user experience.
"""

class MarketAnalysisTasks():
  def e_commerce_evaluation(self, agent, product): 
    return Task(description=dedent(f"""
        This is the product / service you need to search: {product}
        Search in the main e-commerce sites like:
        - Amazon
        - Ebay
        - Alibaba
        - Taobao
        
        Review prices (values, ranges), review comments and what the people commented
        about an specific product / service
        Create a report that give us the range of prices and the keyword for this search
        
        take in mind the next evaluation criteria:
        {evaluation_criteria}
      """),
      agent=agent,
      expected_output= "{'lowerPrice': number, 'higherPrice': number, 'keywords': [string]}",
    )
  def web_search_analysis_task(self, agent, product):
    return Task(
    description=f"""
    This is the product / service you need to search: {product}
    Conduct focused research on [Product/Service Name] for content creation:

    1.	Keywords: Use tools like Google Keyword Planner to find relevant keywords.
    2.	Pricing: Compare prices across platforms and note competitor discounts.
    3.	Consumer Feedback: Read reviews on e-commerce sites and forums to understand customer perceptions.
    4.	General Info: Gather features and benefits from official and third-party sources.
    
    evaluation_criteria:
    {evaluation_criteria}
    """,
    expected_output="""
    [keywords]
    [reviews / feedback]
    [general information around product/service]
    """,
    agent=agent,
)
