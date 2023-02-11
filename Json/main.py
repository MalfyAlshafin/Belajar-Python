import json

data_dict = {
    "employees":[
        {
            "firstName":"John",
            "lastName":"Doe"},
        {
            "firstName":"Anna",
            "lastName":"Smith"
        },
        {
            "firstName":"Peter",
            "lastName":"Jones"
        }
    ]
}

data = json.dumps(data_dict)

with open("data.json", "w") as file:
    json.dump(data, file, indent=4)

print(json.dumps(data_dict,indent=4))