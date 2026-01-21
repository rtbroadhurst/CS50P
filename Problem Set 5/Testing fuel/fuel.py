# prompts the user for a fraction (formatted X/Y) where X and Y are positive integers
# converts the fraction into a percentage (rounded to the nearest integer)
# prints "E" if 1% or less remains, and "F" if 99% or more remains

def main():
    while True:
        try:
            fraction = input("Fraction: ")
            percentage = convert(fraction)
            print(gauge(percentage))
            break
        except (ValueError, ZeroDivisionError):
            # keep prompting until valid input
            continue


def convert(fraction):
    # splits the user input and converts to integers
    X, Y = fraction.split("/")
    X = int(X)
    Y = int(Y)

    # raises errors for invalid cases
    if Y == 0:
        raise ZeroDivisionError
    if X > Y:
        raise ValueError

    # calculates and returns the percentage
    return round(X / Y * 100)


def gauge(percentage):
    # returns "E" for empty, "F" for full, or the percentage
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
