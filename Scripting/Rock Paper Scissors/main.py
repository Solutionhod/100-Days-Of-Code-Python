rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random


def game_on():
    choice_list = [rock, paper, scissors]
    user_choice = int(input("What do you choose? Type 0 for rock, 1 for paper and 2 for scissors: "))
    computer_choice = random.randint(0, 2)
    if type(user_choice) != int:
        return "you typed a wrong input"
    elif user_choice == computer_choice:
        print(f"you chose:\n{choice_list[user_choice]}\ncomputer chose:\n{choice_list[computer_choice]}")
        print("it's a Draw")
    elif user_choice == 0 and computer_choice == 1:
        print(f"you chose:\n{choice_list[user_choice]}\ncomputer chose:\n{choice_list[computer_choice]}")
        print("paper cover rock. You lose")
    elif user_choice == 0 and computer_choice == 2:
        print(f"you chose:\n{choice_list[user_choice]}\ncomputer chose:\n{choice_list[computer_choice]}")
        print("rock beats scissors. You win")
    elif user_choice == 1 and computer_choice == 0:
        print(f"you chose:\n{choice_list[user_choice]}\ncomputer chose:\n{choice_list[computer_choice]}")
        print("paper cover rock. You win")
    elif user_choice == 1 and computer_choice == 2:
        print(f"you chose:\n{choice_list[user_choice]}\ncomputer chose:\n{choice_list[computer_choice]}")
        print("scissors cuts paper. You lose")
    elif user_choice == 2 and computer_choice == 0:
        print(f"you chose:\n{choice_list[user_choice]}\ncomputer chose:\n{choice_list[computer_choice]}")
        print("rock beats scissors. You lose")
    elif user_choice == 2 and computer_choice == 1:
        print(f"you chose:\n{choice_list[user_choice]}\ncomputer chose:\n{choice_list[computer_choice]}")
        print("scissors cuts paper. You win")


game_on()
