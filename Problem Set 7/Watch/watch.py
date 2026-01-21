# takes a string of html as input and then returns any youtube url that's an src attribute of an iframe element therein and returns a shorter youtu.be equivalent as a string

import re

def parse(s):
    match = re.search(r"src=\"https?://(?:www\.)?youtube\.com/embed/(.+?)\"", s)
    if not match:
        return None
    return ("https://youtu.be/" + match.group(1))
    

def main():
    print(parse(input("HTML: ")))


if __name__ == "__main__":
    main()
