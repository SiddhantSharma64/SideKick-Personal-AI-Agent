# SideKick: Your Personal AI Agent

**SideKick** is an AI agent that helps you with various tasks using a chat interface. It can browse the web, run code, and access information.

---

## ✨ Features

- **Interactive Chat**: Easy-to-use interface built with Gradio.
- **Task Automation**: Define tasks and success criteria.
- **Web & Code**: Uses Playwright for web browsing and a Python REPL for code execution.
- **Information Access**: Integrates with Wikipedia and Google Serper for search.
- **Extensible**: Easily add new tools.
- **Memory**: Maintains conversation history.

---

## ⚙️ How it Works

SideKick is built with the following components:

- **Gradio (`app.py`)** – User interface
- **LangGraph (`sidekick.py`)** – Core AI logic and task orchestration
- **LangChain Tools (`sidekick_tools.py`)** – Actions like web browsing, code execution, search
- **OpenAI GPT Models** – Uses `gpt-4o-mini` for processing and reasoning

---

## 🚀 Get Started

### ✅ Prerequisites

- Python 3.9+
- OpenAI API Key
- *(Optional)* Google Serper API Key, Pushover API Token/User Key

---

### 📦 Installation

```bash
git clone https://github.com/SiddhantSharma64/SideKick-Personal-AI-Agent.git
cd SideKick-Personal-AI-Agent
pip install -r requirements.txt
