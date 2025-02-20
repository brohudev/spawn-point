import platform, os
try:
    if platform.system() != 'Linux':
        raise Exception(f"{platform.system()}")
    with open('/etc/os-release') as f:
        os_info = {k:v.strip('"') for k,v in (line.strip().split('=') for line in f if '=' in line)}
    if os_info.get('ID') == 'fedora' and int(os_info.get('VERSION_ID',0)) >= 41:
        print("im working")
    else:
        raise Exception(f"Fedora {os_info.get('VERSION_ID','<unknown>')}")
except Exception as e:
    print(f"{str(e)} is not supported, please check back later or open a pr with support for your distro at github.com/brohudev/spawn-point")
