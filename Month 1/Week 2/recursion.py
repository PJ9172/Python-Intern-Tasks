# Factorial using recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
print("Factorial of 5 : ",factorial(5))

# Fibonacci series
def fibo(a,b,n):
    if n > 0:
        a,b = b, a+b
        print(b)
        n -= 1
        fibo(a,b,n)
a,b = 0,1
print(a)
print(b)
fibo(a,b,n=3)

# sum of digits
def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return (n%10) + sum_of_digits(n//10)
print("Sum of digits : ",sum_of_digits(123))

# reverse string
def reverse_str(str):
    if len(str) <= 1:
        return str
    
    return str[-1] + reverse_str(str[:-1])
str = "Hello"
print("Befor reverse : ",str)
print("After reverse : ",reverse_str(str))