from flask import Flask
from flask_cors import CORS

def app(test_config=None):
    """Application factory for the Spawnpoint API."""
    app = Flask(__name__, instance_relative_config=True)
    
    # Configure CORS to allow requests from frontend
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    
    # Register error handlers
    from . import errors
    errors.register_handlers(app)
    
    # Register API routes
    from .routes import api
    app.register_blueprint(api.bp)
    
    # Simple health check route at the root
    @app.route('/')
    def index():
        return {
            "status": "online",
            "message": "Spawnpoint API is running"
        }
    
    return app
