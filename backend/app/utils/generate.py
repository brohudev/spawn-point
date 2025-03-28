import os

def _load_fragment(fragment_type, name):
     """Load a fragment file if it exists, return empty string if not."""
     # Calculate the fragments directory path relative to this file
     fragments_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'fragments')
     fragment_path = os.path.join(fragments_dir, fragment_type, f"{name}.py")
     try:
          if os.path.exists(fragment_path):
               with open(fragment_path, 'r') as f:
                    return f.read()
          return f"# {name} fragment not found\nprint(\"Fragment {name} not found\")\n"
     except Exception as e:
          print(f"Error loading fragment {name}: {str(e)}")
          return f"# Error loading {name} fragment\nprint(\"Error loading fragment {name}\")\n"

def _generate_header(os_full, proj_type, ci_option, deploy_option):
     """Generate the script header with metadata."""
     header = "#!/usr/bin/env python3\n"
     header += f"# Generated by Spawnpoint for {os_full}/{proj_type}\n"
     header += f"# CI: {ci_option}, Deploy: {deploy_option}\n\n"
     return header

def _generate_imports():
     """Generate the import statements for the script."""
     return "import os\nimport sys\nimport argparse\n\n"

def _generate_os_verification(os_full):
     """Generate the OS verification section."""
     return _load_fragment('os', f"{os_full}_check")

def _generate_project_setup(proj_type):
     """Generate the project setup section."""
     return "    # Project setup\n" + _load_fragment('project', f"{proj_type}_setup")

def _generate_ci_setup(ci_option):
     """Generate the CI setup section if needed."""
     if ci_option == 'none':
          return ""
     return "\n    # CI setup\n" + _load_fragment('ci', f"{ci_option}_setup")

def _generate_deploy_setup(deploy_option):
     """Generate the deployment setup section if needed."""
     if deploy_option == 'none':
          return ""
     return "\n    # Deployment setup\n" + _load_fragment('deploy', f"{deploy_option}_setup")

def _generate_main_function(os_full, proj_type):
     """Generate the main function definition."""
     main_func = "\ndef main():\n"
     main_func += f"    print(\"Setting up {proj_type}end project for {os_full}\")\n"
     
     # Add OS verification call
     if os_full == 'linux':
          main_func += "    verify_linux()\n\n"
     elif os_full == 'macos':
          main_func += "    verify_macos()\n\n"
     elif os_full == 'windows':
          main_func += "    verify_windows()\n\n"
     
     return main_func

def _generate_entrypoint(ci_option, deploy_option):
     """Generate the script entrypoint."""
     entrypoint = "\nif __name__ == \"__main__\":\n"
     entrypoint += "    parser = argparse.ArgumentParser(description='Project setup script')\n"
     entrypoint += f"    parser.add_argument('--ci', default='{ci_option}', help='CI option')\n"
     entrypoint += f"    parser.add_argument('--deploy', default='{deploy_option}', help='Deployment option')\n"
     entrypoint += "    args = parser.parse_args()\n"
     entrypoint += "    main()\n"
     return entrypoint

def generate_script(os_type, proj_type, ci_option, deploy_option):
     """Generate a Python script based on the provided parameters."""
     
     # Map abbreviated OS to full name
     os_map = {
          'lin': 'linux',
          'mac': 'macos',
          'wind': 'windows'
     }
     
     os_full = os_map.get(os_type, 'linux')
     
     # Assemble the script from components
     script = _generate_header(os_full, proj_type, ci_option, deploy_option)
     script += _generate_imports()
     script += _generate_os_verification(os_full)
     script += _generate_main_function(os_full, proj_type)
     
     # Add the main setup sections with proper indentation
     project_setup = _generate_project_setup(proj_type)
     script += project_setup.replace('\n', '\n    ')
     
     ci_setup = _generate_ci_setup(ci_option)
     if ci_setup:
          script += ci_setup.replace('\n', '\n    ')
     
     deploy_setup = _generate_deploy_setup(deploy_option)
     if deploy_setup:
          script += deploy_setup.replace('\n', '\n    ')
     
     script += "\n    print(\"Setup complete!\")\n"
     script += _generate_entrypoint(ci_option, deploy_option)
     
     return script
