# Loading the required libraries
from agents import finance_agent
from agno.playground import Playground,serve_playground_app

app = Playground(agents=[finance_agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("playground:app",reload=True)
    