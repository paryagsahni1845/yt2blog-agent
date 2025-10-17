import os
from dotenv import load_dotenv
from crewai import Agent
from tools import yt_tool
from langchain_groq import ChatGroq



# Load environment variables
load_dotenv()
os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"]="gpt-4-0125-preview"


# --- Load GROQ API Key ---
#groq_api_key = os.getenv("GROQ_API_KEY")
#if not groq_api_key:
    #raise ValueError("❌ GROQ_API_KEY not found in environment variables. Please add it to your .env file.")

# --- Initialize Groq LLM ---
#llm = ChatGroq(
    #api_key=groq_api_key,
    #model="llama-3.3-70b-versatile",
    #temperature=0.5
#)

# --- Agents ---

# Blog Researcher Agent
blog_researcher = Agent(
    role="Blog Researcher from YouTube",
    goal="Find the most relevant video content for {topic} from the YouTube channel.",
    verbose=True,
    memory=True,
    backstory=(
        "An expert in analyzing AI, Data Science, Machine Learning, and GenAI content, "
        "you extract core insights from videos to help writers create strong blogs."
    ),
    tools=[yt_tool],
    llm =llm,
    allow_delegation=True
)

# Blog Writer Agent
blog_writer = Agent(
    role="Blog Writer",
    goal="Craft an engaging blog post based on the video content about {topic}.",
    verbose=True,
    memory=True,
    backstory=(
        "You simplify complex AI concepts and turn them into engaging, educational stories "
        "that readers enjoy while learning something new."
    ),
    tools=[yt_tool],
    llm = llm,
    allow_delegation=False
)
