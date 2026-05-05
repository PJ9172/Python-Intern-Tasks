# Checking number is_positive or is_negative
num = int(input("Enter 1 number : "))
if num < 0:
    print("num is negative!!")
elif num > 0:
    print("num is positive!!")
else:
    print("num is zero!!")

    


# Checking Leap year
year = int(input("Enter any year : "))
if (year%4 == 0 and year%100 != 0) or (year%400 == 0):
    print(year,"is leap year!!!")
else:
    print(year,"is not a leap year!!!")
