import requests
import json
import pprint

r = requests.get("https://opentdb.com/api.php?amount=1&category=12&difficulty=easy&type=multiple")

question = json.loads(r.text)

print(question)
print(type(question))

print(pprint.pprint(question))

person = {'name': 'John', 'age' : 30}
person_json = json.dumps(person)
print(person_json)

boy = {'name' : 'Paul', 'age' : 33, 'job' : 'datascientist', 'hometown' : 'new york', 'criminalRecord' : 'none'}
boy_json = json.dumps(boy)
print(boy_json)

# If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.