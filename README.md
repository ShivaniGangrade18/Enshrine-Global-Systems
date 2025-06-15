# Multi-Agent AI System

A modular multi-agent system that accepts user goals and coordinates between intelligent agents to fulfill complex tasks through planning, enrichment, and decision-making.

---

## 💡 Features

- 🌐 Uses user goals to dynamically plan a sequence of agents
- 🔗 Agents collaborate by enriching each other's output
- 📚 Summarizes live Bitcoin-related news from the internet
- 🔁 Agents can loop if needed until the goal is fulfilled
- 🔍 Clean modular architecture for easy extensibility

---

## ⚙️ Agents & Roles

- **Planner Agent**: Understands user goals and routes them to the required agents
- **News Agent**: Pulls latest articles using [NewsAPI](https://newsapi.org/)
- **Summary Agent**: Uses NLP to summarize fetched articles

---

## ✅ Requirements Fulfilled

- ✅ Multi-agent chaining & result handoff
- ✅ Planner decides task flow dynamically
- ✅ Agents depend on each other's outputs
- ✅ Uses 2+ public APIs
- ✅ Performs iterative refinement if needed
- ✅ Clean and modular codebase
- ✅ Easy to evaluate individual agent logic and outputs

---
## 📦 Installation

##📚  Libraries Used

requests:-To make HTTP requests to external APIs (e.g., NewsAPI)
newspaper3k:-To extract article text from URLs and perform basic natural language processing
lxml_html_clean:-Required for HTML sanitization by newspaper3k after version changes in lxml
lxml:-Dependency used internally by newspaper3k for HTML/XML parsing

##Dependencies used 
pip install requests newspaper3k lxml_html_clean
