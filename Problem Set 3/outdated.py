# prompts the user for a date (AD) in the order month-day-year formatted either like 9/8/1636 or september 8, 1636 
# outputs the same date in YYYY-MM-DD format

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def num_date(date):
    month, day, year = date.split("/")

    month = int(month)
    day = int(day)
    year = int(year)

    if month < 1 or month > 12:
        raise ValueError
    if day < 1 or day > 31:
        raise ValueError

    return f"{year:04d}-{month:02d}-{day:02d}"


def letter_date(date):
    if "," not in date:
        raise ValueError

    date = date.replace(",", "")
    month, day, year = date.split(" ")

    day = int(day)
    year = int(year)

    if day < 1 or day > 31:
        raise ValueError

    z = 0
    valid_month = False
    for x in months:
        z += 1
        if month == x:
            valid_month = True
            break

    if not valid_month:
        raise ValueError

    month = z
    return f"{year:04d}-{month:02d}-{day:02d}"


def main():
    while True:
        date = input("Date: ")

        try:
            if "/" in date:
                print(num_date(date))
            else:
                print(letter_date(date))
            break
        except (ValueError, IndexError):
            pass


main()
