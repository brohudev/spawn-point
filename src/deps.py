# deps.py
import subprocess

def fedora_install():
    subprocess.run([
        "sudo", "dnf", "install", 
        "git", "docker", "nodejs"
    ], check=True)
    
def python_versions():
    # Your version pinning logic here
     pass