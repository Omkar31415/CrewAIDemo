from crewai import Agent
from tools import yt_tool

from dotenv import load_dotenv

load_dotenv()

import os
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"]="gpt-4o-mini"

## Create a senior blog content researcher
blog_researcher=Agent(
    role='Blog Researcher from Youtube Videos',
    goal='Get relevant blog content for the topic{topic} from Youtube videos',
    verbose=True,
    memory=True,
    backstory=(
        "Expert in understanding videos in AI Data Science, Machine Learning, Deep Learning, Gen AI and Python Programming"
    ),
    tools=[yt_tool],
    allow_delegation=True #Will you transfer the work done in this agent to another agent? Yes
)


blog_writer=Agent(
    role='Blog Writer',
    goal='Narrate compelling tech stories about the video {topic} from Youtube videos',
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft"
        "engaging narratives that captivate and educate, bringing new"
        "discoveries to light in an accessible manner."
    ),
    tools=[yt_tool],
    allow_delegation=False
)