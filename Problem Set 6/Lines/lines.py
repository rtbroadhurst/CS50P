# takes in the name or path of a python file and outputs the number of lines in the file
# excluding comments and blank lines

import sys

def number_of_lines(file_name):  # returns the number of lines in the program
    num_lines = 0
    with open(file_name, "r") as file:
        for line in file:
            line = line.strip()
            if len(line) == 0:
                continue
            if line.startswith("#"):
                continue
            num_lines += 1
    return num_lines

def get_args():
    # checks that the user has inputted exactly one command line argument
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    # checks that the user has inputted a python file
    if not sys.argv[1].lower().endswith(".py"):
        sys.exit("Not a Python file")

    return sys.argv[1]

def main():
    file_name = get_args()
    try:
        print(number_of_lines(file_name))
    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()