#!/usr/bin/env python3
import sys

def main():
    if not sys.stdin.isatty():
        print("Running in piped mode... bootstrapping...")
        # Add your bootstrap logic here
    else:
        print("Error: Please run this script using 'curl -sSL <URL> | python3 starter.py'")

if __name__ == '__main__':
    main()