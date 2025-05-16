#!/usr/bin/env python3
import os
import sys

# Add the project root to Python path
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

from app.main import run

if __name__ == "__main__":
    run() 