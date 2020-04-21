# Create a program to calculate the BMI (body mass index) of a person.
# Ask the user for his height in  meters and his weight in kg.

# BMI = weight / (height * height)
# weight is kg
# height in meters

# BMI = (weight / (height * height)) * 703
# weight in pounds
# height in inches
# 1 foot = 12 inches

# Print the BMI and the if classification:
#
# Less than or equal to 18.5 : Underweight
# Greater than 18.5 or less than or equal to 24.9 : Normal Weight
# Greater than 24.9 or less than or  equal to 29.9 : Overweight
# Greater than or equal to 30 : Obesity


weight = float(input("Enter your weight :  "))
height = float(input("Enter your height :  "))

bmi = round(weight / (height * height), 2)

print("Your BMI is ", bmi)

if bmi <= 18.5:
    classification = "Underweight"
elif bmi > 18.5 and bmi <= 24.9:
    classification = "Normal Weight"
elif bmi > 24.9 and bmi <= 29.9:
    classification = "Overweight"
else:
    classification = "Obesity"

print("The result of your BMI is ", classification)