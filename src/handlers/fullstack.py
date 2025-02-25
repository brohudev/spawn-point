from utils import validate_os

# todo: turn this into an actual function (and seperate out the os verification to a seperate utility down the line)
def handle_fullstack():
    return """#!/usr/bin/env python
print("Initializing fullstack environment...")
print("│ 1. cheking for Node.js 20.x")
print("│ 2. Setting up Python 3.12 virtualenv")
print("│ 3. Configuring PostgreSQL container")
print("└── ✔️ Done! Run 'make dev' to start")
"""