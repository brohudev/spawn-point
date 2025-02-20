#!/bin/bash
OUTPUT="deploy.py"

cat << EOF > $OUTPUT
import sys, argparse

EOF

cat platform_check.py >> $OUTPUT
cat handlers/*.py >> $OUTPUT

cat << EOF >> $OUTPUT

STACKS = {
    '--frontend': lambda: generic_handler('frontend'),
    '--backend': lambda: generic_handler('backend'),
    '--aiml': lambda: generic_handler('aiml'),
    '--web3': lambda: generic_handler('web3'),
    '--devops': lambda: generic_handler('devops'),
    '--embedded': lambda: generic_handler('embedded'),
    '--cybersec': lambda: generic_handler('cybersec'),
    '--gamedev': lambda: generic_handler('gamedev'),
    '--fullstack': handle_fullstack
}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('flags', nargs='*')
    args = parser.parse_args()
    
    if not args.flags:
        print("Usage: python - <flag>")
        return
    
    for flag in args.flags:
        if handler := STACKS.get(flag):
            handler()
        else:
            print(f"Unknown stack: {flag}")

if __name__ == "__main__":
    try:
        verify_platform()
        main()
    except Exception as e:
        print(f"{e} is not supported...")
EOF

echo "Bundled into $OUTPUT"
