#import json
#import os

# with open('file.json','r') as file:
#     data = json.load(file)

# print(data)

#print(os.getcwd())

import json
import os

# Print the current working directory
print("Current Working Directory:", os.getcwd())

# Check if the file exists
file_path = 'file.json'
if not os.path.isfile(file_path):
    print(f"File not found: {file_path}")
else:
    with open(file_path, 'r') as file:
        data = json.load(file)
    print(data)

