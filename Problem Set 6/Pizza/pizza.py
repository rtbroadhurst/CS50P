# takes the name or path or a csv file and outputs a table formatted as ASCII art using the the tabulate package

from sys import exit, argv
from tabulate import tabulate
import csv


def return_table(file_name):
    data = []
    with open(file_name, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return tabulate(data)


def get_args():
    if len(argv) > 2:
        exit("Too many command-line arguments")
    if len(argv) < 2:
        exit("Too few command-line arguments")
    if not argv[1].endswith(".csv"): 
        exit("Not a csv file")
    return argv[1]
    

def main():
    file_name = get_args()
    try:
        print(return_table(file_name))
    except FileNotFoundError:
        exit("File does not exist")


if __name__ =="__main__":
    main()