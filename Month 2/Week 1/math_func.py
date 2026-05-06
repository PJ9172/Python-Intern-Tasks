# Built-in Math Functions

# Min Max
x = (3,1,8,5)
print("Minimum of (3,1,8,5) : ", min(x))
print("Minimum of (3,1,8,5) : ", max(x))

# The abs() function returns the absolute (positive) value of the specified number
x = abs(-2.85)
print("Positive of -2.85 : ",x)

# The pow(x, y) function returns the value of x to the power of y
x = pow(5,2)
print("Square of 5 is : ",x)


import math

# The math.sqrt() method returns the square root of a number
x = math.sqrt(100)
print("Square Root of 100 is : ",x)

# he math.ceil() method rounds a number upwards to its nearest integer, 
# and the math.floor() method rounds a number downwards to its nearest integer, 
# and returns the result

x = math.ceil(2.4)
print("math.ceil(2.4) : ",x)
x = math.floor(2.4)
print("math.floor(2.4) : ",x)

# The math.pi constant, returns the value of PI (3.14)
x = math.pi
print("math.pi value : ",x)