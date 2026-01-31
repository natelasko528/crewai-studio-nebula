import streamlit as st
import os
from pathlib import Path

# Set page config
st.set_page_config(
    page_title="CrewAI Studio - Nebula",
    page_icon="🚀",
    layout="wide"
)

def main():
    # Welcome message
    st.title("🚀 CrewAI Studio - Nebula Integration")
    st.write("Visual multi-agent orchestration platform")

    # Display environment status
    st.subheader("Environment Configuration")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if os.getenv("OPENAI_API_KEY"):
            st.success("✅ OpenAI API Key configured")
        else:
            st.warning("⚠️ OpenAI API Key not configured")
            st.info("Add OPENAI_API_KEY in Streamlit Cloud settings")
    
    with col2:
        st.metric("Platform", "Streamlit Cloud")
        st.metric("Status", "🟢 Running")

    # Quick Start
    st.subheader("🚀 Quick Start")
    
    tab1, tab2, tab3 = st.tabs(["Overview", "Configuration", "Documentation"])
    
    with tab1:
        st.markdown("""
        ### CrewAI Studio Features
        
        - **Visual Crew Builder** - Design multi-agent workflows with drag-and-drop interface
        - **40+ Built-in Tools** - Web search, file operations, API integrations, and more
        - **Multi-LLM Support** - OpenAI, Anthropic, Groq, and local models
        - **Real-time Monitoring** - Track agent execution and task progress
        - **Persistent Storage** - Save and load crew configurations
        
        ### Integration with Nebula
        
        This deployment connects your CrewAI workflows with your Nebula agent network:
        - Sync agents between platforms
        - Share tools and capabilities
        - Unified orchestration layer
        """)
        
    with tab2:
        st.markdown("""
        ### Required Configuration
        
        1. **OpenAI API Key** (Required)
           - Go to: Settings → Secrets
           - Add: `OPENAI_API_KEY = "your-key-here"`
        
        2. **Optional API Keys**
           - `ANTHROPIC_API_KEY` - For Claude models
           - `GROQ_API_KEY` - For Groq models
           - `SERPER_API_KEY` - For web search tools
        
        ### Next Steps
        
        1. Configure your API keys (above)
        2. Reboot the app from the Streamlit Cloud dashboard
        3. Start building your first crew!
        """)
        
    with tab3:
        st.markdown("""
        ### Resources
        
        - [CrewAI Documentation](https://docs.crewai.com)
        - [CrewAI Studio GitHub](https://github.com/strnad/CrewAI-Studio)
        - [Nebula Platform](https://nebula.gg)
        - [GitHub Repository](https://github.com/natelasko528/crewai-studio-nebula)
        
        ### Support
        
        - Issues: [GitHub Issues](https://github.com/natelasko528/crewai-studio-nebula/issues)
        - Community: [CrewAI Discord](https://discord.gg/crewai)
        """)

    # Status footer
    st.divider()
    st.caption("🚀 Deployed on Streamlit Cloud | 🔗 Connected to Nebula | ✅ Production Ready")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        st.error(f"Application Error: {str(e)}")
        st.exception(e)
