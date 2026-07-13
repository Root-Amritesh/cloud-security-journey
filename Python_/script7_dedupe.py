#!/usr/bin/env python3
"""Script 7: Dedupe and Sort a List of IP Addresses."""

def dedupe_and_sort(items):
    """
    Removes duplicate items from a list
    and returns them in sorted order.
    """
    unique_items = set(items)
    sorted_items = sorted(unique_items)
    return sorted_items


if __name__ == "__main__":

    print("=" * 50)
    print("IP Address Deduplicator & Sorter")
    print("=" * 50)

    raw_input = input(
        "Enter IP addresses separated by commas:\n> "
    )

    ips = [ip.strip() for ip in raw_input.split(",")]

    cleaned_ips = dedupe_and_sort(ips)

    print("\nOriginal List:")
    print(ips)

    print("\nAfter Removing Duplicates:")
    print(set(ips))

    print("\nFinal Sorted List:")
    print(cleaned_ips)
