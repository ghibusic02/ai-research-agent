import os
from crewai import Agent, LLM

# Configure the local ollama LLM
local_llm = LLM(
    model="Ollama/llama3.2:latest",
    base_url="http://localhost:11434"
)

# Define the researcher agent
tech_researcher = Agent(
    role="Senior Technology Researcher",
    goal="Descover the lates advancements and breaktroughs in AI agents in 2026",
    backstory="""You are a tehnology researcher with a high passion for inovation.
    You excel at filtering through vast amount of information to find the most relevant and high-impact news.
    You maintain an analytical, objective tone and always uncover the truth behind tech trends.""",
    verbose= True,#Dysplay the agent's step by step reasoning process in the terminal
    allow_delegation=False,
    llm=local_llm
)

# DEfine the writer agent
content_writer = Agent(
    role="Lead content writer",
    goal="Transform complex tehnical research into accessible and structured blog posts",
    backstory="""You are a proffesional blogger and storyteller.You know how to take 
    tehnical jargon and explain it in a way that anyone can understand.You write with an enthusiastic and proffessional tone.""",
    verbose=True,
    allow_delegation=False,
    llm=local_llm
)