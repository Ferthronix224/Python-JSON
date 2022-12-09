from urllib.request import urlopen
import json

url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"
response = urlopen(url)
data_json = json.loads(response.read())
json_indent = json.dumps(data_json, indent=4)

print(json_indent)