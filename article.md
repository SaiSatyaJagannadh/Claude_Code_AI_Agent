# Understanding the Local AI Agent File

## Overview

The `local_ai_agent.py` file demonstrates how to build a simple AI agent using LangChain that can interact with tools to perform tasks. This agent uses OpenAI's language model and includes a custom tool for listing directory contents.

## Key Components

### 1. **Imports and Environment Setup**

```python
import os
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
```

The file imports:
- **os**: For directory operations
- **dotenv**: To load environment variables from a `.env` file (likely containing API keys)
- **LangChain modules**: Tools for creating agents and initializing chat models

### 2. **LLM Initialization**

```python
llm = init_chat_model(
    "gpt-5-mini",
    model_provider='openai',
    temperature=0.5
)
```

Sets up the language model with:
- **Model**: GPT-5-mini (OpenAI's model)
- **Provider**: OpenAI
- **Temperature**: 0.5 (controls randomness; 0.5 is balanced between deterministic and creative responses)

### 3. **Custom Tool: `list_directory()`**

```python
def list_directory(path: str=".") -> str:
    """List all files and folders in the given directory path. Default is current directory."""
```

This is a custom tool that:
- Takes a directory path as input (defaults to current directory)
- Separates files and folders
- Returns a formatted string with:
  - **Folders section**: Lists all subdirectories
  - **Files section**: Lists all files

The function scans the directory and organizes items into two categories for better readability.

### 4. **Agent Creation**

```python
agent = create_agent(
    model=llm,
    tools=[list_directory]
)
```

Creates an AI agent that:
- Uses the initialized LLM model
- Has access to the `list_directory` tool
- Can decide when and how to use the tool

### 5. **Agent Execution and Streaming**

```python
user_input = "Give me the list of files in the dir"
messages = [{"role":"user", "content":user_input}]
chunks = list(agent.stream({"messages": messages}, stream_mode='updates'))
```

The execution flow:
- Defines a user request: "Give me the list of files in the dir"
- Streams the agent's response in real-time using `stream_mode='updates'`
- Collects response chunks as they arrive

### 6. **Processing Tool Calls**

```python
for chunk in chunks:
    for step, data in chunk.items():
        if step == 'model':
            msg = data['messages'][-1]
            print("MSG toOL CALL", msg.tool_calls)
            if msg.tool_calls:
                tool = msg.tool_calls[0]['name']
                message = f"🔧 Using tool: {tool}"
                print(message)
            else:
                ai_message = msg.content
        elif step == 'tools':
            result = data['messages'][-1].content
            result = result if len(result) < 50 else result[:50] + "..."
            print(f"🗒️ Tool result:\n {result}")
```

Processes the streamed response by:
- **Model Step**: When the model generates output
  - Checks if the model wants to call a tool
  - Prints the tool being used with 🔧 emoji
  - Saves the AI message if no tool call is made
- **Tools Step**: When a tool executes
  - Captures the tool result
  - Truncates long results to 50 characters for readability
  - Prints the result with 🗒️ emoji

### 7. **Final Output**

```python
print(30*"-", "\n")
print(ai_message)
```

Prints a separator line and the final AI response to the user.

## How It Works (Flow)

1. User asks: "Give me the list of files in the dir"
2. Agent receives the request and decides to use `list_directory()` tool
3. Tool executes and returns file/folder information
4. Agent processes the tool result
5. Agent generates a natural language response
6. Response is printed to the console

## Use Cases

This pattern is useful for:
- **File system exploration**: AI agents can browse directories
- **Task automation**: Building agents that can use multiple tools
- **Interactive CLI**: Creating conversational interfaces that perform actions
- **Real-time feedback**: Streaming responses as they're generated

## Key Takeaway

The `local_ai_agent.py` file demonstrates a foundational pattern for building AI agents—combining language models with tools to create intelligent systems that can interact with external systems in response to user requests.
