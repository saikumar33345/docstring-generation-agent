import re
from fastapi import FastAPI
from app.models import DocstringRequest, DocstringResponse
from app.agents import run_docstring_agent

app = FastAPI(title="Docstring Generation Agent")


@app.get("/about")
def about():
    return {"message": "Docstring Generation Agent using Gemini"}


@app.post("/generate-docstrings", response_model=DocstringResponse)
def generate_docstrings(payload: DocstringRequest):

    file_path = payload.file_path

    if not file_path or file_path.strip().lower() == "string":
        file_path = None

    
    if not file_path and payload.message:
        match = re.search(r'([A-Za-z0-9_:\\/.\-]+\.py)', payload.message)
        if match:
            file_path = match.group(1).replace("\\", "/")

    if not file_path:
        return DocstringResponse(
            updated_code="Error: No valid Python file detected in request."
        )

    updated_code = run_docstring_agent(file_path)

    return DocstringResponse(updated_code=updated_code)
