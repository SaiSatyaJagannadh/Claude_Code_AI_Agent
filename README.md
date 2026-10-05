<div align="center">

# 🤖 Local AI Agent — LangChain Tools + Flask UI

### A minimal, readable tool-calling agent you can run from the terminal or the browser.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-create__agent-1C3C3C?style=flat-square&logo=langchain&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-gpt--5--mini-412991?style=flat-square&logo=openai&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white)
![Rich](https://img.shields.io/badge/Rich-terminal_UI-FAD000?style=flat-square)
![Claude Code](https://img.shields.io/badge/Built_with-Claude_Code-D97757?style=flat-square)

</div>

---

## ✨ What it is

A small agent built with LangChain's `create_agent`, wired to a custom **`list_directory`** tool. Ask it about your files in plain English; it decides when to call the tool and answers with the result — rendered as Markdown in a Rich terminal panel, or in a simple Flask web page.

It's intentionally tiny so every moving part is visible: model init → tool definition → agent loop → output. A line-by-line walkthrough lives in [`article.md`](article.md).

```
 you ──► Flask form / CLI ──► LangChain agent (gpt-5-mini) ──► list_directory tool
                                        ▲                              │
                                        └──────── tool result ◄────────┘
```

## 🚀 Run it

```bash
git clone https://github.com/SaiSatyaJagannadh/Claude_Code_AI_Agent.git && cd Claude_Code_AI_Agent
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt langchain langchain-openai python-dotenv rich
echo "OPENAI_API_KEY=sk-..." > .env

python local_ai_agent.py    # terminal agent
python app.py               # web UI → http://127.0.0.1:5000
```

## 📁 Files

| File | Purpose |
|---|---|
| `local_ai_agent.py` | Agent, tool, and `run_agent()` entry point |
| `app.py` + `templates/index.html` | Flask front end |
| `article.md` | Explainer of how the agent works |
| `CLAUDE.md`, `.claude/` | Claude Code project config used to build it |

---

<div align="center">

**Built by [Sai Satya Jagannadh Doddipatla (DJ)](https://saisatyajagannadh.github.io/PersonalPortfolio/)** · ⭐ Star the repo if it helped

</div>
