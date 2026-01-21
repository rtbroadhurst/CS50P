# this function takes a greeting as its input and returns a value based on the greeting
# if the greeting starts with "hello" (case insensitive) the function returns $0
# if the greeting starts with "h" (case insensitive) the function returns $20   
# otherwise the function returns $100


def value(greeting):
  greeting = greeting.lower().strip()
  if greeting.startswith("hello"):
     return "$0"
  elif greeting.startswith("h"):
     return "$20"
  else:
     return "$100"


def main():
    greeting = input("Greeting: ")
    print(value(greeting))

main()