import platform, os

def verify_platform():
     if platform.system() != 'Linux':
          raise Exception(platform.system())
          
     with open('/etc/os-release') as f:
          os_info = {k:v.strip('"') for k,v in (line.strip().split('=', 1) for line in f if '=' in line)}

     if os_info.get('ID') != 'fedora' or int(os_info.get('VERSION_ID', 0)) < 41:
          raise Exception(f"Fedora {os_info.get('VERSION_ID', '')}".strip())

     return True
