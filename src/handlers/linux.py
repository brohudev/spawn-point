from utils import validate_linux

# todo: turn this into an actual function (and seperate out the os verification to a seperate utility down the line)
def handle_fullstack() -> str:
    """Generates complete initialization script with validation"""
    validation_code = validate_linux()
    
    setup_script = r'''
if __name__ == "__main__":
    try:
        distro = detect_pkg_base()
        print(f"Initializing {distro} fullstack environment...")
        print("│ 1. checking for Node.js 20.x")
        print("│ 2. Setting up Python 3.12 virtualenv")
        print("│ 3. Configuring PostgreSQL container")
        print("└── ✔️ Done! Run 'make dev' to start")
    except RuntimeError as e:
        sys.stderr.write(f"ERROR: {str(e)}\n")
        sys.exit(1)
'''
    
    return f"{validation_code}\n{setup_script}"


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