# Exercise 1: Sum of Squares
# Write a Python program that calculates and prints the sum of the squares of
# numbers from 1 to 5 using a
# for loop

sum = 0
for i in range(1, 6):
    sum = sum + (i * i)
print("Sum of squares:", sum)


# Exercise 2: Countdown
# Write a Python program that uses a
# while loop to print a countdown from 5 to 1.

i = 5
while i >= 1:
    print(i)
    i = i - 1

# Exercise 3: Multiplication Table with Nested For Loop
# Write a Python program to print the multiplication table for a user-specified
# number using a nested for loop.  

num = int(input("Enter a number: "))
for i in range(1, 2):
    for j in range(1, 11):
      print(num, "x", j, "=", num * j)

# Exercise 4:
# Write a Python program that uses a "for" loop to find the sum of all even
# numbers between 0 and 10 (inclusive).

sum = 0
for i in range(0, 11):
    if i % 2 == 0:
        sum = sum + i
        print("Sum of even numbers:", sum)

# Exercise 5:
# Calculate the sum of all numbers from 1 to a given number        

n = int(input("Enter a number: "))
sum = 0
for i in range(1, n + 1):
    sum = sum + i
print("Sum:", sum)


# Exercise 6:
# Display numbers from a list using loop

numbers = [10, 20, 30, 40, 50]
for i in numbers:
    print(i)

# Exercise 7:
# Display numbers from -10 to -1 using for loop  

for i in range(-10, 0):
    print(i)

# Exercise 8:
# Write a Python program to print the cube of all numbers from 1 to a given
# number    

n = int(input("enter a number: "))
for i in range(1, n + 1):
    print("Cube of", i, "=", i ** 3)