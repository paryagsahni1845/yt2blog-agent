from crewai import Agent
from tools import yt_tool
import os
from load_dotenv import load_dotenv
from langchain_groq import ChatGroq
load_dotenv()
# Get GROQ API key and handle missing key
groq_api_key = os.getenv("GROQ_API_KEY")

# Initialize the model
llm = ChatGroq(
    api_key=groq_api_key,
    model="llama-3.3-70b-versatile",
    temperature=0.7
)



## a senior blog content researcher 
blog_researcher=Agent(
    role='Blog_Researcher from youtube video',
    goal='get the relevant video content for the {topic} from the YT channel',
    verbose=True,
    memory=True,
    backstory=(
        "expert in understanding videos in AI , Data Science , Machine Learning and Gen AI "
    ),
    tools=[yt_tool],
    llm=llm,
    allow_delegation=True
)



# creating a senior blog writer agent with YT tool

blog_writer=Agent(
    role='Blog Writer',
    goal='narrate compelling tech stories about the video {topic} from YT channel',
    verbose=True,
    memory=True,
    backstory=(
        "with a flair for simplifying complex topics , you craft"
        "engaging narratives that captivate and educate,bringing new"
        "discoveries to light in an accessible manner."
    ),
    tools=[yt_tool],
    llm=llm,
    allow_delegation=False 
)