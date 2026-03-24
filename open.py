#!/usr/bin/env python3
"""
ML Chronic Disease Indicator - Auto Startup (like Vite)
Run this once and everything starts automatically with browser opening
"""

import subprocess
import time
import webbrowser
import sys
import os

def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    print("\n" + "="*70)
    print("ML CHRONIC DISEASE INDICATOR - Starting...")
    print("="*70 + "\n")
    
    # Start backend
    print("[1/2] Starting Backend API...")
    backend = subprocess.Popen(
        [sys.executable, "ml-app/apps.py"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    time.sleep(2)
    
    # Start frontend
    print("[2/2] Starting Frontend Server...")
    frontend = subprocess.Popen(
        [sys.executable, "-m", "http.server", "5500"],
        cwd="frontend",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    time.sleep(2)
    
    # Open browser
    url = "http://127.0.0.1:5500/index.html"
    print("\nOpening browser...\n")
    webbrowser.open(url)
    
    # Display like Vite
    print("="*70)
    print("  LOCAL:   http://127.0.0.1:5500/index.html")
    print("="*70)
    print("\n  Backend:  http://127.0.0.1:10000")
    print("  Frontend: http://127.0.0.1:5500")
    print("\n  Press Ctrl+C to stop all servers\n")
    print("="*70 + "\n")
    
    try:
        backend.wait()
        frontend.wait()
    except KeyboardInterrupt:
        print("\n\nShutting down servers...")
        backend.terminate()
        frontend.terminate()
        backend.wait()
        frontend.wait()
        print("Servers stopped. Goodbye!\n")

if __name__ == "__main__":
    main()
