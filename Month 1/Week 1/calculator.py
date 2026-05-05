data = input("Enter 2 numbers for Calculation : ").split()
num1 , num2 = int(data[0]), int(data[1])
operator = input("Enter the operator symbol like (+,-,*,/) : ")

if operator == "+":
    print("Addition is:", num1 + num2)
elif operator == "-":
    print("Subtraction is:", num1 - num2)
elif operator == "*":
    print("Multiplication is:", num1 * num2)
elif operator == "/":
    print("Division is:", num1 / num2)
else:
    print("Invalid operator")
    
    