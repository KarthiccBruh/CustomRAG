import json

with open('Resume.json', 'r') as file:
    data = json.load(file)
    data=str(data)
print(data)
