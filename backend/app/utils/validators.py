"""
Validation utilities for the API endpoints.
"""

def validate_os(os):
    """
    Validate operating system parameter.
    
    Returns:
        tuple: (is_valid, error_response)
    """
    valid_os = ['lin', 'wind', 'mac']
    if os not in valid_os:
        return False, {
            "error": "Invalid OS",
            "message": f"OS must be one of: {', '.join(valid_os)}"
        }
    return True, None

def validate_project_type(project_type):
    """
    Validate project type parameter.
    
    Returns:
        tuple: (is_valid, error_response)
    """
    valid_types = ['front', 'back', 'full', "micro"]
    if project_type not in valid_types:
        return False, f"print(\"error: Invalid project type. Valid types are: {', '.join(valid_types)}\")"
    return True, None
