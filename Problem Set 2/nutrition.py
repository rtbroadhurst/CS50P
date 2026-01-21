# prompts the user to enter a fruit (from fda poster) and then returns calorie information 

fruits = {
    "apple": 130,
    "avocado": 50,
    "banana": 110,
    "cantaloupe": 50,
    "grapefruit": 60,
    "grapes": 90,
    "honeydew melon": 50,
    "kiwifruit": 90,
    "lemon": 15,
    "lime": 20,
    "nectarine": 60,
    "orange": 80,
    "peach": 60,
    "pear": 100,
    "pineapple": 50,
    "plums": 70,
    "strawberries": 50,
    "sweet cherries": 100,
    "tangerine": 50,
    "watermelon": 80
}


def get_calories(fruit):
    if fruit in fruits:
        return fruits[fruit]
    else:
        return "no calorie data"

def main():
    fruit = input("Enter a fruit: ").lower().strip()
    calories = get_calories(fruit)
    print(f"Calories: {calories}")