# Number guessing game:
# - Prompts the user for a level (n)
# - Randomly selects a number between 1 and n
# - Repeatedly asks for guesses until the user guesses correctly,
# - giving feedback ("Too small", "Too large", "Just right")

import random


def main():
    while True:
        try:
            level = int(input("Enter Level: "))
        except ValueError:
            print("You must enter a positive integer")
        else:
            if level > 0:
                break
            else:
                print("You must enter a positive integer")
    print("x")


if __name__ == "__main__":
    main()