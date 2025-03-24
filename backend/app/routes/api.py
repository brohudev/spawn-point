from flask import Blueprint, jsonify, request
from flask import Response
from backend.app.utils.generate import generate_script
from app.utils.validators import validate_os, validate_project_type

bp = Blueprint('api', __name__, url_prefix='')

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
def generate_project(os, project_type):
     """Generate script for specific OS and project type."""
     
     valid, error = validate_os(os) 
     if not valid:
          return jsonify(error), 400

     valid, error = validate_project_type(project_type)
     if not valid:
          return jsonify(error), 400

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