import os
from crewai import Agent, Task, Crew, Process, LLM

# 1. Configure CrewAI to use the local Ollama instance
local_llm = LLM(
    model='ollama/llama3',
    base_url="http://localhost:11434"
)

# 2. Agent Definition
# Giving the agent a clear identity, goal and background expertise
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

# 3. Task Definition
# Specifying what the agent needs to achive and the expected format
research_task = Task(
    description="""Identify the top 3 major breakthroughs in the field of AI Agents this year.
    Provide a concise summary for each breakthrough and explain its practical impact in the industry.""",
    expected_output="A well structured report containing 3 clear points and a definitive conclusion",
    agent=tech_researcher # assign the task to the agent
)

# 4. Assambling the Crew
# Binding the task and agent together into an execution flow

project_crew = Crew(
    agents=[tech_researcher],
    tasks=[research_task],
    process=Process.sequential,
    planning_llm=local_llm
)

# 5. Kickoff the agent process
if __name__ == "__main__":
    print("### Ai Agent is starting the research process... ###\n")
    result = project_crew.kickoff()
    
    print("\n### Final Raport Output: ###\n")
    print(result)