# 🔍 CrewAI Research Assistant

A powerful AI-powered research assistant built with CrewAI, Streamlit, and Exa that conducts comprehensive research on any topic using AI agents.

## 🌟 Features

- 📱 **Modern Responsive UI** - Clean, intuitive Streamlit interface
- 🤖 **Multi-LLM Support** - OpenAI, GROQ, and Ollama integration
- 🔍 **Advanced Research** - Uses Exa AI for deep web research
- 📊 **Real-time Progress** - Live visualization of research process
- 📝 **Structured Reports** - Comprehensive markdown reports with citations
- 📥 **Export Reports** - Download research as markdown files

## 🚀 Live Demo

Visit the live app: [CrewAI Research Assistant](https://crewai-studio-nebula-93dwdsrfadgvtdjntzrogq.streamlit.app/)

## 📋 Prerequisites

- Python 3.10-3.12
- API Keys:
  - OpenAI API Key (for GPT models) OR GROQ API Key
  - Exa API Key (for research capabilities)
  - Ollama (optional, for local models)

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
GROQ_API_KEY = "your-groq-key-here"
EXA_API_KEY = "your-exa-key-here"
```

Or set environment variables:
```bash
export OPENAI_API_KEY="your-key"
export EXA_API_KEY="your-key"
```

## 🎯 Usage

1. **Run the application**
```bash
streamlit run app.py
```

2. **Configure in sidebar**
   - Select your LLM provider (OpenAI, GROQ, or Ollama)
   - Enter your API keys
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
│   │   ├── researcher.py          # CrewAI agent and tasks
│   │   └── sidebar.py             # Sidebar configuration UI
│   └── utils/
│       ├── __init__.py
│       └── output_handler.py      # Real-time output capture
└── output/                         # Generated research reports
```

## 🔑 API Keys

### OpenAI
Get your API key from [OpenAI Platform](https://platform.openai.com/api-keys)

### GROQ
Get your API key from [GROQ Console](https://console.groq.com/keys)

### Exa
Get your API key from [Exa.ai](https://exa.ai)

### Ollama (Optional)
Install Ollama locally from [ollama.com](https://ollama.com)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License.

## 🙏 Acknowledgments

- [CrewAI](https://crewai.com) - AI agent framework
- [Streamlit](https://streamlit.io) - Web interface
- [Exa](https://exa.ai) - Advanced search capabilities

---

Made with ❤️ using CrewAI, Exa, and Streamlit