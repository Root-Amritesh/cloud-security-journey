#!/usr/bin/env python3
"""
Script 5 / Gate 2: Log Parser

Walk through a directory, scan every .log file,
count FAILED and ERROR lines,
save the results into results.json.
"""

import os
import json


def parse_logs(dirpath):
    """Parse every .log file and count FAILED / ERROR lines."""

    summary = {}

    for current_dir, dirnames, filenames in os.walk(dirpath):

        for name in filenames:

            # Ignore non-log files
            if not name.endswith(".log"):
                continue

            full_path = os.path.join(current_dir, name)

            flagged = 0

            with open(full_path) as f:

                for line in f:

                    if "FAILED" in line or "ERROR" in line:
                        flagged += 1

            summary[name] = flagged

    return summary


if __name__ == "__main__":

    directory = input("Enter directory to scan: ").strip()

    if not os.path.isdir(directory):
        print("Directory not found!")
        exit()

    summary = parse_logs(directory)

    with open("results.json", "w") as f:
        json.dump(summary, f, indent=4)

    print("\nScan Complete")
    print("-" * 40)

    print(json.dumps(summary, indent=4))

    print(f"\nResults saved to results.json")
