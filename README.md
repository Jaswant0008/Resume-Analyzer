# 📄 Resume Analyzer & JD Matcher

A sleek, AI-powered web application that parses PDF resumes and matches them against a job description (JD) to evaluate candidate fit. Built using **Streamlit**, **LangChain**, and **Groq (Llama-3.3-70b-versatile)**.

---

## 🚀 Key Features

*   **Structured PDF Parsing**: Extracts key details from resumes, including candidate information (name, email, phone number), education history (universities, degrees, GPAs), experience details (companies, duration, project names, descriptions, tech stacks), and core skills.
*   **Job Description Matching**: Evaluates candidate fit against a provided job description text.
*   **Detailed Fit Assessment**:
    *   Generates an overall **Match Score** (0-100).
    *   Lists **Matched Skills** vs. **Missing Skills**.
    *   Highlights **Key Strengths** and **Experience Gaps**.
    *   Provides a structured **Text Summary** assessment of the candidate.
*   **Interactive Web UI**: A clean dashboard built with Streamlit.
*   **Raw Data View**: Inspect the extracted candidate data in clean raw JSON.

---

## 🛠️ Tech Stack

*   **Backend**: Python, LangChain, Pydantic
*   **Frontend UI**: Streamlit
*   **PDF Loader**: PyPDF
*   **LLM Engine**: Groq Cloud APIs (utilizing `llama-3.3-70b-versatile`)

---

## ⚙️ Setup & Installation

### Prerequisites

Make sure you have Python 3.10+ installed and a Groq API Key. You can get one from the [Groq Console](https://console.groq.com/).

### 1. Clone the Repository
```bash
git clone https://github.com/Jaswant0008/Resume-Analyzer.git
cd Resume-Analyzer
```

### 2. Set Up a Virtual Environment (Recommended)
```bash
python -m venv .venv
# On Windows (cmd/Powershell):
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirments.txt
```

### 4. Configure Environment Variables
Create a file named `.env` in the root directory and add your Groq API key:
```env
GROQ_API_KEY=your_groq_api_key_here
```

---

## 🖥️ Running the Application

To run the Streamlit app:
```bash
streamlit run main.py
```

Open your browser and navigate to `http://localhost:8501` to start analyzing resumes!

---

## 📂 Project Structure

```text
├── main.py          # Streamlit UI & Application Entry Point
├── parser.py        # Logic for parsing PDFs and extracting structured JSON with LLM
├── matcher.py       # Logic for comparing parsed resumes against job descriptions
├── models.py        # Pydantic data schemas (Resume, Education, Experience, JDMatchResult)
├── prompts.py       # Prompt templates for extraction and matching
├── requirments.txt  # Python package dependencies
└── .gitignore       # Git ignore rules (excluding .env, .venv, etc.)
```
