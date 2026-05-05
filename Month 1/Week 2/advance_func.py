# lambda :  Square a number
sqrt = lambda x : x**2
print("Square of 4 is : ",sqrt(4))

# map() : Square all elements in a list
l = [1,2,3,4,5]
sqrt = list(map(lambda x: x**2, l))
print("Square of list : ",sqrt)

# filter() : Extract even numbers from a list
even_list = list(filter(lambda x: x%2 == 0, l))
print("Filtered Even list : ",even_list)

#  zip() : Combine two lists into pairs
names = ["Rohit","Rajesj","Raj"]
age = [20,22,19]
ziped_dict = dict(zip(names,age))
print("Zipped dict is : ",ziped_dict)