"""function to detect package manager on Linux and validate the OS is correct"""
def validate_linux() -> str:
    """Returns Linux validation code as a string"""
    return r'''#!/usr/bin/env python
import platform
import os
import sys

def detect_pkg_base():
    """Detect Linux package manager family"""
    if platform.system() != "Linux":
        raise RuntimeError("This script requires Linux")

    # NixOS detection
    if os.path.exists("/etc/nixos/configuration.nix"):
        return "nix"

    # Package manager fallback checks
    pm_checks = [
        ("pacman-aur", "/usr/bin/pacman"),
        ("apt-deb-snap", "/usr/bin/apt"),
        ("yum-dnf", "/usr/bin/dnf"),
        ("yum-dnf", "/usr/bin/yum")
    ]

    for name, path in pm_checks:
        if os.path.exists(path):
            return name

    # os-release parsing for distros without package managers in standard locations
    os_release = {}
    try:
        with open("/etc/os-release") as f:
            for line in f:
                key, _, value = line.strip().partition('=')
                if key and value:
                    os_release[key] = value.strip('"')
    except FileNotFoundError:
        pass

    distro_id = os_release.get("ID", "").lower()
    id_like = os_release.get("ID_LIKE", "").lower().split()

    if 'arch' in [distro_id] + id_like:
        return "pacman-aur"
    if 'debian' in [distro_id] + id_like or 'ubuntu' in [distro_id] + id_like:
        return "apt-deb-snap"
    if any(d in ['fedora', 'rhel', 'centos'] for d in [distro_id] + id_like):
        return "yum-dnf"

    raise RuntimeError("Could not determine package manager family")
'''

