import random
from art import logo


def check_number(guess, number):
    if guess < number:
        print("too low.")
    elif guess > number:
        print("too high.")


def guess_game():
    print(logo)
    print("welcome to the number guessing game.")
    print("I am thinking of a number between 1 and 100.")
    number = random.randint(1, 100)
    if input("choose a difficulty. type 'easy' or 'hard': ") == "easy":
        attempt = 10
    else:
        attempt = 5
    is_game_on = True
    while is_game_on:
        print(f"you have {attempt} attempts remaining to guess the number.")
        guess = int(input("make a guess: "))
        check_number(guess, number)
        attempt -= 1
        if guess == number:
            print(f"you got it. the number was {number}")
            is_game_on = False
        elif attempt >= 1:
            print("guess again.")
            is_game_on
        else:
            print("you've run out of guesses, you lose.")
            is_game_on = False


while input("do you want to play a number guessing game? type 'y' to continue and 'n' to end: ") == "y":
    guess_game()
