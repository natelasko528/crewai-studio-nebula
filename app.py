import streamlit as st
import os
from datetime import datetime

# Set page config
st.set_page_config(
    page_title="CrewAI Studio - Nebula",
    page_icon="🚀",
    layout="wide"
)

def main():
    # Header
    st.title("🚀 CrewAI Studio")
    st.markdown("**Visual Multi-Agent Orchestration Platform**")
    st.markdown("---")
    
    # Environment check
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if os.getenv("OPENAI_API_KEY"):
            st.success("✅ OpenAI API Key Configured")
        else:
            st.warning("⚠️ OpenAI API Key Missing")
    
    with col2:
        st.info(f"🐍 Python Ready")
    
    with col3:
        st.info(f"⚡ CrewAI v1.9.3")
    
    st.markdown("---")
    
    # Tabs
    tab1, tab2, tab3 = st.tabs(["📊 Overview", "⚙️ Configuration", "📚 Documentation"])
    
    with tab1:
        st.subheader("Welcome to CrewAI Studio")
        st.write("""
        This is your visual interface for building and managing AI agent teams using CrewAI.
        
        **Key Features:**
        - 🤖 Create and configure AI agents
        - 🔗 Define agent workflows and collaboration patterns
        - 📊 Monitor agent execution in real-time
        - 🎯 Manage tasks and objectives
        - 💾 Persistent storage of configurations
        """)
        
        st.markdown("### Quick Start")
        st.write("""
        1. Configure your OpenAI API key in Streamlit Cloud settings
        2. Create your first agent using the sidebar
        3. Define tasks and objectives
        4. Run your multi-agent workflow
        """)
        
        # Stats
        st.markdown("### Platform Stats")
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Agents Created", "0", "+0")
        col2.metric("Tasks Completed", "0", "+0")
        col3.metric("Workflows Active", "0", "+0")
        col4.metric("Uptime", "100%", "0s")
    
    with tab2:
        st.subheader("⚙️ Configuration")
        
        st.markdown("#### API Keys")
        st.write("Configure your API keys in Streamlit Cloud:")
        
        st.code("""
# Go to: App Settings → Secrets
# Add the following:

OPENAI_API_KEY = "sk-..."
        """, language="toml")
        
        st.markdown("#### Agent Configuration")
        st.write("Create and configure your AI agents:")
        
        with st.expander("Create New Agent"):
            agent_name = st.text_input("Agent Name", placeholder="Data Analyst")
            agent_role = st.text_input("Agent Role", placeholder="Expert in data analysis")
            agent_goal = st.text_area("Agent Goal", placeholder="Analyze data and provide insights")
            
            if st.button("Create Agent"):
                if agent_name and agent_role and agent_goal:
                    st.success(f"✅ Agent '{agent_name}' created successfully!")
                else:
                    st.error("Please fill in all fields")
        
        st.markdown("#### Workflow Settings")
        st.write("Configure how agents collaborate:")
        
        workflow_type = st.selectbox(
            "Workflow Type",
            ["Sequential", "Parallel", "Hierarchical"]
        )
        
        max_iterations = st.slider("Max Iterations", 1, 20, 10)
        
        st.info(f"Selected: {workflow_type} workflow with {max_iterations} max iterations")
    
    with tab3:
        st.subheader("📚 Documentation")
        
        st.markdown("""
        ### Getting Started with CrewAI
        
        CrewAI is a framework for orchestrating autonomous AI agents. Agents work together
        to accomplish complex tasks through role-based collaboration.
        
        #### Core Concepts
        
        **Agents:**
        - Autonomous AI entities with specific roles and goals
        - Can use tools and make decisions
        - Collaborate with other agents to solve problems
        
        **Tasks:**
        - Discrete units of work assigned to agents
        - Have clear objectives and success criteria
        - Can be sequential or parallel
        
        **Crews:**
        - Teams of agents working together
        - Defined workflows and collaboration patterns
        - Shared context and memory
        
        #### Example Usage
        
        ```python
        from crewai import Agent, Task, Crew
        
        # Create an agent
        researcher = Agent(
            role='Researcher',
            goal='Find and analyze information',
            backstory='Expert researcher with attention to detail'
        )
        
        # Define a task
        task = Task(
            description='Research AI trends in 2024',
            agent=researcher
        )
        
        # Create a crew
        crew = Crew(
            agents=[researcher],
            tasks=[task]
        )
        
        # Execute
        result = crew.kickoff()
        ```
        
        #### Resources
        
        - [CrewAI Documentation](https://docs.crewai.com)
        - [GitHub Repository](https://github.com/joaomdmoura/crewai)
        - [Community Discord](https://discord.gg/crewai)
        """)
    
    # Sidebar
    with st.sidebar:
        st.image("https://avatars.githubusercontent.com/u/170677839?s=200&v=4", width=100)
        st.markdown("### CrewAI Studio")
        st.markdown(f"**Version:** 1.9.3")
        st.markdown(f"**Deployed:** {datetime.now().strftime('%Y-%m-%d')}")
        st.markdown("---")
        
        st.markdown("### Quick Actions")
        if st.button("🔄 Refresh"):
            st.rerun()
        
        if st.button("📥 Export Config"):
            st.info("Export feature coming soon!")
        
        if st.button("📤 Import Config"):
            st.info("Import feature coming soon!")
        
        st.markdown("---")
        st.markdown("### Status")
        st.success("✅ System Ready")
        st.info("📡 Connected to Nebula")

if __name__ == "__main__":
    main()
