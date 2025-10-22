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
    return (f"{year:04d}-{month:02d}-{day:02d}")

def letter_date(date):
    date = date.replace(",", "")
    month, day, year = date.split(" ")
    day = int(day)
    year = int(year)
    z = 0
    for x in months:
        z += 1
        if month == x:
            break
    month = z
    return(f"{year:04d}-{month:02d}-{day:02d}")

def main():
    date = input("enter a date in the order month-day-year, formatted either like 9/8/1636 or september 8, 1936: ")
    if "/" in date:
        print(num_date(date))
    else:
        print(letter_date(date))

main()