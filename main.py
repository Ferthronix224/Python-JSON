import json

person_1 = {
    "name": "Fernando",
    "age": 22,
    "city": "Purisima"
}

print(person_1.keys())

json_1 = json.dumps(person_1)
json_2 = json.dumps(['hello', 'hello'])
print(person_1)
print(json_1)
print(json_2.count('hello'))
