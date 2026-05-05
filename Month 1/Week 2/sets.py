# Union, Intersection, Difference
s1 = {3,7,1,9,4}
s2 = {4,8,3,1,2}
print("Union of s1 & s2 : ", s1.union(s2))
print("Intersection of s1 & s2 : ", s1.intersection(s2))
print("Difference of s1 & s2 : ", s1.difference(s2))


# Adding element in set
s1.add(6)
print("After adding 6 : ",s1)




# remove() removes the item but rise error if not available
s1.remove(6)
print("After removing 6 : ", s1)

# discard() also removes item but not rise any error if not available.
s1.discard(7)
print("After discarding 7 : ",s1)

# pop() remove random item from set
s1.pop()
print("After poping = ",s1)

# clear() empty the set
dummy = s1.copy()
dummy.clear()
print("After clearing dummy set : ", dummy)

# del deletes the set
del dummy

# Checking subset
subset = s1.union(s2)
if s1.issubset(subset):
    print("Subset!!")
else:
    print("Not subset!!")