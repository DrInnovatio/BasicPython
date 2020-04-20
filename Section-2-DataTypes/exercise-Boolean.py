# Create a program and store your age in a variable. Then, ask the user for his age and print whether:
# - He's older than you.
# - He's younger than you.
# - You two have the same age.

myAge = 40;

userAge = int(input("Enter the user's age : "))

if(myAge < userAge):
    print("He's older than you.")
elif(myAge > userAge):
    print("He's younger than you.")
else:
    print("You two have the same age.")


