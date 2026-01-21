# takes an input of mass and returns the equivalent energy in joules using E = mc^2

def ConvertToEnergy(mass):
    energy = mass * (300000000 ** 2)
    return energy

def main():
    mass = int(input("enter mass in kg as an integer: "))
    print(f"{ConvertToEnergy(mass):,} joules")

main()