# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Commands

### Setup
```bash
pip install -r requirements.txt
```

### Running the Agent
To run the local AI agent:
```bash
python local_ai_agent.py
```

The agent will list files and directories in the current working directory using its built-in `list_directory` tool.

### Testing
There are no formal tests in this repository. To test functionality:
1. Run `python local_ai_agent.py` to see the agent in action
2. Modify the `user_input` variable in the script to test different commands
3. The agent currently only supports the `list_directory` tool

## Code Architecture

### High-Level Structure
This is a simple AI agent demonstration project with the following components:

1. **Core Agent (`local_ai_agent.py`)**:
   - Uses LangChain framework with OpenAI's GPT-5-mini model
   - Implements a single custom tool: `list_directory()` for file system exploration
   - Demonstrates agent creation, tool usage, and streaming response handling
   - Loads environment variables from `.env` file for API keys

2. **Data Files**:
   - `products.csv`: Sample product data with columns for ID, name, category, brand, price, stock quantity, rating, description, and stock date
   - `article.md`: Detailed explanation of how the AI agent works
   - `.env`: Contains API keys for OpenAI and Gemini services

3. **Dependencies** (in `requirements.txt`):
   - Core: langchain, langchain-openai, python-dotenv, openai
   - Additional: langchain-google-genai, gradio, google-genai, pillow, sounddevice, soundfile, rich

### Key Components Explained

#### LLM Initialization
The agent initializes a ChatOpenAI model with:
- Model: `gpt-5-mini` 
- Provider: OpenAI
- Temperature: 0.5 (balanced between deterministic and creative responses)

#### Custom Tool - `list_directory()`
A custom LangChain tool that:
- Takes an optional directory path parameter (defaults to current directory)
- Separates files and directories into organized lists
- Returns formatted string output showing folders and files
- Helps the agent understand the file system structure

#### Agent Workflow
1. User provides input (currently hardcoded as "Give me the list of files in the dir")
2. Agent processes input and determines if tool usage is needed
3. If needed, agent invokes `list_directory()` tool
4. Results are streamed back in real-time using `stream_mode='updates'`
5. Final response is displayed to the user

### Environment Setup
- Requires API keys in `.env` file:
  - `OPENAI_API_KEY` for OpenAI GPT-5-mini access
  - `GEMINI_API_KEY` for Gemini model access (alternative)
- Uses python-dotenv for secure environment variable loading

### Extending the Agent
To add new capabilities:
1. Create new tool functions following the `list_directory()` pattern
2. Add the new tool to the `tools` list when creating the agent
3. Update the user input/prompts to test new functionality
4. Ensure any required dependencies are added to `requirements.txt`

### File Operations
The agent can only perform read-only directory listing through its current tool. For file modification capabilities:
- Add new tools for reading/writing files
- Implement appropriate security considerations
- Update the agent's tool set accordingly

## Notes
- This is an educational demonstration project showing basic AI agent concepts
- The agent currently has limited functionality (directory listing only)
- Error handling is minimal in the demonstration code
- Environment variables should never be committed to version control