"""
The try block test a block of code for errors.

The except block handle the error.

The else block execute code when there is no error.

The finally block execute code, regardless of the result of the try- and except blocks.
"""

try:
    x = int(input("Enter number to divide by 10: "))
    print(10 / x)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input")

print("---------------------------")

# Custom exceptions
class InvalidAgeError(Exception):
    pass
age = int(input("Enter age: "))
if age < 18:
    raise InvalidAgeError("Age must be 18+")

print("---------------------------")

# finally
try:
  print(a)
except Exception:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

print("---------------------------")

# else
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")