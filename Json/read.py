import json

with open('jerry_data.json','r') as file:
    data = json.load(file)

print(data)