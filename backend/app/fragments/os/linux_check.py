# Linux system verification
def verify_linux():
    """Verify the current system is Linux."""
    if sys.platform != 'linux':
        print("Warning: This script was generated for Linux but is being run on a different OS.")
        return False
    return True
