import tkinter as tk
import os

# Print the current working directory
print(f"Keylog file will be created in: {os.getcwd()}")

# Defining the log file
log_file = "keylog.txt"

# Function to handle key press events
def on_key(event):
    with open(log_file, "a") as f:
        f.write(f"{event.char}")

# Setting up the main application window
root = tk.Tk()
root.bind_all("<Key>", on_key)

# Keep the application running
root.mainloop()
