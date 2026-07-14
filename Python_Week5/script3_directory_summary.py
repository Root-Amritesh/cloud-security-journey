#!/usr/bin/env python3
"""Script 3: Directory Summary."""

import os


def summarize_directory(dirpath):

    print("\nDirectory Summary")
    print("=" * 75)
    print(f"{'Filename':20} {'Size':>10} {'Lines':>10}")
    print("-" * 75)

    total_files = 0

    for current_dir, dirnames, filenames in os.walk(dirpath):

        for name in filenames:

            full_path = os.path.join(current_dir, name)

            size = os.path.getsize(full_path)

            with open(full_path) as f:
                line_count = sum(1 for _ in f)

            print(f"{name:20} {size:>8} bytes {line_count:>8}")

            total_files += 1

    print("-" * 75)
    print(f"Total Files: {total_files}")


if __name__ == "__main__":

    directory = input("Enter directory path: ").strip()

    if os.path.isdir(directory):
        summarize_directory(directory)
    else:
        print("Directory not found!")
