# asks the user what the answer to the Great Question of Life, the Universe and Everything
# outputs yes if the answer is 42 and otherwise responds with no

def main():
    answer = input("What is the answer to the Great Question of Life, the Universe and Everything? ")
    answer = answer.lower().strip()

    if answer == "42" or answer == "forty two" or answer == "forty-two":
        print("Yes")
    else:
        print("No")

main()