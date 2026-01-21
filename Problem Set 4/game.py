# Number guessing game:
# - Prompts the user for a level (n)
# - Randomly selects a number between 1 and n
# - Repeatedly asks for guesses until the user guesses correctly
# - Gives feedback ("Too small", "Too large", "Just right")


import random
import sys


def guess(rand_int):
    # Continuously prompts the user to guess until they match rand_int
    while True:
        # Validate user input and ensure it's a positive integer
        while True:
            try:
                guess = int(input("Enter guess: "))
            except ValueError:
                print("You must enter a positive integer")
            else:
                if guess > 0:
                    break

        # Compare the guess to the random number
        if guess == rand_int:
            print("Just right!")
            sys.exit()
        elif guess > rand_int:
            print("Too large!")
        else:
            print("Too small!")


def main():
    # Prompts the user for a level and starts the guessing game
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

    # Generate a random integer between 1 and the chosen level (inclusive)
    rand_int = random.randint(1, level)

    # Start the guessing loop
    guess(rand_int)


if __name__ == "__main__":
    main()
