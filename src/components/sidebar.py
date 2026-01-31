import streamlit as st
import os
import requests
from openai import OpenAI

def get_openai_models():
    """Fetch available OpenAI models dynamically from the API.
    
    Returns:
        list: List of model IDs, or default list if API call fails
    """
    try:
        # Try to fetch models from OpenAI API
        api_key = os.environ.get("OPENAI_API_KEY", "")
        if not api_key:
            # Return current defaults if no API key
            return [
                "gpt-5.2",          # Latest flagship (Jan 2026)
                "gpt-5.2-pro",      # Pro version
                "gpt-5.1",          # Previous flagship
                "gpt-5",            # Original GPT-5
                "gpt-5-mini",       # Faster/cheaper GPT-5
                "gpt-5-nano",       # Smallest GPT-5
                "gpt-4.1",          # Non-reasoning flagship
                "gpt-4.1-mini",     # Smaller GPT-4.1
                "gpt-4.1-nano",     # Smallest GPT-4.1
                "gpt-4o",           # Multimodal
                "gpt-4o-mini",      # Cheaper multimodal
                "gpt-4-turbo",      # Legacy turbo
                "gpt-3.5-turbo",    # Legacy 3.5
            ]
        
        client = OpenAI(api_key=api_key)
        models = client.models.list()
        
        # Filter for GPT models only (including o-series reasoning models)
        gpt_models = [
            m.id for m in models.data 
            if ('gpt' in m.id.lower() or m.id.startswith('o')) 
            and not any(x in m.id.lower() for x in ['whisper', 'tts', 'transcribe', 'embedding', 'moderation', 'image', 'realtime', 'audio'])
        ]
        
        # Sort with priority: GPT-5.2 > GPT-5 > GPT-4 > o-series > GPT-3
        def model_priority(model_id):
            if 'gpt-5.2' in model_id.lower():
                return (0, model_id)
            elif 'gpt-5' in model_id.lower():
                return (1, model_id)
            elif 'gpt-4' in model_id.lower():
                return (2, model_id)
            elif model_id.startswith('o'):
                return (3, model_id)
            else:
                return (4, model_id)
        
        gpt_models.sort(key=model_priority)
        
        # Return fetched models or defaults if none found
        return gpt_models if gpt_models else [
            "gpt-5.2", "gpt-5.2-pro", "gpt-5.1", "gpt-5", "gpt-5-mini", "gpt-5-nano",
            "gpt-4.1", "gpt-4.1-mini", "gpt-4.1-nano", "gpt-4o", "gpt-4o-mini"
        ]
        
    except Exception as e:
        # If API call fails, return current defaults (Jan 2026)
        return [
            "gpt-5.2",          # Latest flagship (Jan 2026)
            "gpt-5.2-pro",      # Pro version
            "gpt-5.1",          # Previous flagship
            "gpt-5",            # Original GPT-5
            "gpt-5-mini",       # Faster/cheaper GPT-5
            "gpt-5-nano",       # Smallest GPT-5
            "gpt-4.1",          # Non-reasoning flagship
            "gpt-4.1-mini",     # Smaller GPT-4.1
            "gpt-4.1-nano",     # Smallest GPT-4.1
            "gpt-4o",           # Multimodal
            "gpt-4o-mini",      # Cheaper multimodal
            "gpt-4-turbo",      # Legacy turbo
            "gpt-3.5-turbo",    # Legacy 3.5
        ]

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
            
            # Dynamically fetch OpenAI models
            with st.spinner("Loading models..."):
                available_models = get_openai_models()
            
            # Model selection for OpenAI
            model = st.selectbox(
                "Select Model",
                available_models,
                help="Choose the OpenAI model to use (auto-updated from API)"
            )
            
            # Show info about the selected model
            if "5.2" in model:
                st.info("🔥 GPT-5.2 is the latest flagship reasoning model (Jan 2026)")
            elif "5.1" in model or "5" in model:
                st.info("🧠 GPT-5 series: Advanced reasoning models")
            elif "4.1" in model:
                st.info("⚡ GPT-4.1: Fast non-reasoning model")
            
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
        - Dynamic model list (auto-updates)
        - Built-in web search (no extra API keys)
        - Real-time research tracking
        - Structured report generation
        - Citation management
        """)
        
        return {"provider": provider, "model": model}