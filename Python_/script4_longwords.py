#!/usr/bin/env python3
"""Script 4: Find all words longer than 8 characters in a file."""

def find_long_words(filepath, min_length=8):
    long_words = []

    with open(filepath) as f:
        for line in f:
            for word in line.split():
                cleaned = word.strip(".,!?;:\"'()")

                if len(cleaned) > min_length:
                    long_words.append(cleaned)

    return long_words


if __name__ == "__main__":
    path = "sample.txt"

    for word in find_long_words(path):
        print(word)
