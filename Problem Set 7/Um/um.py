# takes a line of text as an input and returns the number of times um appears in the text, as a word itself, not a substring of another word

import re

def count(s):
    matches = re.findall(r"\bum\b", s, re.IGNORECASE)
    return len(matches)


def main():
    print(count(input("Text: ")))


if __name__ == "__main__":
    main()

