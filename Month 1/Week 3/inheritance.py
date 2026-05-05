class School:
    def __init__(self, school_name, est_year):
        self.school_name = school_name
        self.est_year = est_year
    
    def __str__(self):
        return f"Name : {self.name}, Establish Year : {self.est_year}"

class Student(School):
    def __init__(self, name, age, school_name, year):
        self.name = name
        self.age = age
        super().__init__(school_name, year)
    def __str__(self):
        return f"Name : {self.name}, Age : {self.age}"
    
s = Student("Rohit", 22, "VVVP", "1990")
print(f"""
      My name is {s.name}. My age is {s.age}. 
      I'm studying in {s.school_name}. 
      Establish Year of school is {s.est_year}
      """)
