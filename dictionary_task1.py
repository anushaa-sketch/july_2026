# Task 1: Dictionary Update
# Write Python code to add a new key-value pair to the following dictionary:
# my_dict = {'name': 'python', 'age': 25}

my_dict = {'name': 'python', 'age': 25}
my_dict['city'] = 'East godavari'
print(my_dict)

# Task 2: Dictionary Access
# Write Python code to access and print the value associated with the key 'price' in
# the following dictionary:
# Dictionary Quiz: 3
# product_info = {'name': 'Laptop', 'brand': 'Dell', 'price': 1
# 200}

product_info = {'name': 'Laptop', 'brand': 'Dell', 'price': 1200}
print(product_info['price'])

# Task 3: Dictionary Removal
# Write Python code to remove the key-value pair with the key 'city' from the
# following dictionary:
# my_dict = {'name': 'python', 'age': 30, 'city': 'Bhimavaram'}

my_dict = {'name': 'python', 'age': 30, 'city': 'Bhimavaram'}
my_dict.pop('city')
print(my_dict)

# Task 4: Dictionary Keys
# Write Python code to print all the keys present in the following dictionary:
# my_dict = {'name': 'python', 'age': 25, 'city': 'Rajahmundr
# y'}

my_dict = {'name': 'python', 'age': 25, 'city': 'Rajahmundry'}
print(list(my_dict.keys()))

# Task 5: Dictionary Values
# Write Python code to print all the values present in the following dictionary:
# my_dict = {'name': 'python', 'age': 25, 'city': 'tanuku'}

my_dict = {'name': 'python', 'age': 25, 'city': 'tanuku'}
print(list(my_dict.values()))


# Exercise 1: Dictionary Update
# Write a Python script that updates a dictionary with a new key-value pair.

my_dict = {"name": "John", "age": 25}
my_dict["city"] = "Hyderabad"
print(my_dict)

# Exercise 2: Dictionary Access
# Write a Python script that accesses and prints the value associated with a specific
# key in a dictionary.

student = {
    "name": "Anusha",
    "roll_no": 101,
    "marks": 95
}
print(student["marks"])

# Exercise 3: Dictionary Removal
# Write a Python script that removes a key-value pair from a dictionary.

my_dict = {
    "name": "John",
    "age": 25,
    "city": "Hyderabad"
}
my_dict.pop("city")
print(my_dict)

# Exercise 4: Dictionary Keys
# Write a Python script that prints all the keys present in a dictionary.

my_dict = {
    "name": "John",
    "age": 25,
    "city": "Hyderabad"
}

print(my_dict.keys())


# Exercise 5: Dictionary Values
# Write a Python script that prints all the values present in a dictionary.

my_dict = {
    "name": "John",
    "age": 25,
    "city": "Hyderabad"
}

print(my_dict.values())
