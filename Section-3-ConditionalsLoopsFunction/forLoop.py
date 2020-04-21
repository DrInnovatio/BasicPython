# blog_posts = ["", "jung-un Kim is in grave danger", "", "How to make HTTP requests in Python.", "A tutorial about data types"]
#
# for post in blog_posts:
#     if post == "":
#         continue
#     else:
#         print(post)

print("===================")

myString = "This is a string!"

for char in myString:
    print(char)

print("===================")

for x in range(0, 10):
    print(x)

print("===================")

person = {'name' : 'Karen Smith', 'age' : 25, 'gender' : 'female'}

for key in person:
    print(key, ":", person[key])

print("===================")

blog_posts2 = {"Python" : ["jung-un Kim is in grave danger", "How to make HTTP requests in Python.",
                           "A tutorial about data types"],
               "Javascript" : ["A tutorial about React", "Who is crying for Javascript?"]}

for category in blog_posts2:
    print("Posts about", category)
    for post in blog_posts2[category]:
        print(post)

print("===================")

classes = {"A Class" : ["Matt", "James", "Jane"],
           "B Class" : ["Kobe", "Paul", "Winny"]}

for group in classes:
    print("Classes ", group)
    for student in classes[group]:
        print(student)
        

print("===================")