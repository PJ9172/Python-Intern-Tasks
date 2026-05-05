# adding numbers
data = input("Enter 2 numbers : ").split()
num1 , num2 = int(data[0]), int(data[1])
print("Addition is : ", num1+num2)


# Area of circle
redius = int(input("Enter the redius : "))
print("Area of circle is : ", 3.14 * redius**2)

# Checking Even & Odd
num = int(input("Enter 1 number : "))
if num%2 == 0:
    print(num, "is Even!!")
else:
    print(num, "is Odd!!")
