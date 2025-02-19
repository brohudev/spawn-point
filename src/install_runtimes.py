# install_runtimes.py
import subprocess

def install_nodejs():
    """Install Node.js 18 and npm"""
    try:
        subprocess.run(['curl', '-fsSL', 'https://rpm.nodesource.com/setup_18.x', '-o', '/tmp/nodesource_setup.sh'], check=True)
        subprocess.run(['sudo', 'bash', '/tmp/nodesource_setup.sh'], check=True)
        subprocess.run(['sudo', 'dnf', 'install', '-y', 'nodejs'], check=True)
        print("✅ Node.js 18 and npm installed")
    except subprocess.CalledProcessError as e:
        print(f"🚨 Error installing Node.js: {e}")