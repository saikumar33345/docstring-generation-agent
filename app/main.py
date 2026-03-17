import re
import os
import time
from fastapi import FastAPI, Request, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.models import DocstringRequest, DocstringResponse
from app.agents import run_docstring_agent

app = FastAPI(title="Docstring Generation Agent")

templates = Jinja2Templates(directory="templates")


# ✅ UI ROUTE
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/about")
def about():
    return {"message": "Docstring Generation Agent using Gemini"}


# 🔥 GET ALL PY FILES
def get_python_files(path):
    if os.path.isfile(path) and path.endswith(".py"):
        return [path]

    python_files = []

    for root, _, files in os.walk(path):
        for file in files:
            if file.endswith(".py") and not file.startswith("__"):
                python_files.append(os.path.join(root, file))

    return python_files


# 🔥 MAIN ENDPOINT
@app.post("/generate-docstrings", response_model=DocstringResponse)
def generate_docstrings(payload: DocstringRequest):

    file_path = payload.file_path

    if not file_path or file_path.strip().lower() == "string":
        file_path = None

    # 🔥 support natural language
    if not file_path and payload.message:
        match = re.search(r'([A-Za-z0-9_:\\/.\-]+\.py)', payload.message)
        if match:
            file_path = match.group(1).replace("\\", "/")

    if not file_path:
        return DocstringResponse(
            files_processed=0,
            results={"error": "No valid Python file or folder detected."}
        )

    files = get_python_files(file_path)

    if not files:
        return DocstringResponse(
            files_processed=0,
            results={"error": "No Python files found."}
        )

    results = {}

    for file in files:
        try:
            result = run_docstring_agent(file)

            # 🔥 API error handling
            if "API key" in result or "INVALID_ARGUMENT" in result:
                return DocstringResponse(
                    files_processed=0,
                    results={"error": "API key invalid or expired. Please update your API key."}
                )

            output_path = file.replace(".py", "_doc.py")

            with open(output_path, "w", encoding="utf-8") as f:
                f.write(result)

            clean_path = output_path.replace("\\", "/")

            # 🔥 show preview in UI
            preview = result[:300] + "..." if len(result) > 300 else result
            results[clean_path] = preview

            time.sleep(5)

        except Exception as e:
            clean_path = file.replace("\\", "/")
            results[clean_path] = f"Error: {str(e)}"

    return DocstringResponse(
        files_processed=len(results),
        results=results
    )


# 🔥 FILE UPLOAD ENDPOINT
@app.post("/upload-docstrings")
async def upload_docstrings(file: UploadFile = File(...)):
    try:
        content = await file.read()

        temp_path = f"temp_{file.filename}"

        with open(temp_path, "wb") as f:
            f.write(content)

        result = run_docstring_agent(temp_path)

        os.remove(temp_path)

        preview = result[:500] + "..." if len(result) > 500 else result

        return {
            "filename": file.filename,
            "result": preview
        }

    except Exception as e:
        return {"error": str(e)}