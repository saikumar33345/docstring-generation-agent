import re
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from app.config import GOOGLE_API_KEY
from app.tools import read_python_file

tools = [read_python_file]

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=GOOGLE_API_KEY,
    temperature=0.2
)

agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt="""
You are a professional Python documentation assistant.

Your task:
- Add concise, high-quality docstrings to all functions, classes, and methods.
- Use clean Google-style docstring format.
- Keep descriptions clear and brief (1-2 lines maximum).
- Include Args and Returns only if applicable.
- Do NOT change any code logic.
- Do NOT add explanations outside docstrings.
- Do NOT add markdown formatting.
- Return ONLY valid, executable Python code.

If the file contains no functions or classes,
add a short module-level docstring at the top describing the script.
"""
)

def run_docstring_agent(file_path: str) -> str:
    try:
    
        with open(file_path, "r", encoding="utf-8") as f:
            raw_content = f.read()

        if not raw_content.strip():
            return '"""Empty Python file."""'

    except FileNotFoundError:
        return "Error: File not found."
    except Exception as e:
        return f"Error reading file: {str(e)}"

   
    user_message = f"""
Use the read_python_file tool to read the file at this path:
{file_path}

Then generate proper docstrings for all functions, classes, and methods.
Return ONLY the full updated Python code.
"""

    try:
        result = agent.invoke(
            {"messages": [{"role": "user", "content": user_message}]}
        )

        messages = result.get("messages", [])
        if not messages:
            return "Error: No response from agent."

        last_message = messages[-1]
        content = getattr(last_message, "content", None)

        if content is None:
            return "Error: Agent returned empty content."

        
        if isinstance(content, list):
            content = "".join(
                [c.get("text", "") for c in content if isinstance(c, dict)]
            )

        content = str(content).strip()

        
        if content.startswith("```"):
            content = re.sub(r"```[a-zA-Z]*", "", content)
            content = content.replace("```", "").strip()

       
        match = re.search(r"(def |class |\"\"\"|\'\'\')", content)
        if match:
            content = content[match.start():]

        return content

    except Exception as e:
        return f"Error while processing: {str(e)}"
