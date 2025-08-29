# This function takes a string as input and replaces all occurrences of ":)" with "🙂" and ":(" with "🙁"

def convert(Input):
    Input = Input.replace(":)", "🙂")
    Input = Input.replace(":(", "🙁")
    return Input

def main():
    print(convert(input("enter a string to be converted: ")))

main()
