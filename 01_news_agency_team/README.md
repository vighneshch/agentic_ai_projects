# 🧠 NYT-Worthy Article Generator using Agno Agents

A multi-agent AI system built with the [Agno SDK](https://github.com/agno-agi/agno) that collaboratively researches, writes, and edits long-form, high-quality articles — tailored to meet the standards of *The New York Times*.

---

## 📌 Overview

This project uses the Agno agent orchestration framework to simulate a newsroom team:

- **WebSearchAgent**: Conducts smart searches and finds credible sources.
- **ContentWriterAgent**: Reads URLs and crafts a full-length editorial article.
- **EditorAgent**: Coordinates agents and ensures the final article is publication-ready.

All interaction is powered by **Groq LLMs** and can be accessed via the built-in **Playground UI**.

---

## 🚀 Features

- ✅ Multi-agent collaboration with Agno
- ✅ Live web search using DuckDuckGo
- ✅ Article scraping using Newspaper4k
- ✅ Long-form writing with Groq's Gemma and LLaMA models
- ✅ Interactive agent Playground for testing and exploration

---

## 🔧 Installation

### 1. Clone the repository

```bash
git clone https://github.com/vighneshch/agentic_ai_projects/tree/main/01_news_agency_team
cd 01_news_agency_team
```

### 2. Create a virtual environment (optional but recommended)

```bash
python -m venv venv
```
#### For macOS/Linus
```bash
source venv/bin/activate  # Activates the virtual environment
```
#### For Windows
```bash
venv\Scripts\activate  # Activates the virtual environment
```
You should now see (venv) at the beginning of your terminal prompt, indicating that the virtual environment is active.

### 3. Install all dependancies
Install all required dependencies using the following command:
```bash
pip install -r requirements.txt
```
### 4. Set up Environment Variables
Create a .env file in the project directory and add your Groq API Key:
```bash
GROQ_API_KEY=your_groq_api_key_here
```
### 5. Start the playground app
To run the app and interact with the agents
```bash
python playground.py
```

## 📁 Project Structure
```bash
01_news_agency_team/
├── playground.py         # Main logic: agent and team setup
├── .env                  # Your environment variables (API key)
├── requirements.txt      # List of Python dependencies
└── README.md             # You are here


