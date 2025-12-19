# takes in a 12 hour time as a string and returns the corresponding time in 24 hour format

import re

def am_to_pm(am_pm,hours):
    if am_pm == "AM":
        if hours == "12":
            hours = "00"
            return hours
        return hours
    elif am_pm == "PM":
        if hours == "12":
            return hours
        else:
            hours = int(hours)
            hours += 12
            hours = str(hours)
            return hours


def convert(s):
    search = re.fullmatch(r"(1[0-2]|0?[1-9])(:[0-5][0-9])? ?(AM|PM) to (1[0-2]|0?[1-9])(:[0-5][0-9])? ?(AM|PM)", s, re.IGNORECASE)
    if not search:
        raise ValueError
    
    hours1 = search.group(1)
    minutes1 = search.group(2).strip(":")
    am_pm1 = search.group(3).upper()
    hours2 = search.group(4)
    minutes2 = search.group(5).strip(":")
    am_pm2 = search.group(6).upper()

    hours1 = am_to_pm(am_pm1, hours1)
    hours2 = am_to_pm(am_pm2, hours2)

    return (hours1 + ":" + minutes1 + " to " + hours2 + ":" + minutes2)
        
        


def main():
    print(convert(input("Hours: ")))


if __name__ == "__main__":
    main()
