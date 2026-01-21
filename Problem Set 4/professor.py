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


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass


def quiz(level):
    score = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        correct_answer = x + y
        got_answer = False

        for _ in range(3):
            try:
                user_answer = int(input(f"{x} + {y} = "))
                if user_answer == correct_answer:
                    score += 1
                    got_answer = True
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")

        if not got_answer:
            print(correct_answer)

    return score


def main():
    level = get_level()
    print(f"Score: {quiz(level)}")


if __name__ == "__main__":
    main()
