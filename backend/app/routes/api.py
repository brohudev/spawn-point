from flask import Blueprint, jsonify, request
from flask import Response
from app.utils.generate import generate_script

bp = Blueprint('api', __name__, url_prefix='')

@bp.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint."""
    return jsonify({
        "status": "healthy",
        "version": "1.0.0",
        "service": "spawnpoint-api"
    })

# the money shot
@bp.route('/<os>/<project_type>', methods=['GET'])
def generate_project(os, project_type):
     """Generate script for specific OS and project type."""

     ci = request.args.get('ci', 'none')
     deploy = request.args.get('deploy', 'none')
     
     try: # generate script
         script_content = generate_script(os, project_type, ci, deploy) 
         return Response(script_content, mimetype='text/plain')
     except Exception as e:
          print("script generation error:",e)
          
          error_message = str(e).replace("'", "\\'")
          return f"print({{'error': 'Script generation failed', 'message': '{error_message}'}})", 500
