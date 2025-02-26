"""function to detect package manager on Linux and validate the OS is correct"""
def validate_linux() -> str:
    """Returns Python code string to execute on target machine"""
    return r'''#!/usr/bin/env python
import platform
import os
import sys

def detect_pkg_base():
    # First check if we're even on Linux
    if platform.system() != "Linux":
        raise RuntimeError("This script requires Linux. \n Please querry the correct endpoint for your OS.")

    # Check for NixOS first
    if os.path.exists("/etc/nixos/configuration.nix"):
        return "nix"

    # Parse os-release file
    os_release = {}
    try:
        with open("/etc/os-release") as f:
            for line in f:
                line = line.strip()
                if line and '=' in line:
                    key, value = line.split('=', 1)
                    os_release[key] = value.strip('"')
    except FileNotFoundError:
        pass

    # Get distro IDs
    distro_id = os_release.get("ID", "").lower()
    id_like = os_release.get("ID_LIKE", "").lower().split()

    # Arch-based detection
    if distro_id == "arch" or "arch" in id_like:
        return "pacman-aur"
    
    # Debian/Ubuntu family
    if "debian" in id_like or "ubuntu" in id_like or distro_id in ["debian", "ubuntu"]:
        return "apt-deb-snap"
    
    # RHEL family detection
    if any(d in ["fedora", "rhel", "centos"] for d in [distro_id] + id_like):
        return "yum-dnf"

    # Fallback to package manager check
    if os.path.exists("/usr/bin/pacman"):
        return "pacman-aur"
    if os.path.exists("/usr/bin/apt-get"):
        return "apt-deb-snap"
    if os.path.exists("/usr/bin/dnf") or os.path.exists("/usr/bin/yum"):
        return "yum-dnf"

    raise RuntimeError(f"Unsupported Linux distribution: {distro_id}")

if __name__ == "__main__":
    try:
        print(detect_pkg_base())
    except RuntimeError as e:
        sys.stderr.write(f"ERROR: {str(e)}\n")
        sys.exit(1)
'''
