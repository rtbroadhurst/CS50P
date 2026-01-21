# takes in two command line arguments
# the name of an existing CSV file to read as input, whose columns are assumed to be, in order, name and house, and
# the name of a new CSV to write as output, whose columns should be, in order, first, last, and house.
# Converts that input to that output, splitting each name into a first name and last name. Assume that each student will have both a first name and last name.

from sys import argv, exit
from csv import DictReader, DictWriter


def get_args():
    if len(argv) > 3:
        exit("Too many command-line arguments")
    if len(argv) < 3:
        exit("Too few command-line arguments")
    if not argv[1].lower().endswith(".csv") or not argv[2].lower().endswith(".csv"): 
        exit("Not a csv file")
    return argv[1], argv[2]


def read_existing_csv(existing_csv):
    existing_csv_data = []
    with open(existing_csv, "r") as existing:
        reader = DictReader(existing)
        for row in reader:
            existing_csv_data.append(row)
        return existing_csv_data


def reformat_existing_csv(existing_csv_data):
    reformatted_existing_csv = []
    for row in existing_csv_data:
        first, last = row["name"].split(",", 1)
        first = first.strip()
        last = last.strip()
        reformatted_existing_csv.append({"first": first, "last": last, "house": row["house"]})
    return reformatted_existing_csv


def write_reformatted_csv(reformatted_csv, new_csv):
    with open(new_csv, "w") as new:
        writer = DictWriter(new, fieldnames=["first", "last", "house"])
        writer.writeheader()
        writer.writerows(reformatted_csv)



def main():
    existing_csv, new_csv = get_args()
    existing_csv_data = read_existing_csv(existing_csv)
    reformatted_csv = reformat_existing_csv(existing_csv_data)
    write_reformatted_csv(reformatted_csv, new_csv)



if __name__ =="__main__":
    main()