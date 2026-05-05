from model import Students
import json
choice = 1
students = []
while choice <= 5:
    print("""
            1. Add Student
            2. View Students
            3. Update Student
            4. Delete Student
            5. Exit
    """)
    choice = int(input("Enter your choice : "))

    # Add 
    if choice == 1:
        rollno = int(input("Enter Rollno : "))
        name = input("Enter Student Name : ")
        try:
            age  = int(input("Enter Student Age : "))
            if age < 4:
                raise Exception
        except Exception:
            print("Please Enter Valid Age!!!")
        else:
            s = Students(rollno,name,age)
            students.append(s)
            print("Student Added!!!")

            for i in range(len(students)):
                students[i] = {
                    "rollno" : students[i].rollno,
                    "name" : students[i].name,
                    "age" : students[i].age
                }

            data = {"students" : students}
            with open("data.json", "w") as f:
                json.dump(data, f, indent=4)

    # View
    elif choice == 2:
        print("All Students : \n")
        for s in students:
            print(s)

    # Update
    elif choice == 3:
        rollno  = int(input("Enter rollno to update student : "))
        name = input("Enter Student Name : ")
        try:
            age  = int(input("Enter Student Age : "))
            if age < 4:
                raise Exception
        except Exception:
            print("Please Enter Valid Age!!!")
        else:
            flag = True
            for s in students:
                if s.rollno == rollno:
                    flag = False
                    s.name = name
                    s.age = age
            if flag:
                print("Student not found with this rollno!!!\nStudent not Updated!!!")
            else:
                print("Student Updated!!!")

            for i in range(len(students)):
                students[i] = {
                    "rollno" : students[i].rollno,
                    "name" : students[i].name,
                    "age" : students[i].age
                }

            data = {"students" : students}
            with open("data.json", "w") as f:
                json.dump(data, f, indent=4)

    elif choice == 4:
        rollno  = int(input("Enter rollno to update student : "))
        flag = True
        for s in students:
            if s.rollno == rollno:
                flag = False
                students.remove(s)
                del s
        if flag:
            print("Student not found with this rollno!!!\nStudent not Deleted!!!")
        else:
            print("Student Deleted!!!")

        for i in range(len(students)):
            students[i] = {
                "rollno" : students[i].rollno,
                "name" : students[i].name,
                "age" : students[i].age
            }

        data = {"students" : students}
        with open("data.json", "w") as f:
            json.dump(data, f, indent=4)
            
    elif choice == 5:
        print("Thank You. Have a nice day!!!")
        break
    else:
        print("Invalid choice. Please enter choice again!!!")
