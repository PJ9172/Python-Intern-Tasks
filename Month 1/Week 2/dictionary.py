# Finding highest marks
student = {
    "Rohit" : 500,
    "Rahul" : 450,
    "Rajesh" : 550
}
max = 0
for m in student.values():
    if m > max:
        max = m  
for key, value in student.items():
    if max == value:
        print("Highest marks student is : ", key)




# The pop() method removes the item with the specified key name:
student.pop("Rajesh")
print("After poping Rajesh : ",student)

# Adding Rajesh again
student["Rajesh"] = 550

# The popitem() method removes the last inserted item
student.popitem()
print("After poping items : ",student)

# The del keyword removes the item with the specified key name
del student["Rahul"]

# The clear() method empties the dictionary
student.clear()
print("After clearing the dictionary : ",student)

# The update() method will add or update dictionary with given item in argument.
student.update({"Rohit" : 500})


# Copying dictionary
dummy = student.copy()
print("Copied dictionary : ",dummy)

# Count frequency of each character in a string.
s = "naman"
d = {}
for ch in s:
    d[ch] = s.count(ch)
print("Given string : ",s)
print("Count of each character in string is : ",d)


# Merging 2 dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged_dict = dict1 | dict2
print("Merged dictionary : ",merged_dict)


# Inverting dictionary 
inverted = {v : k for k,v in dict1.items()}
print("Inverted dictionary : ",inverted)