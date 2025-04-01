import sys


def verify_platform(expected_platform):
    if sys.platform != expected_platform:
        print(f"Warning: This script was generated for {expected_platform} but is being run on {sys.platform}.")
        return False
    return True
