# CrewAI Studio - Nebula Integration

Visual multi-agent orchestration platform with Nebula integration. This is a deployment-ready fork of [CrewAI Studio](https://github.com/strnad/CrewAI-Studio) configured for cloud hosting.

## Features

- 🎨 **Visual Crew Builder** - Drag-and-drop interface for creating multi-agent workflows
- 🤖 **Multi-LLM Support** - OpenAI, Anthropic, Groq, Ollama, and local models
- 🛠️ **40+ Built-in Tools** - Web scraping, APIs, code execution, file operations
- 💾 **Persistent Storage** - SQLite (development) or PostgreSQL (production)
- 🔄 **Real-time Monitoring** - Watch agents work with live output
- 📊 **Results History** - Every crew run saved and searchable
- 🔌 **Nebula Integration** - Sync with your existing Nebula agent network

## Quick Deploy

### Railway

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template)

1. Click the button above
2. Set environment variable: `OPENAI_API_KEY`
3. Deploy!

### Vercel

```bash
vercel deploy
```

### Docker

```bash
docker build -t crewai-studio .
docker run -p 8501:8501 -e OPENAI_API_KEY=your_key crewai-studio
```

## Environment Variables

Required:
- `OPENAI_API_KEY` - Your OpenAI API key

Optional:
- `ANTHROPIC_API_KEY` - Anthropic Claude API key
- `GROQ_API_KEY` - Groq API key
- `DATABASE_URL` - PostgreSQL connection string (defaults to SQLite)

## Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run setup
sh setup.sh

# Start application
streamlit run app.py
```

Access at: http://localhost:8501

## Architecture

```
Nebula Agents → CrewAI Studio GUI → Database → CrewAI Framework
```

## Documentation

- [Complete Setup Guide](../docs/CREWAI_GUI_COMPLETE_GUIDE.md)
- [Architecture Overview](../docs/CREWAI_STUDIO_ARCHITECTURE.md)
- [Integration Bridge](../code/integration/nebula_crewai_bridge.py)

## Original Project

This deployment is based on [CrewAI Studio](https://github.com/strnad/CrewAI-Studio) by strnad.

- ⭐ 1,151 GitHub stars
- 📝 MIT License
- 🔥 Production-ready

## License

MIT License - See LICENSE file for details
