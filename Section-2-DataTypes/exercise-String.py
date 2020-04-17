# 1) Create a program that asks the user for his first name, his middle name and his last name. Then print:
# "Your initials are ___"

first_name = input("What is your first name : ")
middle_name = input("What is your middle name : ")
last_name = input("What is your last name : ")

first_initial = (first_name[0]).upper()
middle_initial = (middle_name[0]).upper()
last_initial = (last_name[0]).upper()

print("Your initial is ", first_initial,".", middle_initial, ".",last_initial)
print("=============")


# 2) Let's say your company has a product with this lot number: "037-00901-00027".
# 037 is the country code. 00901 is the product code. 00027 is the batch number.
# Create a program to print:
# Country Code:
# Product Code:
# Batch Code:

lotNumber = "037-00901-00027"

print("Country Code : ", lotNumber[0:3])
print("Product Code : ", lotNumber[4:9])
print("Batch Code : ", lotNumber[-5:])