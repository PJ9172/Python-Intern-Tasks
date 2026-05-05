# #  Even Odd list
# even = []
# odd = []
# for i in range(1,26):
#     if i%2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)

# print("Even list : ",even)
# print("Odd list : ",odd)



# # Sum of first N numbers
# n = int(input("Enter a number : "))
# sum = 0
# for i in range(1, n+1):
#     sum += i
# print(f"Sum of first {n} is : ", sum)



# Printing list
fruits = ["apple", "banana", "cherry"]
for i in fruits:
    print(i)

print("-----------------------------------")
# Reverse printing list
print("Printing in reverse order : ")
for i in range(-1,-(len(fruits)+1) ,-1):
    print(fruits[i])



# Addition of given numbers
total_sum = 0
number = 0

while number >= 0:
    total_sum += number
    number = int(input("Enter a number (negative to stop): "))

print(f"The total sum is: {total_sum}")
