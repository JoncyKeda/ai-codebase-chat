import zipfile
import os

def load_codebase(zip_path):
    extract_path = "data/extracted"

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)

    docs = []

    for root, _, files in os.walk(extract_path):
        for file in files:
            if file.endswith((".py", ".js", ".txt", ".md")):
                path = os.path.join(root, file)
                try:
                    with open(path, "r", encoding="utf-8") as f:
                        docs.append(f.read())
                except:
                    pass

    return docs
