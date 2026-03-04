AI Docstring Generation Agent

AI-powered agent that automatically generates clean, professional Google-style docstrings for Python source code.

This project was developed as part of the Epoch AI/ML Club × Nasiko Hackathon.

The agent reads Python files, analyzes the structure, and generates meaningful documentation for functions, classes, and methods while preserving the original code logic.

---

Problem Statement

Writing documentation for code is essential but often overlooked. Developers frequently delay writing docstrings, which reduces code readability and maintainability.

This project builds an AI Agent that automatically generates high-quality docstrings for Python codebases.

The system analyzes source code and inserts concise documentation in Google docstring format.

---

Key Features

- Automatic docstring generation for:
  - Functions
  - Classes
  - Instance methods
  - Static methods
  - Class methods
  - Nested functions
- Module-level documentation when no functions/classes exist
- Preserves original code logic
- Returns executable Python code
- Handles edge cases such as empty files
- Clean and modular backend architecture

---

Tech Stack

- FastAPI – API backend
- LangChain – Agent orchestration
- Google Gemini API – LLM for code understanding
- Python – Core implementation

---

Project Architecture

project_root/
│
├── app/
│   ├── main.py          # FastAPI entry point
│   ├── config.py        # API key configuration
│   ├── models.py        # Request / response schemas
│   ├── tools.py         # File-reading utility
│   ├── agents.py        # LangChain agent logic
│
├── README.md

The architecture separates responsibilities clearly between API handling, agent logic, and utilities.

---

Execution Flow

1. User sends a Python file path via API request.
2. The system reads the file locally.
3. If the file is empty, it returns a safe response without invoking the model.
4. Otherwise, the LangChain agent invokes the Gemini LLM.
5. The model generates structured docstrings.
6. Post-processing removes markdown artifacts.
7. Clean executable Python code is returned.

---

API Usage

Endpoint

POST "/generate-docstrings"

Request

{
  "file_path": "sample.py"
}

Response

{
  "updated_code": "Python code with generated docstrings"
}

---

Edge Case Handling

The system explicitly handles several edge cases:

- Empty files (no model invocation)
- Files without functions or classes
- Nested functions
- Mixed scripts containing both functions and module-level code
- Static methods and class methods
- Private methods
- File-not-found scenarios
- API quota errors

---

Assumptions

- Input file contains valid Python code
- File path is accessible locally
- LLM is responsible for docstring generation

---

Limitations

- Very large files may exceed model context limits
- Free-tier API usage may face quota restrictions
- No AST-based structural validation (LLM-driven generation approach)

---

Future Improvements

- AST-based deterministic docstring insertion
- Support for large file chunking
- Folder-level batch processing
- CLI interface for command-line usage
- Syntax validation before returning output

---

Author

Saikumar
ECE – IIIT Sri City

GitHub: https://github.com/saikumar33345
