import streamlit as st
import os
import requests
from openai import OpenAI

def get_openai_models():
    """Fetch available OpenAI models dynamically from the API.
    
    Returns:
        list: List of model IDs, or default list if API call fails
    """
    # Current defaults as of January 2026 (from official OpenAI docs)
    default_models = [
        "gpt-5.2",          # Latest flagship (Jan 2026)
        "gpt-5.2-pro",      # Pro version with smarter responses
        "gpt-5",            # Original GPT-5 with configurable reasoning
        "gpt-5-mini",       # Faster, cost-efficient GPT-5
        "gpt-5-nano",       # Fastest, most cost-efficient GPT-5
        "gpt-4.1",          # Smartest non-reasoning model
        "gpt-4o",           # Multimodal with audio (legacy)
        "gpt-4o-mini",      # Cheaper multimodal (legacy)
    ]
    
    try:
        # Try to fetch models from OpenAI API
        api_key = os.environ.get("OPENAI_API_KEY", "")
        if not api_key:
            return default_models
        
        client = OpenAI(api_key=api_key)
        models = client.models.list()
        
        # Filter for chat/completion models only
        gpt_models = [
            m.id for m in models.data 
            if ('gpt' in m.id.lower() or m.id.startswith('o1')) 
            and not any(x in m.id.lower() for x in [
                'whisper', 'tts', 'transcribe', 'embedding', 
                'moderation', 'image', 'realtime', 'audio', 'sora',
                'instruct'  # Exclude instruct-only models
            ])
        ]
        
        # Sort with priority: GPT-5.2 > GPT-5 > GPT-4.1 > GPT-4o > o1 > older
        def model_priority(model_id):
            lower = model_id.lower()
            if 'gpt-5.2-pro' in lower:
                return (0, model_id)
            elif 'gpt-5.2' in lower:
                return (1, model_id)
            elif 'gpt-5-mini' in lower:
                return (2, model_id)
            elif 'gpt-5-nano' in lower:
                return (3, model_id)
            elif 'gpt-5' in lower:
                return (4, model_id)
            elif 'gpt-4.1' in lower:
                return (5, model_id)
            elif 'gpt-4o' in lower:
                return (6, model_id)
            elif model_id.startswith('o1'):
                return (7, model_id)
            else:
                return (8, model_id)
        
        gpt_models.sort(key=model_priority)
        
        # Return fetched models or defaults if none found
        return gpt_models if gpt_models else default_models
        
    except Exception as e:
        # If API call fails, return defaults
        return default_models

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
            ["OpenAI", "GROQ", "Zhipu AI (GLM)", "Ollama"],
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
                help="Choose the OpenAI model (auto-updates from API)"
            )
            
            # Show info about the selected model
            if "5.2-pro" in model:
                st.info("🔥 GPT-5.2 Pro: Most advanced with smarter responses")
            elif "5.2" in model:
                st.info("🚀 GPT-5.2: Latest flagship for coding & agents (Jan 2026)")
            elif "5-mini" in model:
                st.info("⚡ GPT-5 Mini: Fast & cost-efficient")
            elif "5-nano" in model:
                st.info("💨 GPT-5 Nano: Fastest & cheapest")
            elif "5" in model:
                st.info("🧠 GPT-5: Advanced reasoning model")
            elif "4.1" in model:
                st.info("✨ GPT-4.1: Fast non-reasoning model")
            
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
            
        elif provider == "Zhipu AI (GLM)":
            api_key = st.text_input(
                "Zhipu AI API Key",
                type="password",
                help="Get your API key from https://open.bigmodel.cn/usercenter/apikeys"
            )
            if api_key:
                os.environ["ZHIPUAI_API_KEY"] = api_key
            
            # Model selection for Zhipu AI
            model = st.selectbox(
                "Select Model",
                [
                    "glm-4.7",           # Latest flagship (Jan 2026)
                    "glm-4.7-flashx",    # Faster version
                    "glm-4.7-flash",     # Fastest version
                    "glm-4.6",           # Previous version
                ],
                help="GLM models from Zhipu AI - excellent for coding"
            )
            
            st.info("🇨🇳 GLM-4.7: Latest Chinese flagship model with excellent coding capabilities")
            
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
        
        **New:** Zhipu AI GLM-4.7 support added!
        """)
        
        return {"provider": provider, "model": model}