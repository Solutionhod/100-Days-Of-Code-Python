import random
from art import logo, vs
from game_data import data


def generate_data():
    """Generates a random data dictionary from data list"""
    random_data = random.choice(data)
    return random_data


def compare(data1, data2):
    if int(data1["follower_count"]) > int(data2["follower_count"]):
        return "A"
    else:
        return "B"


def game():
    print(logo)
    score = 0
    data1 = generate_data()
    game_on = True
    while game_on:
        print(f"Compare A: {data1['name']}, {data1['description']}, from {data1['country']}.")
        print(vs)
        data2 = generate_data()
        while data1 == data2:
            data2 = generate_data()
        print(f"Compare B: {data2['name']}, {data2['description']}, from {data2['country']}.")
        if input("Who has more followers? Type 'A' or 'B': ").upper() == compare(data1, data2):
            score += 1
            print(f"You're right! Current score: {score}.")
            data1 = data2
            game_on
        else:
            print(f"Sorry, that's wrong. Final score: {score}.")
            game_on = False


game()
