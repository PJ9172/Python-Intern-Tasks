import json

data = {
    "students": [
        {"id": 1, "name": "Prajwal", "marks": 85},
        {"id": 2, "name": "Rahul", "marks": 90}
    ]
}

with open("student.json", "w")as f:
    json.dump(data, f, indent=4)

with open("student.json") as f:
    reader = json.load(f)
for s in reader["students"]:
    print(s)

# append 
with open("student.json") as f:
    data = json.load(f)
    data["students"].append({"id": 3, "name": "Sneha", "marks": 88})

with open("student.json", "w") as f:
    json.dump(data, f, indent=4)