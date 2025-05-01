# Loading the required libraries
import os
from dotenv import load_dotenv
from agno.agent import Agent
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.newspaper4k import Newspaper4kTools
from agno.team.team import Team
from agno.models.groq import Groq
from agno.playground import Playground, serve_playground_app

# Loading the groq api key
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")
if not groq_api_key:
    raise ValueError("GROQ_API_KEY is not set in the environment variables.")

# Search agent
websearch_agent = Agent(
    name = "WebSearchAgent",
    role = 'Searches the web for relevant information',
    model = Groq(id = 'gemma2-9b-it',api_key=groq_api_key),
    instructions = [
        "Given a topic, first generate a list of 3 search terms related to that topic.",
        "For each search term, search the web and analyze the results.Return the 10 most relevant URLs to the topic.",
        "You are writing for the New York Times, so the quality of the sources is important.",
    ],
    tools=[DuckDuckGoTools()],
    add_datetime_to_instructions=True
    )

# Writer Agent
content_writer_agent = Agent(
    name = "ContentWriterAgent",
    role = 'Writes a high-quality article',
    model = Groq(id = 'gemma2-9b-it',api_key=groq_api_key),
    description=(
        "You are a senior writer for the New York Times. Given a topic and a list of URLs, "
        "your goal is to write a high-quality NYT-worthy article on the topic."
    ),
    instructions=[
        "First read all urls using `read_article`."
        "Then write a high-quality NYT-worthy article on the topic."
        "The article should be well-structured, informative, engaging and catchy.",
        "Ensure the length is at least as long as a NYT cover story -- at a minimum, 15 paragraphs.",
        "Ensure you provide a nuanced and balanced opinion, quoting facts where possible.",
        "Focus on clarity, coherence, and overall quality.",
        "Never make up facts or plagiarize. Always provide proper attribution.",
        "Remember: you are writing for the New York Times, so the quality of the article is important.",
    ],
    tools=[Newspaper4kTools()],
    add_datetime_to_instructions=True,
)

# Editor Agent
editor_agent = Team(
    name = "EditorAgent",
    mode = "coordinate",
    model = Groq(id = 'gemma2-9b-it',api_key=groq_api_key),
    members = [websearch_agent, content_writer_agent],
    description="You are a senior NYT editor. Given a topic, your goal is to write a NYT worthy article.",
    instructions=[
        "First ask the search journalist to search for the most relevant URLs for that topic.",
        "Then ask the writer to get an engaging draft of the article.",
        "Edit, proofread, and refine the article to ensure it meets the high standards of the New York Times.",
        "The article should be extremely articulate and well written. "
        "Focus on clarity, coherence, and overall quality.",
        "Remember: you are the final gatekeeper before the article is published, so make sure the article is perfect.",
    ],
    add_datetime_to_instructions=True,
    enable_agentic_context=True,
    markdown=True,
    show_members_responses=True,
)

editor_agent.print_response("Write an article about latest developments in AI")

app = Playground(agents=[websearch_agent, content_writer_agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("playground:app", reload=True)