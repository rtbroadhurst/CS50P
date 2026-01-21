from project import validate_date, calculate_streak, log_done
import os
import csv

# testing for validate_date
def test_validate_date_valid():
    assert validate_date("2026-01-20") is True

def test_validate_date_invalid_format():
    assert validate_date("20-01-2026") is False

def test_validate_date_impossible_date():
    assert validate_date("2026-02-30") is False


# testing for calculate_streak
def test_calulate_streak_no_logs(tmp_path):
    os.chdir(tmp_path)
    (tmp_path / "habits.csv").write_text("habit_key,name\nstudy,Study\n")
    assert calculate_streak("study", "2026-01-20") == 0

def test_calculate_streak_three_day_streak(tmp_path):
    os.chdir(tmp_path)
    (tmp_path / "habits.csv").write_text("habit_key,name\nstudy,Study\n")

    with open(tmp_path / "logs.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["habit_key", "date", "done"])
        writer.writeheader()
        writer.writerows([
            {"habit_key": "study", "date": "2026-01-18", "done": 1},
            {"habit_key": "study", "date": "2026-01-19", "done": 1},
            {"habit_key": "study", "date": "2026-01-20", "done": 1},
        ])

    assert calculate_streak("study", "2026-01-20") == 3

# testing for log done

def test_log_done_creates_log_entry(tmp_path):
    os.chdir(tmp_path)
    (tmp_path / "habits.csv").write_text("habit_key,name\nstudy,Study\n")

    log_done("study", "2026-01-20")

    # check logs.csv exists and contains the entry
    with open(tmp_path / "logs.csv", "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    assert len(rows) == 1
    assert rows[0]["habit_key"] == "study"
    assert rows[0]["date"] == "2026-01-20"
    assert rows[0]["done"] == "1"




