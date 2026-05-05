class Students:
    def __init__(self,rollno, name, age):
        self.rollno = rollno
        self.name = name
        self.age = age

    def __str__(self):
        return f"Roll_no : {self.rollno} || Name : {self.name} || Age : {self.age}"
    
    