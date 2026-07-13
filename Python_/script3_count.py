#!/usr/bin/env python3
"""Script 3: Read a file, count lines and words."""

def count_lines_and_words(filepath):
    with open(filepath) as f:
        lines = f.readlines()
    line_count = len(lines)
    word_count = sum(len(line.split()) for line in lines)
    return line_count, word_count

if __name__ == "__main__":
    path = "sample.txt"
    lines, words = count_lines_and_words(path)
    print(f"{path}: {lines} lines, {words} words")
