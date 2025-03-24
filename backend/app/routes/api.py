from flask import Blueprint, jsonify, request
from flask import Response
from fragments.generate import generate_script

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint."""
    return jsonify({
        "status": "healthy",
        "version": "1.0.0",
        "service": "spawnpoint-api"
    })


# OS-specific project type endpoints
@bp.route('/<os>/<project_type>', methods=['GET'])
def generate_os_project(os, project_type):
     """Generate script for specific OS and project type."""
     # Validate OS
     valid_os = ['lin', 'wind', 'mac']
     if os not in valid_os:
          return jsonify({
               "error": "Invalid OS",
               "message": f"OS must be one of: {', '.join(valid_os)}"
          }), 400

     valid_types = ['front', 'back', 'full']
     if project_type not in valid_types:
          return jsonify({
               "error": "Invalid project type",
               "message": f"Project type must be one of: {', '.join(valid_types)}"
          }), 400

     ci = request.args.get('ci', 'none')
     deploy = request.args.get('deploy', 'none')
     
     try:
         script_content = generate_script(os, project_type, ci, deploy)
         return Response(script_content, mimetype='text/plain')
     except Exception as e:
          print("script generation error:",e)
          
          return jsonify({
             "error": "Script generation failed",
             "message": str(e)
          }), 500