import json

# JSON string
json_string = '{"name": "John", "age": 30}'

# Parse JSON string to Python dictionary
data = json.loads(json_string)
print(data['name'])  # Output: John

# Convert Python dictionary to JSON string
json_data = json.dumps(data)
print(json_data)  # Output: {"name": "John", "age": 30}
