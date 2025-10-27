# takes in a string as a user input and uses the pyfiglet module to convert it into ascii art
# if the user passes 0 arguments a random font will be used
# if the user wants to select a font they will need to pass -f (or --font) and their desired font as arguments

import sys
import random
from pyfiglet import Figlet

figlet = Figlet()               
font_list = figlet.getFonts()  

def main():
    terminal_argument = sys.argv
    if len(terminal_argument) == 1:
        user_input = input("Enter text: ") # takes in a user input to be displayed
        figlet.setFont(font=(random.choice(font_list))) # chises a random font to display it in from the list of fonts
        print(figlet.renderText(user_input)) # outputs the text using figlet

    elif len(terminal_argument) == 3:
        user_input = input("Enter text: ")
    else:
        print("invalid argument")





if __name__ == "__main__":
    main()
    