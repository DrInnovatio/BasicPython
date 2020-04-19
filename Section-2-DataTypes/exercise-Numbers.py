# Create a program to calculate the area and circumference of a circle. Ask the user for the radius.

import math

radius = float(input("What is the radius ? : "))

circumference = 2 * math.pi * radius

area = math.pi * math.pow(radius, 2)

print("The circumference is ", round(circumference, 2))
print("The area is ", round(area, 2))

