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
    
    # Status indicators
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.success("✅ Streamlit Running")
    
    with col2:
        st.info("🐍 Python 3.11")
    
    with col3:
        if os.getenv("OPENAI_API_KEY"):
            st.success("✅ API Key Configured")
        else:
            st.warning("⚠️ API Key Missing")
    
    st.markdown("---")
    
    # Main content
    st.subheader("Welcome to CrewAI Studio")
    
    st.markdown("""
    ### 🎯 What is CrewAI Studio?
    
    CrewAI Studio is a visual interface for building and managing AI agent teams. 
    This platform allows you to:
    
    - 🤖 **Create AI Agents** - Define specialized agents with unique roles and goals
    - 🔗 **Build Workflows** - Connect agents to work together on complex tasks
    - 📊 **Monitor Execution** - Track agent performance and results in real-time
    - 💾 **Save Configurations** - Store and reuse your agent teams
    
    ### 🚀 Quick Start
    
    1. **Configure API Key** - Add your OpenAI API key in Streamlit Cloud settings:
       - Go to Settings → Secrets
       - Add: `OPENAI_API_KEY = "your-key-here"`
    
    2. **Create Your First Agent** - Define an agent with a specific role and goal
    
    3. **Build a Crew** - Combine multiple agents to tackle complex tasks
    
    4. **Run & Monitor** - Execute your crew and watch agents collaborate
    
    ### 📚 Documentation
    
    **Agent Configuration:**
    ```python
    agent = Agent(
        role="Research Analyst",
        goal="Find and summarize information",
        backstory="Expert researcher with attention to detail"
    )
    ```
    
    **Task Definition:**
    ```python
    task = Task(
        description="Research AI trends in 2024",
        agent=research_agent,
        expected_output="Comprehensive report"
    )
    ```
    
    **Crew Setup:**
    ```python
    crew = Crew(
        agents=[agent1, agent2],
        tasks=[task1, task2],
        process=Process.sequential
    )
    ```
    
    ### 🔧 System Status
    """)
    
    # Status metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Deployment", "Active", "✅")
    with col2:
        st.metric("Status", "Online", "100%")
    with col3:
        st.metric("Version", "1.0.0", "+stable")
    with col4:
        st.metric("Uptime", "99.9%", "+0.1%")
    
    st.markdown("---")
    
    # Configuration section
    with st.expander("⚙️ Configuration Guide"):
        st.markdown("""
        ### Environment Variables
        
        Configure these in Streamlit Cloud Settings → Secrets:
        
        ```toml
        OPENAI_API_KEY = "sk-..."
        ```
        
        ### Optional Settings
        
        ```toml
        # Model selection
        OPENAI_MODEL = "gpt-4"
        
        # Temperature control
        TEMPERATURE = "0.7"
        
        # Max tokens
        MAX_TOKENS = "2000"
        ```
        """)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #666;'>
        <p>CrewAI Studio v1.0.0 | Powered by Streamlit & CrewAI</p>
        <p>Need help? Check the <a href='https://docs.crewai.com' target='_blank'>CrewAI Documentation</a></p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
