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

