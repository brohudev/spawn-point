import sys


def verify_platform(expected_platform):
    """
    Verify the current system matches the expected platform.
    
    Args:
        expected_platform (str): The expected platform (e.g., 'linux', 'win32', 'darwin')
        
    Returns:
        bool: True if running on the expected platform, False otherwise
    """
    if sys.platform != expected_platform:
        print(f"Warning: This script was generated for {expected_platform} but is being run on {sys.platform}.")
        return False
    return True
