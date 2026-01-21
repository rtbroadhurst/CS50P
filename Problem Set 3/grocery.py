# prompts the user for one item per line, until the user inputs control d
# then outputs the user whole grocery list in all upercase, sorted alphabetically by item, prefixing each line with the number of times the user inputted that item

grocery = {}

def output_list():
    grocery_sorted = sorted(grocery)
    for item in grocery_sorted:
        print(grocery[item], item)

def add_to_list(item):
    if item in grocery:
        grocery[item] += 1
    else:
        grocery[item] = 1


def main():
    while True:
        try:
            item = input().upper()
            add_to_list(item)
        except EOFError:
            output_list()
            break

main()