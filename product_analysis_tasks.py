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
      async_execution=True,
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
    async_execution=True,
    agent=agent,
)
  def social_media_analysis_task(self, agent, product):
    return Task(
    description=f"""
    This is the product / service you need to search: {product}
    Conduct focused research on [Product/Service Name] for content creation:

    Identify the trends in social media content, analyze them and include
    that information in your report
    your report will help to create the piece of content that will be
    published
    """,
    expected_output="""
      [trends]
      [popular events]
      [popular people]
      [popular jokes]
    """,
    async_execution=True,
    agent=agent,
)
  def verify_results_task(self, agent):
    return Task(
    description="""
     	•	Data Collection: Gather firsthand accounts and clinical data on hallucinations from various sources including medical journals, online forums, and patient interviews.
      •	Validation Criteria:
      •	Source Credibility: Assess the reliability of the information source.
      •	Consistency Check: Compare reported experiences against established medical understanding of hallucinations.
      •	Context Analysis: Analyze the context in which hallucinations occur, looking for environmental or psychological triggers.
      •	Sentiment Analysis: Use NLP to gauge the emotional tone of the reports to understand the impact of hallucinations on individuals.
      •	Content Creation:
      •	Keyword Extraction: Identify and utilize key terms and phrases related to hallucinations for SEO optimization.
      •	Review Summaries: Compile user reviews and expert opinions to enrich the content.
      •	Image Generation: Create visual content that abstractly represents hallucinations, considering the emotional and psychological elements discussed in the reports.
    """,
    expected_output="""
    Develop a comprehensive content piece that offers insights into hallucinations, 
    supported by validated data, enriched with relevant keywords, reviews, and 
    custom-generated images to enhance reader engagement and understanding.
    """,
    agent=agent,
    # context=[]
)
