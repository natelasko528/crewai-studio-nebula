import streamlit as st
import os
import requests
from openai import OpenAI

def get_openai_models():
    """Fetch available OpenAI models dynamically from the API.
    
    Returns:
        list: List of model IDs, or default list if API call fails
    """
    # Current defaults as of January 2026 (from official OpenAI docs - VERIFIED)
    default_models = [
        "gpt-5.2",          # Latest flagship for coding/agents (Jan 2026)
        "gpt-5.2-pro",      # Pro version with smarter responses
        "gpt-5.1",          # Previous flagship with configurable reasoning
        "gpt-5",            # Original GPT-5 with reasoning
        "gpt-5-mini",       # Faster, cost-efficient GPT-5
        "gpt-5-nano",       # Fastest, most cost-efficient GPT-5
        "gpt-4.1",          # Smartest non-reasoning model
        "gpt-4.1-mini",     # Smaller GPT-4.1
        "gpt-4.1-nano",     # Fastest GPT-4.1
        "gpt-4o",           # Multimodal with audio (legacy)
        "gpt-4o-mini",      # Cheaper multimodal (legacy)
    ]
    
    try:
        api_key = os.environ.get("OPENAI_API_KEY", "")
        if not api_key:
            return default_models
        
        client = OpenAI(api_key=api_key)
        models = client.models.list()
        
        # Filter for chat/completion models only
        gpt_models = [
            m.id for m in models.data 
            if ('gpt' in m.id.lower() or m.id.startswith('o')) 
            and not any(x in m.id.lower() for x in [
                'whisper', 'tts', 'transcribe', 'embedding', 
                'moderation', 'image', 'realtime', 'audio', 'sora',
                'instruct', 'chat-latest'
            ])
        ]
        
        # Sort with priority
        def model_priority(model_id):
            lower = model_id.lower()
            if 'gpt-5.2-pro' in lower: return (0, model_id)
            elif 'gpt-5.2' in lower: return (1, model_id)
            elif 'gpt-5.1' in lower: return (2, model_id)
            elif 'gpt-5-mini' in lower: return (3, model_id)
            elif 'gpt-5-nano' in lower: return (4, model_id)
            elif 'gpt-5' in lower: return (5, model_id)
            elif 'gpt-4.1' in lower: return (6, model_id)
            elif 'gpt-4o' in lower: return (7, model_id)
            elif model_id.startswith('o'): return (8, model_id)
            else: return (9, model_id)
        
        gpt_models.sort(key=model_priority)
        return gpt_models if gpt_models else default_models
        
    except Exception:
        return default_models

def render_sidebar():
    """Render the sidebar with API key inputs and model selection.
    
    Returns:
        dict: Contains 'manager_provider', 'manager_model', 'worker_provider', 'worker_model', 'use_hierarchical'
    """
    with st.sidebar:
        st.header("⚙️ Configuration")
        
        # Hierarchical mode toggle
        use_hierarchical = st.checkbox(
            "Use Hierarchical Process",
            value=True,
            help="Enable manager agent to coordinate multiple worker agents for better research quality"
        )
        
        if use_hierarchical:
            st.info("🎯 Hierarchical mode: Manager agent coordinates specialized researchers")
            
            # MANAGER AGENT CONFIGURATION
            st.subheader("👑 Manager Agent")
            manager_provider = st.selectbox(
                "Manager Provider",
                ["Anthropic (Claude)", "OpenAI", "GROQ", "Zhipu AI (GLM)", "Ollama"],
                help="Manager coordinates and validates research. Claude Opus 4.5 recommended for best results."
            )
            
            manager_model, manager_api_key = configure_provider(manager_provider, "manager")
            
            # WORKER AGENT CONFIGURATION
            st.subheader("👥 Worker Agents")
            worker_provider = st.selectbox(
                "Worker Provider",
                ["OpenAI", "Anthropic (Claude)", "GROQ", "Zhipu AI (GLM)", "Ollama"],
                help="Workers perform specialized research tasks. Can be different from manager."
            )
            
            worker_model, worker_api_key = configure_provider(worker_provider, "worker")
            
        else:
            # SINGLE AGENT MODE (Sequential)
            st.info("🔗 Sequential mode: Single agent performs all tasks")
            provider = st.selectbox(
                "Select LLM Provider",
                ["OpenAI", "Anthropic (Claude)", "GROQ", "Zhipu AI (GLM)", "Ollama"],
                help="Choose your preferred language model provider"
            )
            
            manager_model, manager_api_key = configure_provider(provider, "single")
            manager_provider = provider
            worker_provider = provider
            worker_model = manager_model
        
        # Information section
        st.divider()
        st.markdown("### 📚 About")
        st.markdown("""
        **Multi-Agent Research Assistant**
        
        **Hierarchical Mode (Recommended):**
        - Manager agent (Claude Opus 4.5) coordinates research
        - Multiple specialized worker agents
        - Superior quality through validation
        - Cost-optimized
        
        **Features:**
        - Dynamic model fetching
        - Built-in web search
        - Real-time progress
        - Structured reports
        """)
        
        return {
            "use_hierarchical": use_hierarchical,
            "manager_provider": manager_provider,
            "manager_model": manager_model,
            "worker_provider": worker_provider,
            "worker_model": worker_model
        }

