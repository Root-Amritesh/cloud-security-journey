#!/usr/bin/env python3
"""Script 9: Parse a colon-separated record."""

def parse_record(line):
    fields = line.strip().split(":")

    return {
        "username": fields[0],
        "uid": fields[2],
        "home": fields[5],
        "shell": fields[6]
    }


if __name__ == "__main__":

    print("=" * 55)
    print("Colon-Separated Record Parser")
    print("=" * 55)

    print("\nExample Record:")
    print("payload:x:1000:1000:Payload User:/home/payload:/bin/bash")

    line = input("\nEnter a colon-separated record:\n> ")

    record = parse_record(line)

    print("\nParsed Record:")
    for key, value in record.items():
        print(f"{key:<10}: {value}")
