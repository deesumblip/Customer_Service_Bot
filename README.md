# Shell Energy Customer Service Assistant - Technical Assignment Submission

A production-ready conversational AI assistant built with Rasa's CALM (Conversational AI with Language Models) architecture. This project demonstrates how to build a sophisticated energy company customer service assistant that combines LLM intelligence with deterministic control for reliable, enterprise-grade conversational AI.

## Assignment Overview

This repository contains a complete implementation of Rasa's CALM architecture for a technical assignment submission. The assistant demonstrates:

- **Hybrid AI Architecture**: Combines LLM flexibility with deterministic control
- **Enterprise Search Integration**: RAG-powered knowledge retrieval from Shell Energy FAQ database
- **Production-Ready Code**: Clean, minimal implementation under 150 lines
- **Comprehensive Testing**: Built-in canary test for pipeline validation
- **Complete Documentation**: Detailed setup and troubleshooting guides

## Technical Implementation

- **CALM Components**: SearchReadyLLMCommandGenerator, FlowPolicy, EnterpriseSearchPolicy
- **Knowledge Base**: 186 Shell Energy FAQ documents processed with FAISS vector search
- **Custom Actions**: Canary test implementation with proper flow control
- **Environment Management**: Automated credential loading and validation
- **Web Interface**: Rasa Inspector GUI for interactive testing

## Features

- **CALM Architecture**: Hybrid approach combining LLM intelligence with deterministic control
- **Enterprise Search**: RAG-powered knowledge retrieval from Shell Energy FAQ database
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
git clone https://github.com/deesumblip/Customer_Service_Bot.git
cd Customer_Service_Bot
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
pip install rasa-pro
```

**Required Dependencies:**
- `rasa-pro>=3.1.0` - Rasa Pro with CALM architecture
- `openai>=1.0.0` - OpenAI API client for LLM integration  
- `python-dotenv>=1.0.0` - Environment variable management

**Note:** `rasa-pro` automatically installs all required dependencies including FAISS for vector search.

### 3. Configure Environment Variables

**Step 1: Create a `.env` file in the project root**
```bash
# Create the file
touch .env  # Mac/Linux
# or create manually on Windows

# Edit the file and add your credentials:
RASA_PRO_LICENSE=your_actual_license_here
OPENAI_API_KEY=your_actual_api_key_here
```

**Step 2: Get Your Credentials**

**Rasa Pro License:**
1. Visit https://rasa.com/pro/
2. Sign up for a free trial or purchase a license
3. Copy your license key to `RASA_PRO_LICENSE`

**OpenAI API Key:**
1. Visit https://platform.openai.com/api-keys
2. Create a new API key
3. Copy the key to `OPENAI_API_KEY`

**Step 3: Validate your environment setup**
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
python autoload_env.py
rasa train --force
```

**Training Process:**
- Loads environment variables automatically
- Processes 186 Shell Energy FAQ documents for knowledge base
- Creates vector embeddings using OpenAI's text-embedding-3-small
- Generates a trained model in the `models/` directory

**When to Retrain:**
- `config.yml` - CALM configuration changes
- `domain.yml` - Response definitions  
- `data/flows.yml` - Conversation flows
- `data/patterns.yml` - Global patterns
- `docs/` folder - Shell Energy FAQ knowledge base updates

**No Retraining Needed:**
- `actions.py` - Custom action code changes
- `credentials.yml` - Input channel configuration
- `endpoints.yml` - Action server configuration

### 5. Start the Assistant

**Option 1: Manual Start (Two Terminals)**

**Terminal 1 - Action Server:**
```bash
python autoload_env.py
rasa run actions --actions actions.actions --port 5055
```

**Terminal 2 - Rasa Inspector GUI:**
```bash
python autoload_env.py
rasa inspect --port 5006
```

**Option 2: Automated Start (Windows)**
```bash
.\start_bot.bat
```

**Access the Assistant:**
Open your browser to `http://localhost:5006` to chat with the assistant!

**Expected Startup:**
- Action server starts on port 5055
- Web interface launches on port 5006
- Both servers load environment variables automatically

