from urllib.request import urlopen
import json

url = "https://ferthronix224.github.io/json/"
response = urlopen(url)
data_json = json.loads(response.read())
json_indent = json.dumps(data_json, indent=4)

# for i in range(len(data_json)):
#     if 'JavaScript' in data_json[i]['programming_languages']:
#         print(data_json[i]['name'], end=', ')