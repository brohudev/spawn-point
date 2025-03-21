from app.app import app

if __name__ == "__main__":
    # Create application instance
    application = app()
    
    # Run the app in debug mode
    # Debug=True enables auto-reloading when code changes
    # Host 0.0.0.0 makes the server accessible from other devices on the network
    application.run(
        debug=True,
        host="0.0.0.0", 
        port=5000
    )
