# prompts the user for names (one per line) until the user inputs control-d
# bid adieu to those names, separating two names with one and, three names with two commas and one and, and 𝑛 names with 𝑛 −1 commas and one and
# example: Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl

import sys

# uses the list of names to generate the adieu adieu string
def generate_adieu(names):
    if len(names) == 1:
        return (f"Adieu, adieu, to {names[0]}")
    elif len(names) == 2:
        return (f"Adieu, adieu, to {names[0]} and {names[1]}")
    else:
        string = ", ".join(names[:-1]) + (f", and {names[-1]}")
        return "Adieu, adieu, to "  + string



def main():
    names = []
    while True:   # take in the names as input and add them to the list "names" until the user presses ctrl d
        try:
            print("Name: ")
            name = input()
            names.append(name)

        except EOFError:
            print(generate_adieu(names))
            sys.exit()


if __name__ == "__main__":
    main()