## Testing

### Canary Test
**Purpose:** Validates the complete pipeline is working correctly.

**Test Questions:**
- "What is the canary fact?"
- "Tell me about canary"
- "Canary information please"

**Expected Response:**
```
The safe color for deployments is ultramarine kiwi.
What else can I help you with?
```

### Shell Energy Knowledge Base Questions
**Purpose:** Tests Enterprise Search Policy with Shell Energy FAQ documents.

**Test Questions:**
- "How do I find Shell station opening times?"
- "What is Shell Go?"
- "How does Pay at Pump work?"
- "What is DYNAFLEX Technology?"
- "How do I activate my Shell Go rewards?"
- "What is Shell Recharge?"
- "How do I get Shell Energy customer discounts?"

**Expected Response:**
- Detailed answer from Shell Energy FAQ knowledge base
- Follow-up: "What else can I help you with?"

### Edge Case Testing
**Greeting:** "Hello" → Welcome message + help suggestions
**Chitchat:** "Thank you" → Friendly response
**Unknown Topics:** "What is Tesla?" → Enterprise Search fallback

## Project Structure

```
Customer_Service_Bot/
├── .gitignore            # Git ignore rules
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
├── docs/               # Shell Energy FAQ knowledge base
│   ├── 115002743932-How-can-I-find-the-opening-times-of-Shell-Service-Stations-.txt
│   ├── 115002772032-Where-can-I-find-the-nearest-Shell-Service-Station-and-the-services-it-offers-.txt
│   ├── 115002985931-How-does-oil-protect-my-engine-.txt
│   ├── 115005981965-How-does-Pay-at-Pump-work-at-a-Shell-Station-.txt
│   ├── 360000747418-Can-I-still-register-for-Shell-Drivers-Club-.txt
│   └── ... (186 Shell Energy FAQ files total)
└── models/             # Trained model files (auto-generated, gitignored)
```

## Architecture

This project demonstrates Rasa's CALM architecture:

- **SearchReadyLLMCommandGenerator**: Converts user input to structured commands
- **FlowPolicy**: Manages deterministic conversation flows
- **EnterpriseSearchPolicy**: Handles RAG-powered knowledge retrieval
- **Patterns**: Global, interruptible conversation handlers

## Troubleshooting

### Environment Validation
Always start troubleshooting by validating your environment:
```bash
python autoload_env.py
```

This will show you:
- Whether your `.env` file exists and is loaded
- Which environment variables are set vs. missing
- Helpful guidance for getting missing credentials

### Common Issues

**"rasa command not found"**
- Ensure your virtual environment is activated
- Verify `rasa-pro` is installed: `pip list | grep rasa`
- Try: `python -m rasa train` instead of `rasa train`

**"Incorrect API key provided" (401 error)**
- Check your `.env` file has the correct `OPENAI_API_KEY`
- Verify the key is valid at https://platform.openai.com/api-keys
- Restart the Rasa server after updating credentials

**"You exceeded your current quota" (429 error)**
- Check your OpenAI usage at https://platform.openai.com/usage
- Add credits to your OpenAI account
- Test with the canary question (doesn't use OpenAI)

**Model training fails**
- Ensure environment variables are loaded: `python autoload_env.py`
- Try training with debug: `python autoload_env.py && rasa train --debug`
- Check for encoding issues in `docs/` files

**Port Conflicts**
- Action server: `rasa run actions --port 5056`
- Web interface: `rasa inspect --port 5007`

**"Failed to execute custom action"**
- Ensure action server is running: `rasa run actions`
- Check `endpoints.yml` configuration
- Verify `actions.py` syntax is correct

### Debug Commands
```bash
# Validate environment
python autoload_env.py

# Train with debug output
python autoload_env.py && rasa train --debug

# Test specific functionality
python test_latest_model.py
```

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

**GitHub**: https://github.com/deesumblip/Customer_Service_Bot

This repository contains a production-ready CALM implementation with comprehensive documentation, making it an excellent resource for learning Rasa's CALM architecture and building enterprise-grade conversational AI systems.
