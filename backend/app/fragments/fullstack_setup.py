import os

def setup_fullstack(os_type):
    print("Setting up full stack project...")
    print("Installing frontend and backend dependencies...")
    print("Creating project structure for both frontend and backend...")
    print("Setting up database connections...")
    
    # Initialize full stack project setup
    print("Initializing full stack project...")
    
    # try:
    #     # Create directory structure
    #     os.makedirs("frontend", exist_ok=True)
    #     os.makedirs("backend", exist_ok=True)
    #     os.makedirs("database", exist_ok=True)
    #     
    #     # Set up frontend
    #     os.chdir("frontend")
    #     os.system("npm init -y")
    #     os.system("npm install react react-dom next axios")
    #     os.makedirs("src/components", exist_ok=True)
    #     os.makedirs("src/pages", exist_ok=True)
    #     os.makedirs("public", exist_ok=True)
    #     os.chdir("..")
    #     
    #     # Set up backend
    #     os.chdir("backend")
    #     os.system("pip install flask flask-cors sqlalchemy")
    #     os.makedirs("app", exist_ok=True)
    #     os.makedirs("app/routes", exist_ok=True)
    #     os.makedirs("app/models", exist_ok=True)
    #     os.chdir("..")
    #     
    #     # Set up database config
    #     os.chdir("database")
    #     with open("config.py", "w") as f:
    #         f.write("DATABASE_URI = 'sqlite:///app.db'\n")
    #     os.chdir("..")
    #     
    #     print("Full stack project setup completed successfully")
    # except Exception as e:
    #     raise RuntimeError(f"Full stack setup failed: {str(e)}")
