 Docstring Generation Agent
Epoch AI/ML Club × Nasiko Hackathon Submission
 Problem Statement

Build an AI Agent that:

Reads Python source code

Automatically generates clear and meaningful docstrings for:

Functions

Classes

Methods

>Selected Challenge

This submission implements the Docstring Generation Agent.

The agent analyzes Python files and generates concise, professional, Google-style docstrings while preserving original code logic and structure.

-> Solution Overview

The system is built using:

FastAPI – API interface

LangChain – Agent orchestration

Google Gemini API – LLM for docstring generation

Tool-based file reading approach

->Agent Design
Architecture Structure
project_root/
│
├── app/
│   ├── __main__.py        → FastAPI entry point
│   ├── config.py          → API key configuration
│   ├── models.py          → Request/response schemas
│   ├── tools.py           → File-reading tool
│   ├── agents.py          → LangChain agent logic
│
├── README.md

Execution Flow

1.User sends a Python file path via API.

2.File is read locally.

3.If file is empty → handled without model invocation.

4.Otherwise, LangChain agent invokes Gemini.

5.Gemini generates structured docstrings.

6.Output is cleaned to remove markdown artifacts.

7.Executable Python code is returned.

 API Usage
Endpoint

POST /generate-docstrings

Request Body
{
  "file_path": "sample.py"
}

Response
{
  "updated_code": "Python code with generated docstrings"
}


 Goal Satisfaction

The agent correctly:

Generates docstrings for:

Functions

Classes

Instance methods

Static methods

Class methods

Nested functions

Adds module-level docstring if no functions/classes exist

Preserves original code logic

Returns executable Python code

Prompt & Coding Style

Modular file structure

Clear separation of concerns

Strict prompt constraints:

No logic modification

No markdown output

Concise professional formatting

Post-processing ensures clean output

⚠ Edge Case Handling

The system explicitly handles:

✅ Empty files (no model call)

✅ Files with no functions/classes

✅ Nested functions

✅ Mixed scripts (functions + module code)

✅ Private methods

✅ Static & class methods

Quota errors and file-not-found cases are safely handled.

 Assumptions

Input file is valid Python code

File path is accessible

LLM is responsible for docstring generation


⚠ Limitations

Very large files may exceed model context limits

Free-tier API usage may have quota restrictions

No AST-level structural validation (LLM-based generation approach)


Future Improvements

AST-based deterministic docstring insertion

Chunking support for large files

Folder-level batch processing

Syntax validation before returning output
