# takes the time as an input and outputs whether its breakfast, lunch, or dinner time 

def main():
    floatTime = convert(input("What time is it? "))
    if 7.0 <= floatTime <= 8.0:
        print("breakfast time")
    elif 12.0 <= floatTime <= 13.0:
        print("lunch time")
    elif 18.0 <= floatTime <= 19.0:
        print("dinner time")

# converts time input formatted as #:## or ##:## into a float e.g. 9:30 becomes 9.5
def convert(time):
   hours, minutes = time.split(":")
   time = float(hours) + (float(minutes) / 60)
   return time


if __name__ == "__main__":
    main()
