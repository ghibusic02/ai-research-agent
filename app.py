import os
from crewai import Crew, Process
from agents import tech_researcher, content_writer, local_llm
from tasks import research_task, writing_task


# Assambling the Multi Agents Crew
# Binding the tasks and agents together into an execution flow

project_crew = Crew(
    agents=[tech_researcher,content_writer],
    tasks=[research_task,writing_task],
    process=Process.sequential,
    planning_llm=local_llm
)

# 5. Kickoff the agent process
if __name__ == "__main__":
    print("### Modular Multi Agents Crew is starting the workflow... ###\n")
    result = project_crew.kickoff()
    
    print("\n### Final Blog Post Output: ###\n")
    print(result)