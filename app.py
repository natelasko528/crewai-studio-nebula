import streamlit as st
import os
from pathlib import Path

# Set page config
st.set_page_config(
    page_title="CrewAI Studio - Nebula",
    page_icon="🚀",
    layout="wide"
)

# Welcome message
st.title("🚀 CrewAI Studio - Nebula Integration")
st.write("Visual multi-agent orchestration platform")

# Note about full deployment
st.info("""
This is a deployment placeholder. The full CrewAI Studio application will be cloned
from the official repository during deployment.

Repository: https://github.com/strnad/CrewAI-Studio
""")

# Display environment status
st.subheader("Environment Configuration")
if os.getenv("OPENAI_API_KEY"):
    st.success("✅ OpenAI API Key configured")
else:
    st.warning("⚠️ OpenAI API Key not configured")

# Instructions
st.subheader("Setup Instructions")
st.markdown("""
1. Configure your API keys in the environment variables
2. The full application will initialize on first deployment
3. Access the visual crew builder interface
4. Create and execute multi-agent workflows
""")
