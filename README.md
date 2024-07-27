# AI Crew for Stock Analysis
## Introduction
This project is an example using the CrewAI framework to automate the process of get information from Amazon, ebay, different websites and social media to get some information to create good social media content for e-commerce. CrewAI orchestrates autonomous AI agents, enabling them to collaborate and execute complex tasks efficiently.

- [CrewAI Framework](#crewai-framework)
- [Running the script](#running-the-script)
- [Details & Explanation](#details--explanation)
- [Using Groq](#using-groq)
- [Using Local Models with Ollama](#using-local-models-with-ollama)
- [Contributing](#contributing)
- [Support and Contact](#support-and-contact)
- [License](#license)

## CrewAI Framework
CrewAI is designed to facilitate the collaboration of role-playing AI agents. In this example, these agents work together to give a complete report about a product and social media trends around this product to perform a social media strategy.

## Running the Script
It uses Llama-70B by default so you should have access to that to run it.

- **Configure Environment**: Copy ``.env.example` and set up the environment variables for [Browseless](https://www.browserless.io/), [Serper](https://serper.dev/), [SEC-API](https://sec-api.io) and [Groq](https://console.groq.com/playground)
- **Install Dependencies**: Run `poetry install --no-root`.
- **Execute the Script**: Run `python main.py` and input your idea.

## Details & Explanation
- **Running the Script**: Execute `python main.py` and input the product / service to be analyzed when prompted. The script will leverage the CrewAI framework to analyze the product and generate a detailed report.
- **Key Components**:
  - `./main.py`: Main script file.
  - `./product_analysis_tasks.py`: Main file with the tasks prompts related with ecommerce sites.
  - `./product_analysis_agents.py`: Main file with the agents creation.
  - `./tools`: Contains tool classes used by the agents.

## Using Groq
CrewAI allow you to pass an llm argument to the agent construtor, that will be it's brain, so changing the agent to use different models is as simple as passing that argument on the agent you want to use that LLM (in `main.py`).
```python
from langchain_groq import ChatGroq

llm = ChatGroq(
    temperature=0,
    model="llama3-70b-8192",
    # api_key="" # Optional if not set as an environment variable
)

def local_expert(self):
	return Agent(
      role='The Best Financial Analyst',
      goal="""Impress all customers with your financial data 
      and market trends analysis""",
      backstory="""The most seasoned financial analyst with 
      lots of expertise in stock market analysis and investment
      strategies that is working for a super important customer.""",
      verbose=True,
      llm=llm, # <----- passing our llm reference here
      tools=[
        BrowserTools.scrape_and_summarize_website,
        SearchTools.search_internet,
        CalculatorTools.calculate,
        SECTools.search_10q,
        SECTools.search_10k
      ]
    )
```

## Using Local Models with Ollama
The CrewAI framework supports integration with local models, such as Ollama, for enhanced flexibility and customization. This allows you to utilize your own models, which can be particularly useful for specialized tasks or data privacy concerns.

### Setting Up Ollama
- **Install Ollama**: Ensure that Ollama is properly installed in your environment. Follow the installation guide provided by Ollama for detailed instructions.
- **Configure Ollama**: Set up Ollama to work with your local model. You will probably need to [tweak the model using a Modelfile](https://github.com/jmorganca/ollama/blob/main/docs/modelfile.md), I'd recommend adding `Observation` as a stop word and playing with `top_p` and `temperature`.

### Integrating Ollama with CrewAI
- Instantiate Ollama Model: Create an instance of the Ollama model. You can specify the model and the base URL during instantiation. For example:

```python
from langchain.llms import Ollama
ollama_openhermes = Ollama(model="openhermes")
# Pass Ollama Model to Agents: When creating your agents within the CrewAI framework, you can pass the Ollama model as an argument to the Agent constructor. For instance:

def local_expert(self):
	return Agent(
      role='The Best Financial Analyst',
      goal="""Impress all customers with your financial data 
      and market trends analysis""",
      backstory="""The most seasoned financial analyst with 
      lots of expertise in stock market analysis and investment
      strategies that is working for a super important customer.""",
      verbose=True,
      llm=ollama_openhermes, # Ollama model passed here
      tools=[
        BrowserTools.scrape_and_summarize_website,
        SearchTools.search_internet,
        CalculatorTools.calculate,
        SECTools.search_10q,
        SECTools.search_10k
      ]
    )
```

### Advantages of Using Local Models
- **Privacy**: Local models allow processing of data within your own infrastructure, ensuring data privacy.
- **Customization**: You can customize the model to better suit the specific needs of your tasks.
- **Performance**: Depending on your setup, local models can offer performance benefits, especially in terms of latency.

## License
This project is released under the MIT License.