# Create a program with a predefined dictionary for a person. Include the following information : name , gender , age ,
# address and phone.

# Ask the user what information he wants to know about the person (example: name), then print the value accociated
# to that key ord(display a message in case the key is not found.


person = {"name" : "John", "gender" : "male", "age" : 34, "address" : "23 Victoria street QLD", "phone" : "0999 - 999 - 444" }

key = input("What do you want to know ?  : ").lower()

result = person.get(key, "That information is not available.!!")


print(result)

