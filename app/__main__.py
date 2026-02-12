from fastapi import FastAPI
from app.models import DocstringRequest, DocstringResponse
from app.agents import run_docstring_agent

app = FastAPI(title="Docstring Generation Agent")

@app.get("/about")
def about():
    return {"message": "Docstring Generation Agent using Gemini"}

@app.post("/generate-docstrings", response_model=DocstringResponse)
def generate_docstrings(payload: DocstringRequest):
    updated_code = run_docstring_agent(payload.file_path)
    return DocstringResponse(updated_code=updated_code)
