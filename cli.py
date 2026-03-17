import sys
import os
import time
from app.agents import run_docstring_agent


MAX_FILES_PER_RUN = 3


def get_python_files(path):
    if os.path.isfile(path) and path.endswith(".py"):
        return [path]

    python_files = []

    for root, _, files in os.walk(path):
        for file in files:
            if file.endswith(".py") and not file.startswith("__"):
                python_files.append(os.path.join(root, file))

    return python_files


def process_files(path):
    files = get_python_files(path)

    if not files:
        print("❌ No Python files found.")
        return

    print(f"📁 Found {len(files)} Python files")


    files = files[:MAX_FILES_PER_RUN]
    print(f"⚠️ Processing only first {len(files)} files due to API limits\n")

    for file in files:
        retry_count = 0

        while retry_count < 3:
            try:
                print(f"⚙️ Processing: {file}")

                result = run_docstring_agent(file)

                
                if "RESOURCE_EXHAUSTED" in result:
                    print("⏳ Rate limit hit. Waiting 30 seconds...")
                    time.sleep(30)
                    retry_count += 1
                    continue

                if "API key" in result or "INVALID_ARGUMENT" in result:
                    print("❌ API Key issue. Fix your key.")
                    return

                output_path = file.replace(".py", "_doc.py")

                with open(output_path, "w", encoding="utf-8") as f:
                    f.write(result)

                print(f"✅ Saved: {output_path}\n")

                time.sleep(6)
                break

            except Exception as e:
                print(f"❌ Error: {str(e)}")
                retry_count += 1

        if retry_count == 3:
            print(f"❌ Skipped after retries: {file}\n")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python cli.py <file_or_folder>")
        sys.exit(1)

    input_path = sys.argv[1]

    if not os.path.exists(input_path):
        print("❌ Path does not exist.")
        sys.exit(1)

    process_files(input_path)