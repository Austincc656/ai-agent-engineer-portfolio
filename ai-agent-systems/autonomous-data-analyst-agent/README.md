# Autonomous Data Analyst Agent

An AI-powered data analyst agent that converts natural language business questions into SQL queries, executes them against a structured database, and returns a formatted analytical report.

This project demonstrates tool-augmented LLM agents, structured reasoning, and API deployment using FastAPI.

---

## 🚀 Overview

This agent allows users to ask business questions such as:

> "Show total revenue by region"

The system:
1. Retrieves the database schema
2. Generates SQL using an LLM-style reasoning flow
3. Executes the query safely
4. Formats results into a structured report
5. Returns a human-readable analytical summary

---

## 🏗 Architecture

User Question  
→ LLM generates SQL  
→ SQL execution tool  
→ Result formatting tool  
→ Insight generation  
→ Structured report output  

The agent follows a tool-based reasoning design similar to ReAct-style agents.

---

## 🛠 Tech Stack

- Python
- FastAPI (API deployment)
- SQLite (database)
- Pydantic (data validation)
- Tool-augmented agent architecture
- Modular project structure
- Pytest (smoke testing)

---

## 📂 Project Structure

