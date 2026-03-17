# AI Docstring Generation Agent

An AI-powered backend tool that automatically generates clean, professional Google-style docstrings for Python code.

Supports single-file processing, folder-level processing, REST API, Web UI, and CLI usage.

---

## Features

- Automatic docstring generation for:
  - Functions
  - Classes
  - Instance methods
  - Static methods
  - Class methods
  - Nested functions
- Multi-file (folder-level) processing
- Google-style structured docstrings
- REST API using FastAPI
- Web-based user interface
- CLI tool for local usage
- Handles edge cases such as empty files and invalid paths

---

## Tech Stack

- Backend: FastAPI
- LLM Integration: LangChain + Google Gemini API
- Language: Python
- Frontend: HTML, CSS, JavaScript
- Deployment: Render

---

## Project Structure
docstring-generation-agent/
│
├── app/
│ ├── main.py
│ ├── agents.py
│ ├── tools.py
│ ├── models.py
│ └── config.py
│
├── templates/
│ └── index.html
│
├── cli.py
├── requirements.txt
└── README.md

---

## Setup Instructions

### 1. Clone the repository
git clone https://github.com/saikumar33345/docstring-generation-agent.git

cd docstring-generation-agent

---

### 2. Create virtual environment
python -m venv venv
venv\Scripts\activate # Windows
### 3. Install dependencies
pip install -r requirements.txt
### 4. Configure API Key

Create a `.env` file in the root directory:
GOOGLE_API_KEY=your_api_key_here
---

## Running the Application

### Start the API server
---

## Running the Application

### Start the API server
uvicorn app.main:app --reload
Open in browser:http://127.0.0.1:8000

---

## Web Interface

- Enter a file or folder path
- Click "Generate Docstrings"
- View generated results in the UI

---

## CLI Usage
python cli.py app/

---

## API Usage

### Endpoint

### Request Example
{
"file_path": "app"
}

---

## Limitations

- Free-tier Gemini API has strict rate limits
- File changes may not persist on deployed environments
- Large files may exceed model context limits

---

## Future Improvements

- AST-based docstring generation
- Batch processing queue system
- File upload support in UI
- Improved error handling and retries
- Authentication and user management

---

## Author

Sai Kumar  
ECE – IIIT Sri City  

GitHub: https://github.com/saikumar33345