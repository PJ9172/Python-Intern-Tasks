#  Accessing elements from 2 to 6
t = (4, 8, 2 ,5, 7, 1, 9, 3)
print("Slicing from 2nd to 6th : ", t[2:7])


# Typecasting 
l = list(t)
l[0] = 6
t = tuple(l)
print(t)



# Counting element appearence
t = (4, 5, 1, 4, 1, 5, 1, 8)
d = {}
for i in t:
    d[i] = t.count(i)

print("Tuple is : ",t)
print("Count : ",d)


# Adding tuples
t1 = (1,2,3,4)
t2 = (5,6,7,8)
t3 = t1+t2
print("Adding tuples : ",t3)