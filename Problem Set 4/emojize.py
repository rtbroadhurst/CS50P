# prompts the user for a string in english and then outputs an "emojised" version of that string converting any codes (or aliases) to the corresponding emoji

import emoji

def main():
    user_input = input("Enter the input you would like to emojise: ")
    print(emoji.emojize(user_input, language='alias'))

if __name__ == "__main__":
    main()
