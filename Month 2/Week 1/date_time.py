import datetime

# Creating datetime object
x = datetime.datetime(2026, 4, 29)
print("Created object : ",x)

# Current time
x = datetime.datetime.now()
print("Current DateTime : ",x)

# The datetime object has a method strftime(), 
# it takes one parameter, "format", to specify the format of the returned string

# Year
print(f"Short Version of year : {x.strftime("%y")}")
print(f"Full version of year : {x.strftime("%Y")}")
print("Another way x.year : ",x.year)

# Month
print(f"Short Version of month : {x.strftime("%b")}")
print(f"Full version of month : {x.strftime("%B")}")
print(f"Month as a number : {x.strftime("%m")}")
print("Another way x.month : ",x.month)

# Day
print(f"Weekday, short version : {x.strftime("%a")}")
print(f"Weekday, full version : {x.strftime("%A")}")
print(f"Weekday as a number 0-6 : {x.strftime("%w")}")
print(f"Day of month 01-31 : {x.strftime("%d")}")

# Hour
print(f"Hour 00-24 : {x.strftime("%H")}")
print(f"Hour 00-12 : {x.strftime("%I")}")

# AM/PM
print(f"AM/PM : {x.strftime("%p")}")

# Min
print(f"Minute 00-59 : {x.strftime("%M")}")

# Sec
print(f"Second 00-59 : {x.strftime("%S")}")
