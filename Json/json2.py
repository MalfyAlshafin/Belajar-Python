import json

with open("json_file.json", "r") as file:
    python_dict = json.load(file)

print(python_dict)