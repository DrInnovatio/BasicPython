grade1 = float(input("Enter the grade of the first test : "))
grade2 = float(input("Enter the grade of the second test : "))
absences = int(input("Enter the number of absences : "))
total_classes = int(input("Enter the total number of classes : "))

average_grade = (grade1 + grade2) / 2

attendance = (total_classes - absences) / total_classes

print("Average grade : ", round(average_grade, 2))
print("Attendance rate : ", str(round(attendance * 100)) + '%')

if (average_grade >= 6):
    if (attendance >= 0.8):
        print("The student was approved.")
    else:
        print("The student has failed due to an attendance rate lower than 80%.")
elif (attendance >= 0.8):
    print("The student has failed due to an average grade lower than 6.0.")
else:
    print("The student has failed due to an average grade lower than 6.0 and an attendance rate lower than 80%.")

