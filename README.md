<div align="center">

<!-- Typing SVG Header -->
<a href="https://github.com/Jaswant0008/Resume-Analyzer">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=28&pause=1000&color=00D9FF&center=true&vCenter=true&width=600&lines=Resume+Analyzer;LLM-Powered+Resume+%E2%86%92+JD+Matching;Built+with+LangChain+%2B+Groq;ATS+Score+%2B+Skill+Gap+Detection" alt="Typing SVG" />
</a>

<br/>

<!-- Badges -->
<p>
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white" />
  <img src="https://img.shields.io/badge/Groq-F55036?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PC9zdmc+&logoColor=white" />
  <img src="https://img.shields.io/badge/Pydantic-E92063?style=for-the-badge&logo=pydantic&logoColor=white" />
</p>

<p>
  <img src="https://img.shields.io/badge/status-active--development-brightgreen?style=flat-square" />
  <img src="https://img.shields.io/badge/license-MIT-blue?style=flat-square" />
  <img src="https://img.shields.io/badge/PRs-welcome-orange?style=flat-square" />
  <img src="https://img.shields.io/github/stars/Jaswant0008/Resume-Analyzer?style=flat-square&color=yellow" />
</p>

</div>

---

## 📖 Overview

**Resume Analyzer** is an intelligent resume evaluation system that helps job seekers and recruiters understand how well their resumes align with specific job descriptions. 

It extracts details from uploaded PDF resumes, converts them into structured data using **Large Language Models (LLMs)**, and compares them against any pasted job description to generate **ATS-style compatibility insights** — including a match score, missing skills, candidate strengths, and experience gaps.

---

## ❓ Problem Statement

Recruiters receive hundreds of resumes for a single position, while candidates struggle to know:
- Whether their resume matches the target role.
- What critical skills are missing from their profile.
- How ATS systems or automated parsers will read their details.

**Resume Analyzer automates this evaluation process and provides clear, structured, and actionable feedback.**

---

## 🎯 Objectives

- 📄 Extract structured information from resumes (Info, Education, Experience).
- 🧩 Identify candidate skills and technologies.
- 🔍 Compare resumes directly against job descriptions.
- 📊 Calculate ATS-style compatibility scores.
- ❌ Detect missing skills and experience gaps.
- 💡 Generate professional assessment summaries.

---

## 🏗️ System Architecture

```text
PDF Resume
     │
     ▼
PDF Text Extraction (PyPDF)
     │
     ▼
Resume Parsing Engine (Structured Output LLM)
     │
     ▼
Structured Resume Object (Pydantic Model)
     │
     ├────────► Resume Details (UI Preview / Raw JSON)
     │
     ▼
Job Description Matcher (structured Output LLM)
     │
     ▼
ATS Evaluation Engine
     │
     ▼
Analysis Report (Match Score, Gaps, Strengths)
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| 🖥️ Frontend | Streamlit |
| ⚙️ Backend | Python |
| 🧠 LLM Framework | LangChain |
| ⚡ LLM Provider | Groq |
| 🤖 Model | Llama 3.3 70B Versatile |
| ✅ Data Validation | Pydantic |
| 📑 PDF Processing | PyPDF |
| 🔐 Configuration | python-dotenv |

---

## 📂 Project Structure

```text
resume-analyzer/
│
├── main.py          # Streamlit UI & Application Entry Point
├── parser.py        # logic for parsing PDFs and extracting structured JSON with LLM
├── matcher.py       # Logic for comparing parsed resumes against job descriptions
├── models.py        # Pydantic data schemas (Resume, Education, Experience, JDMatchResult)
├── prompts.py       # Prompt templates for extraction and matching
├── requirments.txt  # Python package dependencies
├── .env.example     # Reference file for environment configuration
└── .gitignore       # Git ignore rules (excluding secrets and temp files)
```

---

## 🧩 Module Breakdown

*   **`models.py`**: Defines the data hierarchy (Education, Experience, Resume, and JDMatchResult) using Pydantic for validation and structured LLM outputs.
*   **`parser.py`**: Loads raw PDF text with PyPDF and utilizes LangChain's `.with_structured_output` to parse it into the Pydantic `Resume` schema.
*   **`matcher.py`**: Uses the parsed resume JSON data and compares it to a job description text using `jd_match_prompt` to generate the structured `JDMatchResult`.
*   **`main.py`**: Manages user upload states, displays parsed info side-by-side, inputs job descriptions, and renders beautiful ATS match metrics.

---

## ⚙️ Setup & Installation

### Prerequisites

Ensure you have Python 3.10+ installed and a Groq API Key from the [Groq Console](https://console.groq.com/).

### 1. Clone the Repository
```bash
git clone https://github.com/Jaswant0008/Resume-Analyzer.git
cd Resume-Analyzer
```

### 2. Set Up Virtual Environment
```bash
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirments.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the root directory:
```env
GROQ_API_KEY=your_groq_api_key_here
```

### 5. Run the Application
```bash
streamlit run main.py
```
