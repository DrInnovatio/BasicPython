# Create a program that asks the user for 8 names of people and store them in a list.
# When all the names have been given, pick a random one and print it.

import random

users = []

for x in range(0, 4):
    name = input("Enter the name : ")
    users.append(name)

number = random.randint(0, 4)

print(users[number])

# Create a guess game with the names of the colors.
# At each round pick a random color from a list and let the user try to guess it.
# When he does it, ask if he wants to play again. Keep playing until the user  types "no".



colors = ["red", "yellow", "purple", "green", "pink", "orange", "black", "white", "rainbow"]

x = random.randint(0, 8)

while True:

    if myColor == colors[x]:
        print("Correct !!!")
        break
    elif myColor == "no":
        print("The End")
        break
    else:
        myColor = input("Enter your color again : ")


# Tutor's answer  

while True:
    color = colors[random.randint(0, len(colors) - 1)]
    myColor = input("Enter your color : ")

    while True:
        if (color == myColor):
            break
        else:
            myColor = input("Nope. Try again! : ")

    print("You guessed it! I was thinking about ", color)

    play_again = input("Let's play again? Type 'no' to quit.")

    if play_again.lower() == "no":
        break

print("It was fun, thanks for playing!!")


















