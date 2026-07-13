#!/usr/bin/env python3
"""Script 8: Port-to-Service Lookup."""

COMMON_PORTS = {
    20: "FTP Data",
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL"
}


def lookup_service(port):
    return COMMON_PORTS.get(port, "Unknown")


if __name__ == "__main__":

    print("=" * 50)
    print("Port to Service Lookup")
    print("=" * 50)

    while True:

        port = int(input("\nEnter a port number: "))

        service = lookup_service(port)

        print(f"Port {port} → {service}")

        again = input("\nLookup another port? (y/n): ").lower()

        if again != "y":
            break

    print("\nGoodbye!")
