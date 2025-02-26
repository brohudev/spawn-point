
#!this is boilerplate code for the macos handler and wont work. 
from utils import validate_linux

# todo: turn this into an actual function (and seperate out the os verification to a seperate utility down the line)
def handle_fullstack():
    # Validate OS before proceeding
    distro = validate_linux()
    
    return f"""#!/usr/bin/env python
print("Initializing {distro} fullstack environment...")
print("│ 1. checking for Node.js 20.x")
print("└── ✔️ Done! Run 'make dev' to start")
"""

# todo: turn this into an actual function (and seperate out the os verification to a seperate utility down the line)
def handle_frontend():
    # Validate OS before proceeding
    distro = validate_linux()
    
    return f"""#!/usr/bin/env python
print("Initializing {distro} frontend environment...")
print("│ 1. checking for brahhhh")
print("└── ✔️ Done! Run 'make dev' to start")
"""

# todo: turn this into an actual function (and seperate out the os verification to a seperate utility down the line)
def handle_backend():
    # Validate OS before proceeding
    distro = validate_linux()
    
    return f"""#!/usr/bin/env python
print("Initializing {distro} backend environment...")
print("│ 1. checking for Node.js 20.x")
print("└── ✔️ Done! Run 'make dev' to start")
"""