# expects an IPv4 address as input as a string and then returns True or False depending on whether the input is a valid IPv4 address or not

def validate(ip):
    parts = ip.split(".")

    if len(parts) != 4:
        return False
    
    for part in parts:

        if not part.isdigit():
            return False

        num = int(part)

        if num < 0 or num > 255:
            return False
        
        if part.startswith("0") and part != "0":
            return False
    
    return True

def main():
    print(validate(input("IPv4 Address: ")))


if __name__ == "__main__":
    main()
