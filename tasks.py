from crewai import Task
from crewai.tools import tool
from duckduckgo_search import DDGS
from agents import tech_researcher, content_writer

# Create a web search Tool
@tool("DuckDunkGo Web Search")
def web_search_tool(search_query:str)->str:
    """SEarch on the internet for information regarding a topic and return
    real time web results."""
    try:
        with DDGS() as ddgs:
            # Search on the internet and find the first 4 relvant results
            results = [r for r in ddgs.text(search_query, max_results=4)]
            if results:
                return "\n\n".join([f"Title: {r['title']}\nLink: {r['href']}\nSnippet: {r['body']}" for r in results])
    except Exception as e:
        return f"Search failed due to an error: {str(e)}"
    return "No result found for this query!"
    

# Assign the tool to the researcher agent dynamically
tech_researcher.tools=[web_search_tool]

# Task 1: Research
research_task = Task(
    description="""Use your web search tool to find the top 3 major breakthroughs in the field of AI Agents this year.
    Provide a detailed bullet-point tehnical summary for each breakthrough based on your findings.""",
    expected_output="A detailed list with tehnical facts,summary and source concepts regarding 3 AI agent breakthroughs.",
    agent=tech_researcher
)

# Task 2: Writing
writing_task = Task(
    description="""Review the tehnical research findings provided about AI agent breackthroughs.
    Transform those findings into a compelling, proffesional blog post.
    The post must include an engaging title,an introduction, 3 main sections(for each breackthroughs) with real world impact
    and an inspiring conclusion.""",
    expected_output="A beautifully blog post ready for publication with a clear title and engaging tone.",
    agent=content_writer,
    output_file="ai_agent_blog_post.md"
)