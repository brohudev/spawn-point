# install_frontend.py
import subprocess
from pathlib import Path

def install_frontend_stack():
    """Install Next.js, Tailwind, and shadcn/ui"""
    try:
        Path("package.json").touch()
        subprocess.run(['npm', 'install', 'next@latest', 'react@latest', 'react-dom@latest'], check=True)
        subprocess.run(['npm', 'install', '-D', 'tailwindcss@latest', 'postcss@latest', 'autoprefixer@latest'], check=True)
        subprocess.run(['npx', 'tailwindcss', 'init', '-p'], check=True)
        subprocess.run(['npm', 'install', 'class-variance-authority', 'clsx', 'tailwind-merge'], check=True)
        print("✅ Frontend stack installed")
    except subprocess.CalledProcessError as e:
        print(f"🚨 Frontend installation error: {e}")
