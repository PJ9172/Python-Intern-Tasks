import csv

# write csv
data = [
    ["id", "name", "marks"],
    [1, "Prajwal", 85],
    [2, "Rahul", 90],
    [3, "Sneha", 88]
]

with open("student.csv", mode="w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)
print("CSV file written successfully")


# Read csv
with open("student.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)


# append csv
new_data = [4, "Amit", 92]
with open("student.csv", mode="a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(new_data)
print("Data appended successfully")