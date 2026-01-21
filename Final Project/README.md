# Habit Tracker

## Description
This project is a simple command-line habit tracker written in Python.

It allows the user to:
- Log predefined daily habits
- Unmark a habit for a specific date
- Track their streak up to a specified date
- List all available habits

## Features
- Predefined habits stored in habits.csv
- Logs are stored persistently in `logs.csv
- Uses argparse for the command line interface
- Basic testing using pytest

## Usage Guide

Dates must be provided in `YYYY-MM-DD` format.

### List available habits
~~~bash
python project.py list
~~~

### Log a daily habit
Marks a habit as completed for the given date.
~~~bash
python project.py done <habit_key> <date>
~~~

Example:
~~~bash
python project.py done study 2026-01-20
~~~

### Unmark a daily habit
Marks a habit as not completed for the given date.
~~~bash
python project.py done <habit_key> <date> 0
~~~

Example:
~~~bash
python project.py done study 2026-01-20 0
~~~


### Show a habit streak
~~~bash
python project.py streak <habit_key> <date>
~~~

Example:
~~~bash
python project.py streak study 2026-01-20
~~~

## File Structure
- `project.py` — main application logic
- `habits.csv` — predefined habits
- `logs.csv` — persistent habit logs
- `test_project.py` — automated tests
- `requirements.txt` — external dependencies
