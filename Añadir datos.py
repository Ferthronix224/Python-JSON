import json
import random

person = []
names = ['Fernando', 'Adolfo', 'Victor', 'Mary', 'Jason', 'Merlin', 'Ma.', 'Martha', 'Fred', 'Shaggy']
lastName = 'Alonso'
ages = [18, 20, 22, 24, 26]
programming_languages = ['Python', 'C', 'C#', 'Java', 'JavaScript', 'Dart']

for number in range(1, 11):
    person.append({'number': number})


for i in range(len(person)):
    person[i]['name'] = names[i]
    person[i]['lastName'] = lastName
    person[i]['age'] = random.choice(ages)
    person[i]['programming_languages'] = random.sample(programming_languages, 3)

with open("..\\..\\GitHub\\json\\index.json", 'w') as archivo_nuevo:
    json.dump(person, archivo_nuevo)

print(json.dumps(person, indent=4))