# Maths Quiz Game:
# - Prompts the user for a level (n), which must be 1, 2, or 3.
# - Randomly generates 10 addition problems ("X + Y ="), where:
#     - Each of X and Y is a non-negative integer with n digits.
#     - Problems are generated as pairs (x₀, y₀), (x₁, y₁), ..., (x₉, y₉).
# - Prompts the user to solve each problem.
# - For each problem:
#     - If the user's answer is incorrect or not a number, prints "EEE" and allows up to 3 attempts
#     - After 3 incorrect attempts, displays the correct answer
# - After all 10 problems, displays the user’s final score as "Score: x/10".


import random
import sys


def generate_integer(level): # generates an integer with n digits based on the levle
    if level == 1:
        return random.randint(1, 9)
    elif level == 2:
        return random.randint(10, 99)
    else: 
        return random.randint(100, 999)


def quiz(level): ## runs the quiz for 10 questions and returns a score
    score = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        correct_answer = x + y
        
        for attempts in range(3):
            try:
                user_answer = int(input(f"{x} + {y} = "))
                if user_answer == correct_answer:
                    score += 1
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")
                
        print(f"The correct answer is: {correct_answer}")

    return score
    
def main():

    while True:
        level = int(input("Enter a level (1, 2 or 3): "))
        if level in [1, 2, 3]:
            break
    
    print(f"Score: {quiz(level)}/10")


if __name__ == "__main__":
    main()