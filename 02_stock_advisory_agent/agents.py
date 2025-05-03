# Loading the required libraries
import os
from dotenv import load_dotenv
from agno.agent import Agent
from agno.tools.yfinance import YFinanceTools
from agno.storage.sqlite import SqliteStorage
from instruction_templates import agent_instruction_template_1
from agno.tools.reasoning import ReasoningTools
from agno.models.groq import Groq

# Load environment variables from .env file
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")
os.environ["GROQ_API_KEY"] = groq_api_key

# Fucntion to save the output to a pdf file
def save_to_file(content:str,file_name : str):
    """
    Function to save the content to a file.

    Args:
        content (str): The content to save.
        file_name (str): The name of the file to save the content to.
    
    Returns:
        None
    
    """
    try:
        with open(file_name, 'w') as file:
            file.write(content)
        print(f"Content saved to {file_name}")
    except Exception as e:
        print(f"An error occurred while saving to file: {e}")

# Creating an agent
finance_agent = Agent(
    name = "Finance Analyst",
    description='An agent that can analyze financial data and provide insights.',
    model= Groq(id="llama-3.3-70b-versatile"),
    tools = [
        YFinanceTools(stock_price=True,
                      stock_history=True,
                      analyst_recommendations=True,
                      stock_fundamentals=True,
                      company_overview=True,
                      company_info=True),
        ReasoningTools(add_name_to_instructions=True),
        save_to_file()
    ],
    storage=SqliteStorage("finance_agent.db",table_name="finance_agent"),
    instruction_template=agent_instruction_template_1,
    show_tool_calls=True,
    add_history_to_messages=True,
    add_datetime_to_instructions=True,
    markdown=True
)