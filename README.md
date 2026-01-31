# 🔍 CrewAI Research Assistant

A powerful AI-powered research assistant built with CrewAI and Streamlit that conducts comprehensive research on any topic using AI agents.

## 🌟 Features

- 📱 **Modern Responsive UI** - Clean, intuitive Streamlit interface
- 🤖 **Multi-LLM Support** - OpenAI (GPT-5.2!), GROQ, Zhipu AI (GLM), and Ollama
- 🔄 **Dynamic Model Fetching** - Auto-updates to latest OpenAI models via API
- 🔍 **Built-in Web Search** - Uses CrewAI's native tools (no extra API keys needed)
- 📊 **Real-time Progress** - Live visualization of research process
- 📝 **Structured Reports** - Comprehensive markdown reports with citations
- 📥 **Export Reports** - Download research as markdown files

## 🌐 Supported LLM Providers

### OpenAI (Latest Models - Jan 2026)
- **GPT-5.2** - Flagship model for coding and agentic tasks
- **GPT-5.2 Pro** - Most advanced with smarter responses
- **GPT-5** - Advanced reasoning with configurable effort
- **GPT-5 Mini** - Faster, cost-efficient version
- **GPT-5 Nano** - Fastest, most affordable
- **GPT-4.1** - Smartest non-reasoning model
- Legacy: GPT-4o, GPT-4o-mini

**Model list auto-updates** from OpenAI API when you enter your key!

### GROQ (Fast Inference)
- Llama 3.3 70B Versatile
- Mixtral 8x7B
- Gemma2 9B

### Zhipu AI (GLM) 🇨🇳
- **GLM-4.7** - Latest flagship (Jan 2026)
- GLM-4.7 FlashX - Faster version
- GLM-4.7 Flash - Fastest version
- GLM-4.6 - Previous version

Excellent for coding tasks and Chinese language!

### Ollama (Local)
- Run any Ollama model locally
- No API key required
- Full privacy

## 🚀 Live Demo

Visit the live app: [CrewAI Research Assistant](https://crewai-studio-nebula-93dwdsrfadgvtdjntzrogq.streamlit.app/)

## 📋 Prerequisites

- Python 3.10-3.12
- API Key for your chosen LLM provider:
  - **OpenAI** API Key (for GPT models) OR
  - **GROQ** API Key (for Llama/Mixtral) OR
  - **Zhipu AI** API Key (for GLM models) OR
  - **Ollama** running locally (no API key needed)

**Note:** Web search is built into CrewAI - no additional API keys required!

## 🛠️ Installation

1. **Clone the repository**
```bash
git clone https://github.com/natelasko528/crewai-studio-nebula.git
cd crewai-studio-nebula
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up API keys**

Create a `.streamlit/secrets.toml` file:
```toml
OPENAI_API_KEY = "your-openai-key-here"
# OR
GROQ_API_KEY = "your-groq-key-here"
# OR
ZHIPUAI_API_KEY = "your-zhipuai-key-here"
```

Or set environment variables:
```bash
export OPENAI_API_KEY="your-key"
# OR
export GROQ_API_KEY="your-key"
# OR
export ZHIPUAI_API_KEY="your-key"
```

## 🎯 Usage

1. **Run the application**
```bash
streamlit run app.py
```

2. **Configure in sidebar**
   - Select your LLM provider
   - Enter your API key (or use Ollama locally)
   - Choose your model (OpenAI models auto-update!)

3. **Start researching**
   - Enter your research topic
   - Click "Start Research"
   - Watch the AI agent work in real-time
   - Download your comprehensive report

## 📁 Project Structure

```
crewai-studio-nebula/
├── app.py                          # Main Streamlit application
├── requirements.txt                # Python dependencies
├── .streamlit/
│   └── config.toml                # Streamlit configuration
├── src/
│   ├── __init__.py
│   ├── components/
│   │   ├── __init__.py
│   │   ├── researcher.py          # CrewAI agent with native tools
│   │   └── sidebar.py             # Sidebar configuration UI
│   └── utils/
│       ├── __init__.py
│       └── output_handler.py      # Real-time output capture
└── output/                         # Generated research reports
```

## 🔑 API Keys

### OpenAI
Get your API key from [OpenAI Platform](https://platform.openai.com/api-keys)

The app **automatically fetches** the latest available models from OpenAI's API!

### GROQ
Get your API key from [GROQ Console](https://console.groq.com/keys)

### Zhipu AI (GLM)
Get your API key from [Zhipu AI Platform](https://open.bigmodel.cn/usercenter/apikeys)

### Ollama (Optional)
Install Ollama locally from [ollama.com](https://ollama.com) - no API key needed!

## 🔥 What's New (Jan 2026)

- ✅ **GPT-5.2 Support** - Latest OpenAI flagship model
- ✅ **Dynamic Model Fetching** - Auto-updates to latest models
- ✅ **Zhipu AI GLM** - Chinese flagship models now supported
- ✅ **Removed EXA** - Using CrewAI native tools (simpler setup)
- ✅ **Better Model Info** - Shows model capabilities in UI

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License.

## 🙏 Acknowledgments

- [CrewAI](https://crewai.com) - AI agent framework with built-in tools
- [Streamlit](https://streamlit.io) - Web interface
- [OpenAI](https://openai.com) - GPT-5.2 and other models
- [Zhipu AI](https://www.zhipuai.cn) - GLM models

---

Made with ❤️ using CrewAI and Streamlit