#!/usr/bin/env python3
"""Script 1: Number guessing game."""

import random


def play_game():
    secret = random.randint(1, 100)
    attempts = 0

    print("Guess a number between 1 and 100.")

    while True:
        guess = int(input("Your guess: "))
        attempts += 1

        if guess < secret:
            print("Too low.")
        elif guess > secret:
            print("Too high.")
        else:
            print(f"Correct! You got it in {attempts} attempts.")
            break


if __name__ == "__main__":
    play_game()
