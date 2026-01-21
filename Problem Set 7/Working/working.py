# takes in a 12 hour time as a string and returns the corresponding time in 24 hour format

import re


def am_to_pm(am_pm, hours):
    if am_pm == "AM":
        if hours == "12":
            return "00"
        return hours
    else:  # PM
        if hours == "12":
            return hours
        hours = int(hours) + 12
        return str(hours)


def convert(s):
    search = re.fullmatch(
        r"(1[0-2]|0?[1-9])(:[0-5][0-9])? (AM|PM) to (1[0-2]|0?[1-9])(:[0-5][0-9])? (AM|PM)",
        s,
        re.IGNORECASE,
    )
    if not search:
        raise ValueError

    hours1 = search.group(1)
    minutes1 = search.group(2)
    am_pm1 = search.group(3).upper()

    hours2 = search.group(4)
    minutes2 = search.group(5)
    am_pm2 = search.group(6).upper()

    if minutes1 is None:
        minutes1 = "00"
    else:
        minutes1 = minutes1[1:]  # drop the ":"

    if minutes2 is None:
        minutes2 = "00"
    else:
        minutes2 = minutes2[1:]  # drop the ":"

    hours1 = am_to_pm(am_pm1, hours1).zfill(2)
    hours2 = am_to_pm(am_pm2, hours2).zfill(2)

    return f"{hours1}:{minutes1} to {hours2}:{minutes2}"


def main():
    print(convert(input("Hours: ")))


if __name__ == "__main__":
    main()
