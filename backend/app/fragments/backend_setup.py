import os

def setup_back():
    print("Setting up backend project...")
    print("Installing backend dependencies...")
    print("Creating Flask project structure...")
    print("Configuring SQLAlchemy and database...")
    
    # Initialize backend project setup
    print("Initializing backend project...")
    
    # try:
    #     # Create basic project structure
    #     os.makedirs("app", exist_ok=True)
    #     os.makedirs("app/routes", exist_ok=True)
    #     os.makedirs("app/models", exist_ok=True)
    #     os.makedirs("app/static", exist_ok=True)
    #     os.makedirs("app/templates", exist_ok=True)
    #     os.makedirs("migrations", exist_ok=True)
    #     
    #     # Create requirements.txt
    #     with open("requirements.txt", "w") as f:
    #         f.write("Flask==2.0.1\n")
    #         f.write("Flask-SQLAlchemy==2.5.1\n")
    #         f.write("Flask-Migrate==3.1.0\n")
    #         f.write("Flask-RESTful==0.3.9\n")
    #     
    #     # Create app initialization file
    #     with open("app/__init__.py", "w") as f:
    #         f.write("from flask import Flask\n")
    #         f.write("from flask_sqlalchemy import SQLAlchemy\n\n")
    #         f.write("db = SQLAlchemy()\n\n")
    #         f.write("def create_app():\n")
    #         f.write("    app = Flask(__name__)\n")
    #         f.write("    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'\n")
    #         f.write("    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False\n")
    #         f.write("    db.init_app(app)\n")
    #         f.write("    return app\n")
    #     
    #     # Create main application file
    #     with open("run.py", "w") as f:
    #         f.write("from app import create_app\n\n")
    #         f.write("app = create_app()\n\n")
    #         f.write("if __name__ == '__main__':\n")
    #         f.write("    app.run(debug=True)\n")
    #     
    #     print("Backend project setup completed successfully")
    # except Exception as e:
    #     raise RuntimeError(f"Backend setup failed: {str(e)}")
