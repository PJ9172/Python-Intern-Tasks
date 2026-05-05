# # Checking Prime number
# def is_prime(n):
#     flag = True
#     for i in range(2,n):
#         if n%i == 0 :
#             flag = False
#             break
#     if flag:
#         print("Number is prime!!!")
#     else:
#         print("Number is not prime!!!")

# is_prime(4)


# # Calculate Factorial
# def factorial(n):
#     if n < 0:
#         return "Invalid input"
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result

# print(factorial(5))  


# # Sum of given list
# def sum_of_list(data):
#     sum = 0
#     for i in data:
#         sum += i
#     return sum

# data = input("Enter the list of numbers : ").split()
# for i in range(len(data)):
#     data[i] = int(data[i])
# print("Addition of given list : ",sum_of_list(data))



# # Additio of default arguments

# def add_default(a=10, b=20):
#     return a+b
# print("Addition of default arguments : ",add_default())


# # Function which return multiple values
# def get_user_data():
#     name = "Rohit"
#     age = 22
#     email = "rohit@gmail.com"
#     return name, age, email 

# user_name, user_age, user_email = get_user_data()

# print(f"{user_name} is {user_age} years old & email is {user_email}")




# ----------------------------------------------------------------------------------------------


# Accepts N number of arguments and returning their sum.
def sum(*args):
    sum = 0
    for i in args:
        sum += i
    return sum
print("Sum of N arguments : ", sum(3,1,2,4,5))

# Accepts keyword arguments and prints key-value pairs
def key_value(**kwargs):
    for key, value in kwargs.items():
        print(f"key : {key}, value : {value}")
key_value(name="Rohit", age=22, email="rohit@gmail.com")

# Function using *args and **kwargs together
def combine_func(*args, **kwargs):
    print("Positional arguments are : ",args)
    print("Keyword arguments are : ",kwargs)
combine_func(1,2,3,4,name="Rohit", age=22)