def configure_provider(provider, mode):
    """Configure provider-specific settings.
    
    Args:
        provider: Provider name
        mode: "manager", "worker", or "single"
    
    Returns:
        tuple: (model, api_key)
    """
    if provider == "Anthropic (Claude)":
        api_key = st.text_input(
            f"Anthropic API Key ({mode})",
            type="password",
            key=f"anthropic_key_{mode}",
            help="Get your API key from https://console.anthropic.com"
        )
        if api_key:
            os.environ[f"ANTHROPIC_API_KEY_{mode.upper()}"] = api_key
        
        # Claude models (Jan 2026 - VERIFIED)
        model = st.selectbox(
            f"Select Model ({mode})",
            [
                "claude-opus-4-5",      # Latest flagship (Nov 2025)
                "claude-sonnet-4-5",    # Recommended balance (Sep 2025)
                "claude-haiku-4-5",     # Fastest (Oct 2025)
            ],
            key=f"claude_model_{mode}",
            help="Claude 4.5 series with extended thinking support"
        )
        
        if "opus" in model:
            st.success("🔥 Opus 4.5: Best for complex reasoning & manager role")
        elif "sonnet" in model:
            st.info("⚡ Sonnet 4.5: Balanced intelligence/cost/speed")
        elif "haiku" in model:
            st.info("💨 Haiku 4.5: Fastest, most cost-efficient")
        
        return model, api_key
        
    elif provider == "OpenAI":
        api_key = st.text_input(
            f"OpenAI API Key ({mode})",
            type="password",
            key=f"openai_key_{mode}",
            help="Get your API key from https://platform.openai.com/api-keys"
        )
        if api_key:
            os.environ[f"OPENAI_API_KEY_{mode.upper()}"] = api_key
        
        with st.spinner("Loading models..."):
            available_models = get_openai_models()
        
        model = st.selectbox(
            f"Select Model ({mode})",
            available_models,
            key=f"openai_model_{mode}",
            help="Auto-updates from OpenAI API"
        )
        
        if "5.2" in model:
            st.success("🚀 GPT-5.2: Latest flagship for coding/agents")
        elif "5-mini" in model or "5-nano" in model:
            st.info("⚡ Cost-efficient GPT-5 variant")
        elif "4.1" in model:
            st.info("✨ GPT-4.1: Fast non-reasoning model")
        
        return model, api_key
        
    elif provider == "GROQ":
        api_key = st.text_input(
            f"GROQ API Key ({mode})",
            type="password",
            key=f"groq_key_{mode}",
            help="Get your API key from https://console.groq.com/keys"
        )
        if api_key:
            os.environ[f"GROQ_API_KEY_{mode.upper()}"] = api_key
        
        model = st.selectbox(
            f"Select Model ({mode})",
            ["llama-3.3-70b-versatile", "mixtral-8x7b-32768", "gemma2-9b-it"],
            key=f"groq_model_{mode}",
            help="GROQ: Fast inference"
        )
        
        return model, api_key
        
    elif provider == "Zhipu AI (GLM)":
        api_key = st.text_input(
            f"Zhipu AI API Key ({mode})",
            type="password",
            key=f"zhipu_key_{mode}",
            help="Get your API key from https://open.bigmodel.cn/usercenter/apikeys"
        )
        if api_key:
            os.environ[f"ZHIPUAI_API_KEY_{mode.upper()}"] = api_key
        
        model = st.selectbox(
            f"Select Model ({mode})",
            [
                "glm-4.7",           # Latest flagship (Jan 2026)
                "glm-4.7-flashx",    # Fast version
                "glm-4.7-flash",     # Fastest version
            ],
            key=f"glm_model_{mode}",
            help="GLM-4.7: Excellent for coding, 3-5x cheaper than GPT-4"
        )
        
        st.info("🇨🇳 GLM-4.7: Cost-effective with strong coding capabilities")
        
        return model, api_key
        
    else:  # Ollama
        st.info("🔧 Make sure Ollama is running locally on port 11434")
        
        try:
            response = requests.get("http://localhost:11434/api/tags", timeout=2)
            if response.status_code == 200:
                models_data = response.json()
                available_models = [m["name"] for m in models_data.get("models", [])]
                if available_models:
                    model = st.selectbox(
                        f"Select Local Model ({mode})",
                        available_models,
                        key=f"ollama_model_{mode}",
                        help="Locally installed Ollama models"
                    )
                else:
                    st.warning("No Ollama models found. Run 'ollama pull <model-name>'")
                    model = None
            else:
                st.error("Could not connect to Ollama. Make sure it's running.")
                model = None
        except Exception as e:
            st.error(f"Ollama connection error: {str(e)}")
            model = None
        
        return model, None