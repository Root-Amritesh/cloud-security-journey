#!/usr/bin/env python3
"""Script 2: Word Counter."""

import os


def count_words(filepath):
    """Read a file and count every word."""

    counts = {}

    with open(filepath) as f:

        for line in f:

            for word in line.split():

                word = word.strip(".,!?;:()[]{}\"'")

                if not word:
                    continue

                counts[word] = counts.get(word, 0) + 1

    return counts


def print_counts(counts):

    print("\nWord Frequency")
    print("-" * 35)

    for word, count in sorted(
        counts.items(),
        key=lambda pair: pair[1],
        reverse=True
    ):
        print(f"{word:<15} {count}")


if __name__ == "__main__":

    path = input("Enter file path: ").strip()

    if os.path.exists(path):

        counts = count_words(path)

        print_counts(counts)

    else:
        print("File not found!")
