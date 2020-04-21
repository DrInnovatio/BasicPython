# people = []
#
# while len(people) < 5:
#     person = input("Type the name of a person : ")
#     people.append(person)
# print(people)

import random

number = random.randint(0, 10)
guess = int(input("I am thinking about a number between zero and ten. Can you guess it ?  "))

while True:
    if guess == number:
        break
    else:
        guess = int(input("Nope. Try again!!"))
print("You guessed it. I was thinking about ", number)
