# CALM Docs Assistant - Quick Installation Guide

A production-ready conversational AI assistant built with Rasa's CALM (Conversational AI with Language Models) architecture. This project demonstrates how to build a sophisticated documentation assistant that combines LLM intelligence with deterministic control for reliable, enterprise-grade conversational AI.

## Features

- **CALM Architecture**: Hybrid approach combining LLM intelligence with deterministic control
- **Enterprise Search**: RAG-powered knowledge retrieval from documentation
- **GUI Interface**: Web-based chat interface via Rasa Inspector
- **Canary Testing**: Built-in validation system for testing the complete pipeline
- **Clean Codebase**: Minimal, production-ready implementation under 150 lines

## Prerequisites

- Python 3.8 or higher
- Rasa Pro license
- OpenAI API key
- Git (for cloning the repository)

## Quick Start

### 1. Clone and Setup Environment

**All Platforms:**
```bash
git clone https://github.com/deesumblip/rasa-calm-docs-bot_enterprise_search.git
cd rasa-calm-docs-bot_enterprise_search
python -m venv .venv
```

**Activate Virtual Environment:**

**Windows (PowerShell):**
```powershell
.\.venv\Scripts\Activate.ps1
```

**Windows (Command Prompt):**
```cmd
.\.venv\Scripts\activate.bat
```

**Mac/Linux:**
```bash
source .venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

This installs:
- `rasa-pro>=3.1.0` - Rasa Pro with CALM architecture
- `openai>=1.0.0` - OpenAI API client for LLM integration
- `python-dotenv>=1.0.0` - Environment variable management

### 3. Configure Environment Variables

**Step 1: Create and edit a `.env` file with your credentials**
```bash
# Get your Rasa Pro license: https://rasa.com/pro/
RASA_PRO_LICENSE=your_actual_license_here

# Get your OpenAI API key: https://platform.openai.com/api-keys
OPENAI_API_KEY=your_actual_api_key_here
```

**Step 2: Validate your environment setup**
```bash
python autoload_env.py
```

This script will:
- Load your `.env` file automatically
- Check that all required variables are set
- Show you which variables are missing (if any)
- Confirm successful configuration

### 4. Train the Model

```bash
rasa train
```

**Note:** You only need to retrain when you modify:
- `config.yml` - CALM configuration changes
- `domain.yml` - Response definitions
- `data/flows.yml` - Conversation flows
- `data/patterns.yml` - Global patterns
- `docs/` folder - Knowledge base updates

Changes to `actions.py`, `credentials.yml`, or `endpoints.yml` don't require retraining.

### 5. Start the Assistant

**Start in two separate terminals:**

**Terminal 1 - Action Server:**
```bash
rasa run actions
```

**Terminal 2 - Rasa Inspector GUI:**
```bash
rasa inspect --port 5006
```

**Access the Assistant:**
Open your browser to `http://localhost:5006` to chat with the assistant!

## Testing

### Canary Test
Ask: "What is the canary fact?" or "Tell me about canary"

Expected response: "The safe color for deployments is ultramarine kiwi."

### Documentation Questions
Try: "How do I configure CALM?" or "What is Enterprise Search?"

## Project Structure

```
rasa-calm-docs-bot_enterprise_search/
├── .gitignore            # Git ignore rules
├── requirements.txt      # Python dependencies
├── README.md            # This file
├── config.yml           # CALM configuration
├── domain.yml           # Response definitions
├── credentials.yml      # Input channels
├── endpoints.yml        # Action server config
├── autoload_env.py      # Environment loader
├── data/
│   ├── flows.yml       # Conversation flows
│   └── patterns.yml    # Global patterns
├── actions/
│   ├── __init__.py     # Package marker
│   └── actions.py      # Custom actions
├── docs/               # Knowledge base
│   ├── calm_overview.txt
│   ├── canary.txt
│   ├── codespaces_howto.txt
│   ├── config_reference.txt
│   ├── enterprise_search_guide.txt
│   ├── faq.txt
│   ├── flows_and_patterns.txt
│   ├── getting_started.txt
│   ├── glossary.txt
│   └── troubleshooting.txt
└── models/             # Trained model files (auto-generated, gitignored)
```

## Architecture

This project demonstrates Rasa's CALM architecture:

- **SearchReadyLLMCommandGenerator**: Converts user input to structured commands
- **FlowPolicy**: Manages deterministic conversation flows
- **EnterpriseSearchPolicy**: Handles RAG-powered knowledge retrieval
- **Patterns**: Global, interruptible conversation handlers

## Troubleshooting

### Port Conflicts
If port 5005 is in use, use a different port:
```bash
rasa inspect --port 5006
```

### Environment Issues
Validate your environment configuration:
```bash
python autoload_env.py
```

This will show you:
- Whether your `.env` file exists and is loaded
- Which environment variables are set vs. missing
- Helpful guidance for getting missing credentials

### Training Issues
First validate your environment, then train with debug info:
```bash
python autoload_env.py
rasa train --debug
```

### Common Issues

**"rasa command not found"**
- Ensure your virtual environment is activated
- Verify `rasa-pro` is installed: `pip list | grep rasa`

**"Incorrect API key provided" (401 error)**
- Check your `.env` file has the correct `OPENAI_API_KEY`
- Verify the key is valid at https://platform.openai.com/api-keys
- Restart the Rasa server after updating credentials

**"You exceeded your current quota" (429 error)**
- Check your OpenAI usage at https://platform.openai.com/usage
- Add credits to your OpenAI account
- Test with the canary question (doesn't use OpenAI)

**Model training fails**
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Check environment variables: `python autoload_env.py`
- Try training with debug: `rasa train --debug`

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the MIT License.

## Support

For issues and questions:
- Check the troubleshooting section above
- Review Rasa's official documentation
- Open an issue in this repository

## Repository

**GitHub**: https://github.com/deesumblip/rasa-calm-docs-bot_enterprise_search

This repository contains a production-ready CALM implementation with comprehensive documentation, making it an excellent resource for learning Rasa's CALM architecture and building enterprise-grade conversational AI systems.
