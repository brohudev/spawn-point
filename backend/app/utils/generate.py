import os
from ._generate_helpers import (
    _generate_header,
    _generate_imports,
    _generate_os_verification,
    _generate_main_function,
    _generate_entrypoint,
    _generate_script_sections
)

def generate_script(os_type, proj_type, ci_option, deploy_option):
     """Generate a Python script based on the provided parameters."""
     
     os_map = { # the url shortnames arent that useful as filenames
          'lin': 'linux',
          'mac': 'macos',
          'wind': 'windows'
     }
     
     proj_map = { # see why i have an os map
          'front': 'frontend',
          'full': 'fullstack',
          'back': 'backend',
          'micro': 'microservice'
     }
     
     os_full = os_map.get(os_type, 'linux')
     proj_full = proj_map.get(proj_type, proj_type)  # Use original if not in map
     
     # Generate script sections and fragment details
     script_sections, fragment_content, fragment_path = _generate_script_sections(
          os_full, proj_full, ci_option, deploy_option
     )
     
     # Assemble the script from components
     script = _generate_header(os_full, proj_full, ci_option, deploy_option)
     script += _generate_imports()
     script += _generate_os_verification(os_full)
     script += fragment_content
     script += _generate_main_function(os_full, proj_full, fragment_path)
     script += script_sections
     script += "\n    print(\"Setup complete!\")\n"
     script += _generate_entrypoint(ci_option, deploy_option)
     
     return script
