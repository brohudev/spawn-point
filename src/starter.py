#!/usr/bin/env python3
import argparse
from install_runtimes import install_nodejs
from install_frontend import install_frontend_stack
from config import BASE_CONFIG

def main():
    parser = argparse.ArgumentParser(description='Fedora Dev Environment Setup')
    parser.add_argument('--all', action='store_true', help='Install full stack')
    parser.add_argument('--frontend', action='store_true', help='Install frontend stack')
    
    args = parser.parse_args()

    if args.all or args.frontend:
        print(f"🚀 Setting up {BASE_CONFIG['framework']} environment")
        
        if args.all:
            install_nodejs()
            
        install_frontend_stack()

        if args.all:
            print("\n🔧 Remaining setup steps:")
            print("- [ ] Configure PostgreSQL database")
            print("- [ ] Initialize Prisma ORM")
            print("- [ ] Set up tRPC routers")
            print("- [ ] Configure Auth.js providers")
            
        print("\n✅ Setup complete! Run 'npm run dev' to start")
    else:
        print("Please specify installation target:\n"
              "  --all    Full stack setup\n"
              "  --frontend Frontend only")

if __name__ == "__main__":
    main()