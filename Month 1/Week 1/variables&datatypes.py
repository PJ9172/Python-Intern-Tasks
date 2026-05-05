# Getting the Types.
print("-------------------------------")
print("Getting the Types")
name = "Prajwal"
age  = 22
height = 5.7
is_married = False

print("Datatype of name : ", type(name))
print("Datatype of age : ", type(age))
print("Datatype of height : ", type(height))
print("Datatype of isMarried : ", type(is_married))




# Multiple Variable assign Multiple values
print("-------------------------------")
print("Assigning Multiple Variables With Multiple Value")
a, b, c = "one", "two", "three"
print("a =",a,"\t","b =",b,"\t","c =",c)




# Multiple Variable assign Single values
print("-------------------------------")
print("Assigning Multiple Variables With single Value")
a = b = c = "Mango"
print("a =",a,"\t","b =",b,"\t","c =",c)




# Unpacking collection in variables
print("-------------------------------")
print("Unpacking collection in variables.")
numbers_list = ["one", "two", "three"]
a, b, c = numbers_list
print("a =",a,"\t","b =",b,"\t","c =",c)
