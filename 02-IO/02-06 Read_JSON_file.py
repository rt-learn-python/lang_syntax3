import json

from pprint import pprint

data = json.load(open('example.json'))

pprint(data)

data["maps"][0]["id"]
data["masks"]["id"]
data["om_points"]
