import platform, os

def verify_platform():
    if platform.system() != 'Linux':
        raise SystemExit(f"{platform.system()} is not supported...")
    
    with open('/etc/os-release') as f:
        os_info = {k:v.strip('"') for k,v in (line.strip().split('=', 1) for line in f if '=' in line)}
    
    if os_info.get('ID') != 'fedora' or int(os_info.get('VERSION_ID', 0)) < 41:
        raise SystemExit(f"Fedora {os_info.get('VERSION_ID', '')} is not supported...")
    
    return True
