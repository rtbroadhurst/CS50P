# Prompts the user for their date of birth in YYYY-MM-DD format.
# Prints how old they are in minutes (rounded to the nearest integer) using English words.
# Assumes the user was born at midnight on that date and that the current time is midnight.

from datetime import date
import inflect
import sys

p = inflect.engine()


def get_minutes(birth_date):
    delta = date.today() - birth_date
    return round(delta.total_seconds() / 60)


def convert_to_words(minutes):
    words = p.number_to_words(minutes, andword="")
    return words.capitalize() + " minutes"


def main():
    user_input = input("Date of Birth: ").strip()
    try:
        birth_date = date.fromisoformat(user_input)
    except ValueError:
        sys.exit()

    minutes = get_minutes(birth_date)
    print(convert_to_words(minutes))


if __name__ == "__main__":
    main()
