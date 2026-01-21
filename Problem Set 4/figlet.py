# takes in a string as a user input and uses the pyfiglet module to convert it into ascii art
# if the user passes 0 arguments a random font will be used
# if the user wants to select a font they will need to pass -f (or --font) and their desired font as arguments

import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
font_list = figlet.getFonts()

def main():
    args = sys.argv

    # Choose font (random or user selected)
    if len(args) == 1:
        figlet.setFont(font=random.choice(font_list))
    elif len(args) == 3 and args[1] in ["-f", "--font"]:
        if args[2] in font_list:
            figlet.setFont(font=args[2])
        else:
            sys.exit("Font is not in list")
    else:
        sys.exit("Invalid argument")

    # Get input text and render it with figlet
    user_input = input("Enter text: ")
    print(figlet.renderText(user_input))

if __name__ == "__main__":
    main()
