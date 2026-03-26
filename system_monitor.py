import os
import socket
import platform
from datetime import datetime
import getpass

print("---- SYSTEM INFO ----")

# Date & Time
now = datetime.now()
print("Date & Time:", now.strftime("%Y-%m-%d %H:%M:%S"))

# Hostname
print("Hostname:", socket.gethostname())

# Python Version
print("Python Version:", platform.python_version())

# Current User
print("Current User:", getpass.getuser())

# Files
files = os.listdir(".")
print("\nFiles in Directory:")
for f in files:
    print("-", f)

# Count files
print("\nTotal Files:", len(files))

# User input
name = input("\nEnter your name: ")
print("Hello,", name)
