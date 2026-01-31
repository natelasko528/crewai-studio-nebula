# 🔍 CrewAI Research Assistant

A powerful AI-powered research assistant built with CrewAI and Streamlit that conducts comprehensive research on any topic using AI agents.

## 🌟 Features

- 📱 **Modern Responsive UI** - Clean, intuitive Streamlit interface
- 🤖 **Multi-LLM Support** - OpenAI, GROQ, and Ollama integration
- 🔍 **Built-in Web Search** - Uses CrewAI's native tools (no extra API keys needed)
- 📊 **Real-time Progress** - Live visualization of research process
- 📝 **Structured Reports** - Comprehensive markdown reports with citations
- 📥 **Export Reports** - Download research as markdown files

## 🚀 Live Demo

Visit the live app: [CrewAI Research Assistant](https://crewai-studio-nebula-93dwdsrfadgvtdjntzrogq.streamlit.app/)

## 📋 Prerequisites

- Python 3.10-3.12
- API Key for your chosen LLM provider:
  - **OpenAI** API Key (for GPT models) OR
  - **GROQ** API Key (for Llama/Mixtral) OR
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
```

Or set environment variables:
```bash
export OPENAI_API_KEY="your-key"
# OR
export GROQ_API_KEY="your-key"
```

## 🎯 Usage

1. **Run the application**
```bash
streamlit run app.py
```

2. **Configure in sidebar**
   - Select your LLM provider (OpenAI, GROQ, or Ollama)
   - Enter your API key (or use Ollama locally)
   - Choose your model

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

**Available Models:**
- gpt-4o (latest, recommended)
- gpt-4o-mini (faster/cheaper)
- gpt-4-turbo
- gpt-4
- gpt-3.5-turbo
- o1, o1-mini, o1-preview

### GROQ
Get your API key from [GROQ Console](https://console.groq.com/keys)

**Available Models:**
- llama-3.3-70b-versatile
- mixtral-8x7b-32768
- gemma2-9b-it

### Ollama (Optional)
Install Ollama locally from [ollama.com](https://ollama.com) - no API key needed!

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License.

## 🙏 Acknowledgments

- [CrewAI](https://crewai.com) - AI agent framework with built-in tools
- [Streamlit](https://streamlit.io) - Web interface

---

Made with ❤️ using CrewAI and Streamlit