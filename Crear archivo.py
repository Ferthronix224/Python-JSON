import json

person = [{'name': 'Fernando'}, {'name': 'Adolfo'}]

person[0]['lastName'] = 'Alonso'
person[1]['lastName'] = 'Arciga'

with open("name.json", 'w') as archivo_nuevo:
    json.dump(person, archivo_nuevo)
print(json.dumps(person, indent=4))