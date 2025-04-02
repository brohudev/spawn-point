def verify_platform(os):
    valid_os = ['lin', 'wind', 'mac']
    if os not in valid_os:
        return False, f"print(\"error: Invalid OS. Please make sure your {os} is one of: {', '.join(valid_os)}\")"
    return True, None
