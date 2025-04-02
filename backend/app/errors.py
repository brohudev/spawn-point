def register_handlers(app):
    """Register error handlers for the Flask app."""
    
    @app.errorhandler(404)
    def not_found(e):
        return f'print("Error: Not found - {str(e)}")', 404
    
    @app.errorhandler(400)
    def bad_request(e):
        return f'print("Error: Bad request - {str(e)}")', 400
    
    @app.errorhandler(500)
    def server_error(e):
        return f'print("Error: Server error - {str(e)}")', 500
    
    @app.errorhandler(Exception)
    def handle_exception(e):
        # Log the error here
        app.logger.error(f"Unhandled exception: {str(e)}")
        return 'print("Error: Internal server error - An unexpected error occurred")', 500
