#!/usr/bin/env python3
"""
Script 1 — Error Line Filter

Print every line in a log file that contains ERROR.
"""

import os


def print_error_lines(filepath):
    """Print every line containing the word ERROR."""

    with open(filepath, "r") as f:

        for line in f:

            if "ERROR" in line:
                print(line.strip())


if __name__ == "__main__":

    path = input("Enter log file path: ").strip()

    if os.path.exists(path):

        print("\nLines containing ERROR")
        print("-" * 40)

        print_error_lines(path)

    else:
        print("File not found!")
