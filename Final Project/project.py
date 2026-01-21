import csv
from datetime import datetime, timedelta
import argparse


def main():
    # create parser and subparser objects
    parser = argparse.ArgumentParser(description="Simple habit tracker")
    subparsers = parser.add_subparsers(dest="command")

    # create subparser for done command
    done_parser = subparsers.add_parser("done", help="Mark a habit as completed on a given date")
    done_parser.add_argument("habit_key")
    done_parser.add_argument("date")
    done_parser.add_argument("done_specifier", nargs="?", type=int, choices=[0, 1], default=1)

    # create subparser for streak command
    streak_parser = subparsers.add_parser("streak", help="Show the streak for a habit as of a date")
    streak_parser.add_argument("habit_key")
    streak_parser.add_argument("as_of")

    # create a subparser for list command
    list_parser = subparsers.add_parser("list", help="list available habits")


    # gets the args object
    args = parser.parse_args()

    # logic for if the user enters no command
    if args.command is None:
        parser.print_help()
        return

    try:
        # logic for when the user enters done command
        if args.command == "done":
            log_done(args.habit_key, args.date, args.done_specifier)
            if args.done_specifier == 1:
                print("Habit Logged")
            elif args.done_specifier == 0:
                print("Habit Marked Not Done")
            
        # logic for when the user enters streak command
        elif args.command == "streak":
            streak = calculate_streak(args.habit_key, args.as_of)
            print(f"Your streak is: {streak}")

        # logic for when the user enters list command
        elif args.command == "list":
            habits = load_habits()
            for habit_key, name in habits.items():
                print(f"{habit_key}:  {name}")


    except ValueError as e:
        parser.error(str(e))
        

def load_habits() -> dict[str, str]: 
    """loads the predefined habits from habits.csv into a dict"""

    habits: dict[str, str] = {}

    with open("habits.csv", "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            habit_key = row["habit_key"].strip()
            name = row["name"].strip()

            habits[habit_key] = name

    return habits


def load_logs() -> list[dict[str, str | int]]:
    """loads the log csv into a list of dicts where each dict is a log"""

    logs: list[dict[str, str | int]] = []

    try:
        with open("logs.csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                logs.append({
                    "habit_key": row["habit_key"].strip(),
                    "date": row["date"].strip(),
                    "done": int(row["done"]),
                })

    except FileNotFoundError:
        return logs
    
    return logs
  

def save_logs(logs: list[dict[str, str | int]]) -> None:
    """writes the logs for the day into the logs csv"""

    with open("logs.csv", "w", newline="", encoding="utf-8") as file:

        writer = csv.DictWriter(file, fieldnames=["habit_key", "date", "done"])
        writer.writeheader()
        writer.writerows(logs)


def log_done(habit_key: str, date: str, done: int = 1) -> None:
    """
    records the completion status for a habit on a date
     
    overwrites any existing log entry for the same habit and date.
    done=1 marks the habit as completed, done=0 undoes it.
    date must be in YYYY-MM-DD format
    """

    # validate that the habit exists

    habits = load_habits()
    if habit_key not in habits:
        raise ValueError("unknown habit")
    
    # validate the date format

    if not validate_date(date):
        raise ValueError("invalid date")

    # load the existing logs

    logs = load_logs()

    # remove any existing entries for the current habit + date 

    logs = [log for log in logs if not (log["habit_key"] == habit_key and log["date"] == date)]

    # add the new log entry

    logs.append(
        {
             "habit_key": habit_key,
             "date": date,
             "done": done,
        }
    )

    # save the logs

    save_logs(logs)


def calculate_streak(habit_key: str, as_of: str) -> int:
    """
    calculate the consecutive-day streak for a habit ending on as_of.

    as_of must be in YYYY-MM-DD format. A streak counts consecutive days with done=1.
    missing days or done=0 break the streak.
    """

    # validate that the habit exists

    habits: dict[str, str] = load_habits()
    if habit_key not in habits:
        raise ValueError("unknown habit")
    
    # validate the date format

    if not validate_date(as_of):
        raise ValueError("invalid date")
    
    # load the logs and filter for the desired habit type

    logs = load_logs()
    logs = [log for log in logs if log["habit_key"] == habit_key]

    # build a dictionary of {date: done} 
    
    done_date: dict[str, int] = {}

    for log in logs:
        done_date[log["date"]] = log["done"]

    # loop starting at the as_of date backwards in date, incrementing streak each time, until done = 0
    streak: int = 0
    current = datetime.strptime(as_of, "%Y-%m-%d").date()

    while True:
        current_str = current.isoformat()
        if done_date.get(current_str) == 1:
            current = current - timedelta(days=1)
            streak += 1
        else:
            return streak
        
    
def validate_date(date: str) -> bool:
    """return True if date is a valid calendar date in YYYY-MM-DD format, if not returns False."""

    try: 
        datetime.strptime(date, "%Y-%m-%d")
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    main()
