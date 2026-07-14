#!/usr/bin/env python3
"""Script 4: Keyword Filter."""

import os


def filter_by_keyword(source_path, keyword, output_path):
    """Copy every matching line into a new file."""

    matches = []

    # Read the source file
    with open(source_path) as f:

        for line in f:

            if keyword in line:
                matches.append(line)

    # Write matches into a new file
    with open(output_path, "w") as f:

        f.writelines(matches)

    return len(matches)


if __name__ == "__main__":

    source = input("Source log file: ").strip()
    keyword = input("Keyword to search: ").strip()
    output = input("Output file name: ").strip()

    if not os.path.exists(source):
        print("Source file not found!")

    else:

        total = filter_by_keyword(source, keyword, output)

        print(f"\n{total} matching line(s) written to '{output}'")
