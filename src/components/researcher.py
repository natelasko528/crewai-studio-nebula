from typing import Type
from crewai import Agent, Task, Crew, Process, LLM
from crewai_tools import SerperDevTool, ScrapeWebsiteTool
from langchain_community.chat_models import ChatZhipuAI
import streamlit as st
import os

#--------------------------------#
#         LLM Creation           #
#--------------------------------#
def create_llm(provider, model, mode="worker"):
    """Create LLM instance based on provider and model.
    
    Args:
        provider: Provider name ("OpenAI", "Anthropic (Claude)", etc.)
        model: Model identifier
        mode: "manager" or "worker" for API key selection
    
    Returns:
        LLM or ChatModel instance
    """
    api_key_suffix = mode.upper()
    
    if provider == "Anthropic (Claude)":
        api_key = os.environ.get(f"ANTHROPIC_API_KEY_{api_key_suffix}") or os.environ.get("ANTHROPIC_API_KEY")
        return LLM(
            model=f"anthropic/{model}",
            api_key=api_key,
            temperature=0.3 if mode == "manager" else 0.7,  # Lower temp for manager consistency
            max_tokens=8192
        )
    
    elif provider == "OpenAI":
        api_key = os.environ.get(f"OPENAI_API_KEY_{api_key_suffix}") or os.environ.get("OPENAI_API_KEY")
        return LLM(
            model=f"openai/{model}",
            api_key=api_key,
            temperature=0.3 if mode == "manager" else 0.7
        )
    
    elif provider == "GROQ":
        api_key = os.environ.get(f"GROQ_API_KEY_{api_key_suffix}") or os.environ.get("GROQ_API_KEY")
        return LLM(
            model=f"groq/{model}",
            api_key=api_key,
            temperature=0.7
        )
    
    elif provider == "Zhipu AI (GLM)":
        # Use LangChain's ChatZhipuAI for GLM models
        api_key = os.environ.get(f"ZHIPUAI_API_KEY_{api_key_suffix}") or os.environ.get("ZHIPUAI_API_KEY")
        return ChatZhipuAI(
            api_key=api_key,
            model=model,
            temperature=0.7
        )
    
    else:  # Ollama
        return LLM(
            base_url="http://localhost:11434",
            model=f"ollama/{model}",
            temperature=0.7
        )

#--------------------------------#
#         Manager Agent          #
#--------------------------------#
def create_manager_agent(config):
    """Create manager agent for hierarchical process.
    
    Args:
        config: Configuration dict with manager_provider and manager_model
    
    Returns:
        Agent: Manager agent configured for delegation and coordination
    """
    manager_llm = create_llm(
        config["manager_provider"],
        config["manager_model"],
        mode="manager"
    )
    
    manager = Agent(
        role="Research Director",
        goal="Coordinate research team to produce comprehensive, accurate, and well-cited analysis",
        backstory="""You are an expert research director with decades of experience managing 
        complex research projects. You excel at:
        - Breaking down complex topics into focused research tasks
        - Delegating work strategically to specialist researchers
        - Validating findings for accuracy and completeness
        - Synthesizing insights into coherent, actionable reports
        - Ensuring all claims are properly cited with authoritative sources
        
        Your role is to coordinate the research team, not to do the research yourself. 
        Delegate specific tasks to your specialized researchers and validate their work.""",
        llm=manager_llm,
        allow_delegation=True,  # Critical for hierarchical process
        verbose=True
    )
    
    return manager

#--------------------------------#
#         Worker Agents          #
#--------------------------------#
def create_worker_agents(config):
    """Create specialized worker agents for research tasks.
    
    Args:
        config: Configuration dict with worker_provider and worker_model
    
    Returns:
        list: List of specialized research agents
    """
    worker_llm = create_llm(
        config["worker_provider"],
        config["worker_model"],
        mode="worker"
    )
    
    # Built-in tools for all workers
    search_tool = SerperDevTool()
    scrape_tool = ScrapeWebsiteTool()
    
    # Web Research Specialist
    web_researcher = Agent(
        role='Web Research Specialist',
        goal='Find and extract comprehensive information from authoritative web sources',
        backstory="""You are an expert web researcher skilled at:
        - Locating authoritative sources through strategic search queries
        - Extracting relevant information from websites and documents
        - Identifying credible sources and cross-referencing information
        - Gathering recent data, statistics, and expert opinions
        
        Your research is thorough, well-sourced, and focused on current information.""",
        llm=worker_llm,
        tools=[search_tool, scrape_tool],
        allow_delegation=False,
        verbose=True
    )
    
    # Data Analysis Specialist
    data_analyst = Agent(
        role='Data Analysis Specialist',
        goal='Analyze research findings to identify patterns, trends, and actionable insights',
        backstory="""You are an experienced data analyst skilled at:
        - Identifying patterns and trends in research data
        - Performing comparative analysis across multiple sources
        - Extracting key metrics and statistical insights
        - Translating complex data into clear, actionable findings
        
        Your analysis is rigorous, data-driven, and highlights what matters most.""",
        llm=worker_llm,
        tools=[search_tool],
        allow_delegation=False,
        verbose=True
    )
    
    # Fact Verification Specialist
    fact_checker = Agent(
        role='Fact Verification Specialist',
        goal='Verify accuracy of claims and validate source credibility',
        backstory="""You are a meticulous fact-checker focused on:
        - Cross-referencing claims across multiple authoritative sources
        - Validating source credibility and publication dates
        - Identifying and flagging unsubstantiated claims
        - Ensuring all information is current and accurate
        
        Your verification ensures research quality and trustworthiness.""",
        llm=worker_llm,
        tools=[search_tool, scrape_tool],
        allow_delegation=False,
        verbose=True
    )
    
    return [web_researcher, data_analyst, fact_checker]

