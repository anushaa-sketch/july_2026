# 1.Write a Python program to calculate the area of a rectangle using the given
# formula: area = length * width . Take the values of length and width as inputs fromthe user
length = float(input("Enter length: "))
width = float(input("Enter width: "))

area = length * width

print("Area of rectangle =", area)

# 2.Write a Python program to demonstrate incrementing and decrementing a variable.
num = int(input("Enter a number: "))

num += 1
print("After increment:", num)

num -= 1
print("After decrement:", num)

# 3.Write a Python program to convert temperature from Celsius to Fahrenheit. The
# formula for conversion is: F = (C * 9/5) + 32 . Take the temperature in Celsius asinput from the user.
celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32

print("Temperature in Fahrenheit =", fahrenheit)

# 4.Write a Python program to calculate the simple interest given the principalamount, rate, and time (in years).
principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time (in years): "))

simple_interest = (principal * rate * time) / 100

print("Simple Interest =", simple_interest)

# 5.Write a Python program to concatenate two strings and display the result. The
# strings should be taken as input from the user.
string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

result = string1 + " " + string2

print("Concatenated String:", result)

# 6.Write a Python program to convert a distance from kilometers to miles.
kilometers = float(input("Enter distance in kilometers: "))

miles = kilometers * 0.65678

print("Distance in miles =", miles)