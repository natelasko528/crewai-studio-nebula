import streamlit as st
import os
import requests

def render_sidebar():
    """Render the sidebar with API key inputs and model selection.
    
    Returns:
        dict: Contains 'provider' and 'model' keys with user selections
    """
    with st.sidebar:
        st.header("⚙️ Configuration")
        
        # Provider selection
        provider = st.selectbox(
            "Select LLM Provider",
            ["OpenAI", "GROQ", "Ollama"],
            help="Choose your preferred language model provider"
        )
        
        # API Key inputs based on provider
        if provider == "OpenAI":
            api_key = st.text_input(
                "OpenAI API Key",
                type="password",
                help="Get your API key from https://platform.openai.com/api-keys"
            )
            if api_key:
                os.environ["OPENAI_API_KEY"] = api_key
            
            # Updated model selection for OpenAI (January 2026)
            model = st.selectbox(
                "Select Model",
                [
                    "gpt-4o",           # Latest GPT-4 Optimized
                    "gpt-4o-mini",      # Faster, cheaper GPT-4o
                    "gpt-4-turbo",      # GPT-4 Turbo
                    "gpt-4",            # Standard GPT-4
                    "gpt-3.5-turbo",    # GPT-3.5
                    "o1",               # o1 reasoning model
                    "o1-mini",          # Smaller o1
                    "o1-preview"        # o1 preview
                ],
                help="Choose the OpenAI model to use"
            )
            
        elif provider == "GROQ":
            api_key = st.text_input(
                "GROQ API Key",
                type="password",
                help="Get your API key from https://console.groq.com/keys"
            )
            if api_key:
                os.environ["GROQ_API_KEY"] = api_key
            
            # Model selection for GROQ
            model = st.selectbox(
                "Select Model",
                ["llama-3.3-70b-versatile", "mixtral-8x7b-32768", "gemma2-9b-it"],
                help="Choose the GROQ model to use"
            )
            
        else:  # Ollama
            st.info("🔧 Make sure Ollama is running locally on port 11434")
            
            # Try to fetch available models from Ollama
            try:
                response = requests.get("http://localhost:11434/api/tags", timeout=2)
                if response.status_code == 200:
                    models_data = response.json()
                    available_models = [model["name"] for model in models_data.get("models", [])]
                    if available_models:
                        model = st.selectbox(
                            "Select Local Model",
                            available_models,
                            help="Choose from your locally installed Ollama models"
                        )
                    else:
                        st.warning("No Ollama models found. Please install models using 'ollama pull <model-name>'")
                        model = None
                else:
                    st.error("Could not connect to Ollama. Make sure it's running.")
                    model = None
            except Exception as e:
                st.error(f"Ollama connection error: {str(e)}")
                model = None
        
        # Information section
        st.divider()
        st.markdown("### 📚 About")
        st.markdown("""
        This research assistant uses CrewAI agents with built-in web search to conduct comprehensive research.
        
        **Features:**
        - Multi-provider LLM support
        - Built-in web search (no extra API keys)
        - Real-time research tracking
        - Structured report generation
        - Citation management
        """)
        
        return {"provider": provider, "model": model}