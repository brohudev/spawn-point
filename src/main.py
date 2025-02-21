from fastapi import FastAPI, Query
from fastapi.responses import PlainTextResponse

app = FastAPI()

SCRIPTS = {
    "fullstack": """#!/bin/bash
set -e
echo "Setting up Fullstack Environment..."
apt update && apt install -y nodejs npm python3
echo "Fullstack setup complete."
""",
    "devops": """#!/bin/bash
set -e
echo "Setting up DevOps Environment..."
apt update && apt install -y docker.io ansible
echo "DevOps setup complete."
""",
    "ml": """#!/bin/bash
set -e
echo "Setting up Machine Learning Environment..."
apt update && apt install -y python3-pip
pip3 install torch numpy pandas
echo "ML setup complete."
"""
}

@app.get("/", response_class=PlainTextResponse)
def generate_script(type: str = Query("default")):
    return SCRIPTS.get(type, "#!/bin/bash\necho 'Invalid project type specified.'")