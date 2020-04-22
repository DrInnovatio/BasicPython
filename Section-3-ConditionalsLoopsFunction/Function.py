def say_hello(person1, person2):
    print("Hello Functions" , person1, person2)

say_hello("John", "Kobe")

def waiting(person3="The teacher"):
    print(person3, "is waiting for you.")

waiting()

def farh2celsius(farh):
    celsius = (5 * (farh - 32 )) / 9
    return celsius

print("Celsius : ", round(farh2celsius(100), 2))
print("Kelvin : ", round(farh2celsius(100) + 273.5, 2))