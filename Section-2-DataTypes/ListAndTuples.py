# List uses []

students = ["john", "Mary", "Steve"]

print(type(students))

print(len(students))

print(students[0])

print(students[-1])


# Tuple uses ()

# Using tuple is safer because we make sure it won't be changed later even by accident which could happen in a complex program.

months = ("July", "June", "May", "April")

print(type(months))

print(months[0])

print(len(months))

students[0] = "Matt"

print(students)

students.append("Kate")

print(students)

students.insert(0, "Peter")

print(students)

print(students.pop())  # taking out the last array

print(students.pop(0))

students.remove("Mary")

print(students)

students2 = ["Paul", "John"]

print(students + students2)  # Lists can be combined.







