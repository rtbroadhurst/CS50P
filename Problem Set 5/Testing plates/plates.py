# validates Massachusetts license plates: 2-6 characters with first two letters,
# only alphanumeric characters, and no letters after numbers

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


if __name__ == "__main__":
    main()
