# validates that a vanity license plate meets the following requirements:
# must be 2 to 6 characters long
# must start with at least two letters
# may only contain alphanumeric characters (no spaces, periods, or punctuation)
# numbers may not appear in the middle of the plate (must all be at the end)


def check_middle(plate):
    # checks that numbers are not enclosed by characters
    seen_number = False
    for ch in plate:
        if ch.isdigit():
            seen_number = True
        elif seen_number and ch.isalpha():
            return False
    return True


def is_valid(plate):
    # Length check
    if len(plate) < 2 or len(plate) > 6:
        return False

    # First two characters must be letters
    for x in range(0, 2):
        if not plate[x].isalpha():
            return False

    # Check for periods, spaces, punctuation
    for ch in plate:
        if not ch.isalnum():
            return False

    # Check that numbers don't appear in the middle
    if not check_middle(plate):
        return False

    return True


def main():
    plate = input("Enter plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


main()
