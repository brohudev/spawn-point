from flask import jsonify

def register_handlers(app):
    """Register error handlers for the Flask app."""
    
    @app.errorhandler(404)
    def not_found(e):
        return jsonify({"error": "Not found", "message": str(e)}), 404
    
    @app.errorhandler(400)
    def bad_request(e):
        return jsonify({"error": "Bad request", "message": str(e)}), 400
    
    @app.errorhandler(500)
    def server_error(e):
        return jsonify({"error": "Server error", "message": str(e)}), 500
    
    @app.errorhandler(Exception)
    def handle_exception(e):
        # Log the error here
        app.logger.error(f"Unhandled exception: {str(e)}")
        return jsonify({
            "error": "Internal server error",
            "message": "An unexpected error occurred"
        }), 500