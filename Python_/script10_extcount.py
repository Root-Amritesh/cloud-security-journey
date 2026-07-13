#!/usr/bin/env python3
"""Script 10: Count files by extension."""

import os


def count_by_extension(filenames):
    counts = {}

    for name in filenames:

        _, ext = os.path.splitext(name)

        if ext == "":
            ext = "(no extension)"

        counts[ext] = counts.get(ext, 0) + 1

    return counts


if __name__ == "__main__":

    print("=" * 55)
    print("File Extension Counter")
    print("=" * 55)

    raw = input(
        "\nEnter filenames separated by commas:\n> "
    )

    files = [f.strip() for f in raw.split(",")]

    counts = count_by_extension(files)

    print("\nExtension Counts")

    for ext, count in sorted(
        counts.items(),
        key=lambda pair: pair[1],
        reverse=True
    ):
        print(f"{ext:15} {count}")
