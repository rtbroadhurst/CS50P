# prompts the user for a fraction (formatted X/Y) where X and Y are positive integers, then outputs as a percentage rounded to the nearest integer how much fuel is in the tank
# if 1% of less remains, the program returns empty and if 99% or more remains, the program returns full

def fraction_to_percentage(X, Y):
    percentage = round(X / Y * 100)
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"


def main():
    while True:
        try:
            fraction = input("Enter a fraction formatted X/Y: ")
            X, Y = fraction.split("/")
            X = int(X)
            Y = int(Y)

            if X < 0 or Y <= 0:
                print("The numbers must be positive and above 0")
                continue

            if X > Y:
                print("X cannot be greater than Y")
                continue

            X / Y

        except ValueError:
            print("X and Y must be integers")
        except ZeroDivisionError:
            print("Y cannot be zero")
        else:
            break
    
    print(fraction_to_percentage(X, Y))



main()


               
        

