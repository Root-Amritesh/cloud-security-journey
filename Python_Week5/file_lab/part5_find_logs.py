#!/usr/bin/env python3

import os

for root, dirs, files in os.walk("."):

    for file in files:

        if file.endswith(".log"):

            full_path = os.path.join(root, file)

            print(f"\nReading: {full_path}")

            with open(full_path) as f:

                for line in f:
                    print(line.strip())
