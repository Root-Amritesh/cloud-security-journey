
#!/usr/bin/env python3

import os

for root, dirs, files in os.walk("."):

    print(f"\nCurrent Folder: {root}")

    print("Directories:", dirs)

    print("Files:", files)
