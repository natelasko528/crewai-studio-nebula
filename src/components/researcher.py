from typing import Type
from crewai import Agent, Task, Crew, Process, LLM
from crewai_tools import SerperDevTool, ScrapeWebsiteTool
import streamlit as st
import os

#--------------------------------#
#         LLM & Research Agent   #
#--------------------------------#
def create_researcher(selection):
    """Create a research agent with the specified LLM configuration.
    
    Args:
        selection (dict): Contains provider and model information
            - provider (str): The LLM provider ("OpenAI", "GROQ", or "Ollama")
            - model (str): The model identifier or name
    
    Returns:
        Agent: A configured CrewAI agent ready for research tasks
    
    Note:
        Uses CrewAI's built-in web search and scraping tools - no external API keys needed.
    """
    provider = selection["provider"]
    model = selection["model"]
    
    if provider == "GROQ":
        llm = LLM(
            api_key=os.environ.get("GROQ_API_KEY", ""),
            model=f"groq/{model}"
        )
    elif provider == "Ollama":
        llm = LLM(
            base_url="http://localhost:11434",
            model=f"ollama/{model}",
        )
    else:  # OpenAI
        llm = LLM(
            api_key=os.environ.get("OPENAI_API_KEY", ""),
            model=f"openai/{model}"
        )
    
    # Use CrewAI's built-in tools - no external API keys needed
    search_tool = SerperDevTool()
    scrape_tool = ScrapeWebsiteTool()
    
    researcher = Agent(
        role='Research Analyst',
        goal='Conduct thorough research on given topics for the current year 2026',
        backstory='Expert at analyzing and summarizing complex information using web research',
        tools=[search_tool, scrape_tool],
        llm=llm,
        verbose=True,
        allow_delegation=False,
    )
    return researcher

#--------------------------------#
#         Research Task          #
#--------------------------------#
def create_research_task(researcher, task_description):
    """Create a research task for the agent to execute.
    
    Args:
        researcher (Agent): The research agent that will perform the task
        task_description (str): The research query or topic to investigate
    
    Returns:
        Task: A configured CrewAI task with expected output format
    """
    return Task(
        description=task_description,
        expected_output="""A comprehensive research report for the year 2026. 
        The report must be detailed yet concise, focusing on the most significant and impactful findings.
        
        Format the output in clean markdown (without code block markers or backticks) using the following structure:

        # Executive Summary
        - Brief overview of the research topic (2-3 sentences)
        - Key highlights and main conclusions
        - Significance of the findings

        # Key Findings
        - Major discoveries and developments
        - Market trends and industry impacts
        - Statistical data and metrics (when available)
        - Technological advancements
        - Challenges and opportunities

        # Analysis
        - Detailed examination of each key finding
        - Comparative analysis with previous developments
        - Industry expert opinions and insights
        - Market implications and business impact

        # Future Implications
        - Short-term impacts (next 6-12 months)
        - Long-term projections
        - Potential disruptions and innovations
        - Emerging trends to watch

        # Recommendations
        - Strategic suggestions for stakeholders
        - Action items and next steps
        - Risk mitigation strategies
        - Investment or focus areas

        # Citations
        - List all sources with titles and URLs
        - Include publication dates when available
        - Prioritize recent and authoritative sources
        - Format as: "[Title] (URL) - [Publication Date if available]"

        Note: Ensure all information is current and relevant to 2026. Include specific dates, 
        numbers, and metrics whenever possible to support findings. All claims should be properly 
        cited using the sources discovered during research.
        """,
        agent=researcher,
        output_file="output/research_report.md"
    )

#--------------------------------#
#         Research Crew          #
#--------------------------------#
def run_research(researcher, task):
    """Execute the research task using the configured agent.
    
    Args:
        researcher (Agent): The research agent to perform the task
        task (Task): The research task to execute
    
    Returns:
        str: The research results in markdown format
    """
    crew = Crew(
        agents=[researcher],
        tasks=[task],
        verbose=True,
        process=Process.sequential
    )
    
    return crew.kickoff()