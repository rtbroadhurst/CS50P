# Users validators library to validate an email input

import validators

def validate(email):
    if validators.email(email) == True:
        return "valid"
    else:
        return "Invalid"

def main():
    print(validate(input("Enter email: ")))

if __name__ == "__main__":
    main()