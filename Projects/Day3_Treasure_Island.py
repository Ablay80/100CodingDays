#🚨Treasure Island
from Art import logo3
print(logo3)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input('You\'re at a crossroad. Where do you want to go?\nType "left" or "right": ').lower()
if choice1 == "left":
    choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake.\nType "wait" to wait for a boat.\nType "swim" to swim across: ').lower()
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue.\nWhich colour do you choose? ").lower()
        if choice3 == "blue":
            print("You enter a room of beasts. Game Over.")
        elif choice3 == "red":
            print("It's a room full of fire. Game Over.")
        elif choice3 == "yellow":
            print("You found the treasure! You Win!")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.") 