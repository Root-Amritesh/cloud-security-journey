#!/usr/bin/env python3
"""Script 2: Advanced calculator (continuous mode)."""

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def calculate(a, op, b):
    ops = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide
    }

    if op not in ops:
        raise ValueError(f"Unknown operator: {op}")

    return ops[op](a, b)


if __name__ == "__main__":

    result = float(input("First number: "))

    while True:
        op = input("Operator (+ - * /): ")

        next_num = float(input("Next number: "))

        try:
            result = calculate(result, op, next_num)
            print(f"\nCurrent Result: {result}\n")
        except ValueError as e:
            print(e)
            continue

        again = input("Continue? (y/n): ").lower()

        if again != "y":
            break

    print(f"\nFinal Result: {result}")
