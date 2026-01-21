# takes in a string of texts and outputs it with vowels removed (A, E, I, O, U)

def shorten(text):
    txt_removed = ""
    for ch in text:
        if ch.upper() not in {'A', 'E', 'I', 'O', 'U'}:
            txt_removed += ch
    return txt_removed


def main():
    print(shorten(input("enter text to be shortened: ")))


if __name__ == "__main__":
    main()
