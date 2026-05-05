# Min Max of list
l1 = [3,1,7,4,7,9,5]
print("Maximum of list : ", max(l1))
print("Minimum of list : ", min(l1))

# Sorting
l1.sort()
print("Ascending order : ", l1)
l1.sort(reverse=True)
print("Decending order : ", l1)

# Removing Duplicates
s1 = set(l1)
l1 = list(s1)
print("After removing duplicates : ",l1)


# Counting Even & Odd
numbers = input("Enter list : ").split()
even_count = odd_count = 0
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
    if numbers[i]%2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even numbers Count of given list : ", even_count)
print("Odd numbers Count of given list : ", odd_count)

# print in reverse order 
numbers.reverse()
print("In reverse order : ",numbers)

# Without built-in function
print("Without Built-in function : ", numbers[::-1])


# string to list
s = "python"
l = list(s)
print(l)