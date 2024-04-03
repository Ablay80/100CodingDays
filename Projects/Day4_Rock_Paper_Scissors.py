import random
from Art import rock, paper, scissors

game_images = [rock, paper, scissors]
user_choice = int(input("What do you choose?\n1 - Rock, 2 - Paper, 3 - Scissors\nType: "))
if user_choice >= 4 or user_choice < 1: 
    print("You typed an invalid number, you lose!") 
else:
    user_choice -= 1
    print(game_images[user_choice])
    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])
    if user_choice == 0 and computer_choice == 2:
        print("You win")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose")
    elif computer_choice == user_choice:
        print("It's a draw")
    elif computer_choice > user_choice:
        print("You lose")
    else:
        print("You win")