#--------------------------------#
#         Research Tasks         #
#--------------------------------#
def create_research_tasks(agents, task_description):
    """Create research tasks for the worker agents.
    
    Args:
        agents: List of worker agents [web_researcher, data_analyst, fact_checker]
        task_description: User's research query
    
    Returns:
        list: List of tasks for the crew
    """
    web_researcher, data_analyst, fact_checker = agents
    
    # Task 1: Web Research
    research_task = Task(
        description=f"""Conduct comprehensive web research on: {task_description}
        
        Your objectives:
        1. Find authoritative sources (academic, industry leaders, official reports)
        2. Gather recent data, statistics, and developments (prioritize 2025-2026)
        3. Extract key facts, trends, and expert opinions
        4. Document all sources with URLs and publication dates
        
        Focus on breadth and quality of sources.""",
        expected_output="""Detailed research findings including:
        - Key facts and developments
        - Recent statistics and data points
        - Expert opinions and industry insights
        - List of authoritative sources with URLs and dates""",
        agent=web_researcher
    )
    
    # Task 2: Data Analysis
    analysis_task = Task(
        description="""Analyze the research findings to identify:
        1. Major patterns and trends
        2. Comparative insights (changes over time, market positioning)
        3. Key metrics and their significance
        4. Emerging opportunities and challenges
        
        Provide structured, data-driven analysis.""",
        expected_output="""Structured analysis including:
        - Major trends and their implications
        - Comparative insights with context
        - Key metrics with interpretation
        - Strategic opportunities and risks""",
        agent=data_analyst
    )
    
    # Task 3: Fact Verification
    verification_task = Task(
        description="""Verify the accuracy and credibility of all research findings:
        1. Cross-reference major claims across sources
        2. Validate source credibility and recency
        3. Flag any unsubstantiated or outdated claims
        4. Confirm all statistics and data points
        
        Ensure research meets high quality standards.""",
        expected_output="""Verification report including:
        - Confirmed facts with supporting sources
        - Source credibility assessment
        - Any flagged concerns or corrections
        - Overall quality and reliability rating""",
        agent=fact_checker
    )
    
    return [research_task, analysis_task, verification_task]

#--------------------------------#
#         Sequential Mode        #
#--------------------------------#
def create_single_agent(config):
    """Create single agent for sequential (non-hierarchical) mode.
    
    Args:
        config: Configuration dict
    
    Returns:
        Agent: Single research agent
    """
    llm = create_llm(
        config["manager_provider"],  # Use manager config for single agent
        config["manager_model"],
        mode="worker"
    )
    
    search_tool = SerperDevTool()
    scrape_tool = ScrapeWebsiteTool()
    
    researcher = Agent(
        role='Research Analyst',
        goal='Conduct thorough research on given topics for the current year 2026',
        backstory='Expert at analyzing and summarizing complex information using web research',
        tools=[search_tool, scrape_tool],
        llm=llm,
        verbose=True,
        allow_delegation=False
    )
    
    return researcher

def create_single_task(agent, task_description):
    """Create single task for sequential mode.
    
    Args:
        agent: Research agent
        task_description: User's research query
    
    Returns:
        Task: Research task
    """
    return Task(
        description=task_description,
        expected_output="""A comprehensive research report for the year 2026. 
        Format in clean markdown with:
        
        # Executive Summary
        Brief overview and key findings
        
        # Key Findings
        Major discoveries, trends, data points
        
        # Analysis
        Detailed examination and implications
        
        # Future Implications
        Short-term and long-term projections
        
        # Recommendations
        Strategic suggestions and action items
        
        # Citations
        All sources with URLs and dates""",
        agent=agent,
        output_file="output/research_report.md"
    )

#--------------------------------#
#         Crew Execution         #
#--------------------------------#
def run_research(config, task_description):
    """Execute research using configured agents and process.
    
    Args:
        config: Configuration dict from sidebar
        task_description: User's research query
    
    Returns:
        str: Research results
    """
    if config["use_hierarchical"]:
        # HIERARCHICAL MODE: Manager + Workers
        manager = create_manager_agent(config)
        workers = create_worker_agents(config)
        tasks = create_research_tasks(workers, task_description)
        
        crew = Crew(
            agents=workers,
            tasks=tasks,
            manager_agent=manager,  # Use custom manager agent
            process=Process.hierarchical,
            verbose=True,
            planning=True  # Enable automatic planning
        )
    else:
        # SEQUENTIAL MODE: Single Agent
        agent = create_single_agent(config)
        task = create_single_task(agent, task_description)
        
        crew = Crew(
            agents=[agent],
            tasks=[task],
            verbose=True,
            process=Process.sequential
        )
    
    return crew.kickoff()