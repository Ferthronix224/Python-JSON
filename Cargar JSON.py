import json

with open("index.json") as archivo:
    datos = json.load(archivo)

datos[0]['name'] = 'Ferthronix'
print(json.dumps(datos, indent=4))