import subprocess
import time
import webbrowser
import sys

print("=" * 60)
print("Starting ML Chronic Disease Indicator Project")
print("=" * 60)

# Start backend
print("\n[1/2] Starting Backend API on port 10000...")
backend_process = subprocess.Popen(
    [sys.executable, "ml-app/apps.py"],
    cwd=".",
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
)

# Start frontend
print("[2/2] Starting Frontend Server on port 5500...")
frontend_process = subprocess.Popen(
    [sys.executable, "-m", "http.server", "5500"],
    cwd="./frontend",
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
)

# Wait for servers to start
time.sleep(3)

# Open browser
url = "http://127.0.0.1:5500/index.html"
print("\n" + "=" * 60)
print("[OK] Both servers are running!")
print("=" * 60)
print(f"\n[OPENING BROWSER] {url}\n")
webbrowser.open(url)

print("=" * 60)
print("Backend API: http://127.0.0.1:10000")
print("Frontend:    http://127.0.0.1:5500")
print("=" * 60)
print("\nPress Ctrl+C to stop all servers.")
print("=" * 60 + "\n")

try:
    backend_process.wait()
    frontend_process.wait()
except KeyboardInterrupt:
    print("\n\nShutting down servers...")
    backend_process.terminate()
    frontend_process.terminate()
    backend_process.wait()
    frontend_process.wait()
    print("[OK] All servers stopped.")
