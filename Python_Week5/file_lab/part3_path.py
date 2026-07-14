#!/usr/bin/env python3
"""Part 3: Using os.path.join() and os.path.getsize()."""

import os

# Folder name
folder = "logs"

# File inside the folder
filename = "auth.log"

# Build the full path safely
full_path = os.path.join(folder, filename)

print(f"Full Path : {full_path}")

# Check if the file exists
if os.path.exists(full_path):

    print("File exists: Yes")

    # Get the size of the file
    size = os.path.getsize(full_path)
    print(f"File Size : {size} bytes\n")

    # Open and read the file
    with open(full_path) as f:
        print("File Contents")
        print("-" * 30)

        for line in f:
            print(line.strip())

else:
    print("File does not exist!")
