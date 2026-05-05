# Classes Objects Constructors Encapsulation

class Student:
    standard = '7th'    # Class property
    def __init__(self, name, age, email):
        self.name = name
        self.__age = age    # Instance property
        self.email = email
    def display_info(self):
        print(f"Standard : {self.standard}, Name : {self.name}, Age : {self.__age}, Email : {self.email}")

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be positive")

s1 = Student("PJ",22,"pj@gmail.com")
s2 = Student("Mosin",22,"mosin@gmail.com")
s3 = Student("Rohit",24,"rohit@gmail.com")
s1.display_info()
s2.display_info()
s3.display_info()
s1.set_age(18)
print("After changing age of s1 : ",s1.get_age())

# deleting email property of s1
del s1.email





# The __str__() method is a special method that controls 
# what is returned when the object is printed
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"Name : {self.name}, Age : {self.age}"

p1 = Person("Raj", 26)
print(p1)


