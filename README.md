# ⚖️ LegalMind AI

**LegalMind AI** is a Multi-Agent Legal Document Analyzer powered by **Ollama** and **Qwen2.5**. The system analyzes legal documents using multiple specialized AI agents to generate comprehensive legal insights, identify risks, check compliance, and produce professional reports.

## 🌐 Live Demo

🔗 https://legal-mind.streamlit.app/

---

## 📌 Features

* 📄 Upload and analyze legal PDF documents
* 🧠 Multi-Agent architecture
* ⚡ Parallel agent execution for faster analysis
* 📝 Automatic document summarization
* 📋 Clause extraction and analysis
* ⚠️ Legal risk assessment
* ✅ Compliance checking
* 📑 Professional legal report generation
* 📥 Download analysis reports as PDF
* 💾 Session history and memory

---

## 🏗️ System Architecture

```text
User Uploads PDF
        |
        v
PDF Reader
        |
        v
Text Cleaner
        |
        v
Legal Orchestrator
        |
        +-----------------------------+
        |             |               |
        v             v               v
SummaryAgent   ClauseAgent    RiskAgent
        |                             |
        +---------- ComplianceAgent --+
                      |
                      v
               ReportAgent
                      |
                      v
              Final Legal Report
```

---

## 🤖 Multi-Agent System

### 1. Summary Agent

Responsible for:

* Document summarization
* Identifying important parties
* Extracting obligations
* Extracting important dates

---

### 2. Clause Agent

Responsible for:

* Confidentiality clause extraction
* Termination clause extraction
* Payment terms analysis
* Liability clause identification
* Governing law extraction

---

### 3. Risk Agent

Responsible for:

* Legal risk assessment
* Identifying problematic clauses
* Assigning risk levels
* Suggesting mitigations

---

### 4. Compliance Agent

Responsible for:

* Checking mandatory clauses
* Compliance verification
* Identifying missing clauses

---

### 5. Report Agent

Responsible for:

* Combining outputs from all agents
* Generating the final professional report

---

## ⚙️ Tech Stack

### Frontend

* Streamlit

### Backend

* Python

### LLM

* Ollama
* Qwen2.5

### PDF Processing

* PyPDF

### Report Generation

* ReportLab

### Parallel Processing

* ThreadPoolExecutor

---

## 📁 Project Structure

```text
LegalMind-AI/
│
├── agents/
│   ├── summary_agent.py
│   ├── clause_agent.py
│   ├── risk_agent.py
│   ├── compliance_agent.py
│   └── report_agent.py
│
├── document_processor/
│   ├── pdf_reader.py
│   └── text_cleaner.py
│
├── app.py
├── llm.py
├── orchestrator.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/Rudra-AI-2127/LegalMind-AI.git
```

```bash
cd LegalMind-AI
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🦙 Install Ollama

Download Ollama:

https://ollama.com/download

Pull Qwen2.5 Model:

```bash
ollama pull qwen2.5:7b
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

## 🔮 Future Enhancements

* Chat with legal documents
* Contract comparison
* Long-term memory
* Vector database integration
* RAG-based retrieval
* Support for DOCX files
* Clause confidence scoring

---

## ⚠️ Disclaimer

This application is intended for **educational and informational purposes only**.

LegalMind AI does **not provide legal advice**. Always consult a qualified legal professional before making legal decisions.

---

## 👥 Team Members

| Name                           | Role                                         |
| ------------------------------ | -------------------------------------------- |
| **Rudra Pratap Singh Rathore** | AI Engineer / Multi-Agent System Development |
| **Yash Pal**                   | AI Engineer / System Development             |

---

## 📄 License

This project is licensed under the MIT License.

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
