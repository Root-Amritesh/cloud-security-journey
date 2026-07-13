#!/usr/bin/env python3
"""Script 6: Caesar cipher - string manipulation."""

def caesar_shift(text, shift):
    result = []

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26 + base
            result.append(chr(shifted))
        else:
            result.append(char)

    return "".join(result)


if __name__ == "__main__":
    message = input("Enter your message: ")

    shift = int(input("Enter shift value: "))

    encoded = caesar_shift(message, shift)
    decoded = caesar_shift(encoded, -shift)

    print("\n----- Results -----")
    print(f"Original : {message}")
    print(f"Encoded  : {encoded}")
    print(f"Decoded  : {decoded}")
