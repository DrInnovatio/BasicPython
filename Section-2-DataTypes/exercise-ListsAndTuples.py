# 1) Create a program that asks the user for his birthday in the format "DD-MM-YYYY" then print:
# "You were born in [month]"
# example: "You were born in January."

birthday = input("When is your birthday ? (DD-MM-YYYY) : ")

x = int(birthday[3:5])

months = ("January", "February", "March", "April", "May", "June", "July", "August",
          "September", "October", "November", "December")

print("You were born in ", months[x - 1])

#     10-04-1981


# 2) Create a program with a predefined list of people.
# Ask the user for his name, add it to the end of the list and print the updated list.


people = ["Matt", "Kan", "Jane", "John", "Kobe"]

user = input("Enter the user name :  ")

people.append(user)

print(people)




