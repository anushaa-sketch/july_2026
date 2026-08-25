# Task 1: Add Function
# Write a Python function named add that takes two arguments a and b and
# returns their sum.

def add(a, b):
    return a + b
print(add(10, 20))

# Task 2: Square Function
# Write a Python function named square that takes a number x as input and
# returns its square.

def square(x):
    return x * x
print(square(5))

# Task 3: Factorial Function
# Write a Python function named factorial that takes a positive integer n as
# input and returns its factorial.

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact
print(factorial(5))

# Task 4: Maximum Function
# Write a Python function named maximum that takes a list of numbers as input and
# returns the maximum value in the list.

def maximum(numbers):
    return max(numbers)
print(maximum([10, 25, 5, 40, 15]))

# Task 5: Reverse Function
# Write a Python function named reverse that takes a string s as input and
# returns its reverse.

def reverse(s):
    return s[::-1]
print(reverse("python"))

# Task 6: Check Prime Function
# Write a Python function named is_prime that takes a positive integer n as input
# and returns True if n is prime, otherwise False .

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
        return True
    print(is_prime(7))


# Task 7: Fibonacci Function
# Write a Python function named fibonacci that takes a positive integer n as
# input and returns the n th Fibonacci number.    

def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        a, b = b, a + b
        return a
    print(fibonacci(7))


# Task 8: Palindrome Function
# Write a Python function named is_palindrome that takes a string s as input and
# returns True if s is a palindrome, otherwise False .    

def is_palindrome(s):
    return s == s[::-1]
print(is_palindrome("madam"))

# Task 9: Sum of Squares Function
# Write a Python function named sum_of_squares that takes a list of numbers as
# input and returns the sum of the squares of those numbers.

def sum_of_squares(numbers):
    total = 0
    for num in numbers:
        total = total + num * num
        return total
    print(sum_of_squares([1, 2, 3, 4]))


# Task 10: Average Function
# Functions Quiz: 3
# Write a Python function named average that takes a list of numbers as input and
# returns the average value.    

def average(numbers):
    return sum(numbers) / len(numbers)
print(average([10, 20, 30, 40, 50]))