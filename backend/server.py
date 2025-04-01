from asgiref.wsgi import WsgiToAsgi
from app.app import app  # Import your application factory

#! DO NOT GET RID OF THIS FILE ITS IMPORTANT FOR THE SERVER TO RUN

# Create the Flask instance
flask_app = app()

# Wrap the Flask WSGI app to ASGI
asgi_app = WsgiToAsgi(flask_app)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server:asgi_app", host="0.0.0.0", port=8000, reload=True)

