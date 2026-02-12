
from langchain.tools import tool

@tool
def read_python_file(file_path: str) -> str:
    """
    Reads a Python file and returns its content as a string.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        if not content.strip():
            return "Error: The file is empty."
        
        return content

    except FileNotFoundError:
        return "Error: File not found."
    except Exception as e:
        return f"Error: {str(e)}"

