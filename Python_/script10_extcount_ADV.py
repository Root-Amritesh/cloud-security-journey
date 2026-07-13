#!/usr/bin/env python3
"""Script 10: Count files by extension."""

import os


def count_by_extension(filenames):
    """Count how many files belong to each extension."""

    counts = {}

    for name in filenames:

        name = name.strip()

        if not name:
            continue

        _, ext = os.path.splitext(name)

        if not ext:
            ext = "(no extension)"

        counts[ext] = counts.get(ext, 0) + 1

    return counts


def print_results(counts):

    print("\nExtension Counts")
    print("-" * 35)

    for ext, count in sorted(
        counts.items(),
        key=lambda item: item[1],
        reverse=True
    ):
        print(f"{ext:<20} {count}")


def scan_directory(path):
    """Return every file inside a directory and all its subdirectories."""

    filenames = []

    for root, dirs, files in os.walk(path):
        for file in files:
            filenames.append(file)

    return filenames


if __name__ == "__main__":

    print("=" * 60)
    print("File Extension Counter")
    print("=" * 60)

    print("""
Choose an option

1. Read filenames from a text file
2. Enter filenames manually
3. Scan an entire directory
""")

    choice = input("Choice (1/2/3): ").strip()

    # --------------------------------------------------------
    # OPTION 1
    # --------------------------------------------------------

    if choice == "1":

        path = input("Enter text file path: ").strip()

        try:

            with open(path) as f:
                filenames = f.readlines()

            counts = count_by_extension(filenames)

            print_results(counts)

        except FileNotFoundError:
            print("\nFile not found!")

    # --------------------------------------------------------
    # OPTION 2
    # --------------------------------------------------------

    elif choice == "2":

        raw = input(
            "\nEnter filenames separated by commas:\n> "
        )

        filenames = raw.split(",")

        counts = count_by_extension(filenames)

        print_results(counts)

    # --------------------------------------------------------
    # OPTION 3
    # --------------------------------------------------------

    elif choice == "3":

        path = input("Enter directory path: ").strip()

        if not os.path.exists(path):
            print("\nDirectory does not exist!")

        elif not os.path.isdir(path):
            print("\nThat path is not a directory!")

        else:

            filenames = scan_directory(path)

            print(f"\nFound {len(filenames)} files.\n")

            if filenames:

                print("Files Found")
                print("-" * 35)

                for file in filenames:
                    print(file)

                counts = count_by_extension(filenames)

                print_results(counts)

            else:
                print("Directory contains no files.")

    # --------------------------------------------------------
    # INVALID OPTION
    # --------------------------------------------------------

    else:
        print("\nInvalid option.")
