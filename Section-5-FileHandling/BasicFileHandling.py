# Open the file and read() mode.

f = open("test.txt", "r")
print(f.read())

# Over writing on the file.

f = open("test.txt", "w")
f.write("This is what I wrote!!")
f = open("test.txt")
print(f.read())

# Append() mode

f = open("test.txt", "a")
f.write("\nThis is not overwriting!!")

f = open("test.txt")
print(f.read())

# Creating a file in another folder on my Mac.
# open("/User/bmac/Desktop/myFile2.txt.rtf", "x")
