#rithmetic operators.

#Addition

num_1= 20
num_2= 10
result=num_2+num_1
print("Addition of two numbers is:",result)

#concatenation of two strings
str_1= "Hello"
str_2= "World"
result=str_1+str_2
print("Concatenation of two strings is:",result)

#Subtraction

num_3= 20
num_4= 10
result=num_3-num_4
print("Subtraction of two numbers is:",result)

#Multiplication

num_5= 20
num_6= 10
result=num_5*num_6
print("Multiplication of two numbers is:",result)

#Division

num_7= 20
num_8= 10
result=num_7/num_8
print("Division of two numbers is:",result)

#floor division

num_9= 20
num_10= 10
result=num_9//num_10
print("Floor division of two numbers is:",result)

# Modulus

num_11= 20
num_12= 10
result=num_11%num_12
print("Modulus of two numbers is:",result)

#Exponentiation

num_13= 4
num_14= 3
result=num_13**num_14
print("Exponentiation of two numbers is:",result)

result=(num_13+num_14)**2
print("(a+b)²:",result)

#Assignment operators
"= is used to assign a value to a variable"
"+= is used to add a value to a variable and assign the result to the same variable"
"-= is used to subtract a value from a variable and assign the result to the same variable"

#comparison operators
"== is used to check if two values are equal"
"!= is used to check if two values are not equal"
"> is used to check if a value is greater than another value"
"< is used to check if a value is less than another value"
">= is used to check if a value is greater than or equal to another value"
"<= is used to check if a value is less than or equal to another value"

product_1= 20
product_2= 10
result=product_1==product_2
print("Are the products equal?",result)
result=product_1!=product_2
print("Are the products not equal?",result)
result=product_1>product_2
print("Is product_1 greater than product_2?",result)
result=product_1<product_2
print("Is product_1 less than product_2?",result)
result=product_1>=product_2
print("Is product_1 greater than or equal to product_2?",result)
result=product_1<=product_2
print("Is product_1 less than or equal to product_2?",result)

#logical operators
"and is used to check if both conditions are true"
"or is used to check if at least one of the conditions is true"
"not is used to check if a condition is false"

User_name="Anu"
User_password="Anu@656"
print(User_name=="Anu" and User_password=="Anu@656")

#identity operators
"is is used to check if two variables point to the same object in memory"

sample_1=[1,2,3]
print(sample_1)
print(id(sample_1))
a=sample_1
print(a)
sample_2=[1,2,3]
print(id(sample_2))
print(sample_2 is sample_1)

#the rule of "-5 to 256 are cached" is about integer catching

user="Anu"
print(id(user))
user_1="Anu"
print(id(user_1))
print(user is user_1)

#membership operators
"in is used to check if a value is present in a sequence"

voter_data=["Anu","Subbu","Siri"]
print("Anu" in voter_data)
print("Subbu" in voter_data)
print("Subbu" not in voter_data)
print("Siri" not in voter_data)
