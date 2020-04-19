# Dictionary uses {}

person = { "first_name" : "John", "last_name" : "Smith", "birth_year" : 1980, "country_of_birth" : "Canada" }

print(type(person))

print(person["first_name"])

person["country_of_birth"] = 1979

print(person)

person["marital_status"] = "Married"

print(person)

person["children"] = ["Nathali", "Ethan"]

print(person)

person["children"].append("Anna")

print(person)

person.get("age", "invalid property")

person.clear()

print(person)