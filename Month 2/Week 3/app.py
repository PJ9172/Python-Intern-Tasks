from flask import Flask, jsonify, request

app = Flask(__name__)

students = [
        {"rollno" : 1,"name" : "Rohit"},
        {"rollno" : 2,"name" : "Rahul"}
    ]

@app.route("/")
def home():
    return "Hello!!!"

# GET API
@app.route("/students", methods=['GET'])
def get_students():
    global students
    return jsonify(students)

# POST API
@app.route("/add_students", methods=['POST'])
def add_students():
    data = request.get_json()
    global students
    students.append(data)
    print("new student list : ",students)
    return {"message" : "Students added successfully"}

# PUT API
@app.route("/update/<int:rollno>", methods=['PUT'])
def update_student(rollno):
    data = request.get_json()
    print("befor update : ",students)
    for s in students:
        if s["rollno"] == rollno:
            s["name"] = data[0]["name"]
    print("Updated list : ",students)
    return {"message" : "Student updated successfully"}

# DELETE API
@app.route("/delete/<int:rollno>", methods=['DELETE'])
def delete_student(rollno):
    global students
    students = [s for s in students if s["rollno"] != rollno]
    print("After deletion : ",students)
    return {"message" : "Student deleted successfully"}

if __name__ == "__main__":
    app.run(debug=True)