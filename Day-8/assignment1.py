# todo:
# create a dictionary that contains username and password, username as key and password as value
# ask user for their username and password
# check if the username and password exist in the dictionary
# if yes print("Welcome")
# if no print("Invalid username or password")



id_list = {"parshab":"123","kunwar":"678","Ram":"456"}

user_name = input("Enter your username: ")

password = input("Enter your password: ")
try:
    if user_name in id_list and id_list.get(user_name) == password:
        print("Welcome")
    else:
        print("Invalid")
except:
    print("Invalid input")

# Exception handle
# simple calculator
# get  2 numbers from user
# get a operator from user(+,-,*,/)
# if operator is + then add two numbers and show the output
# if operator is - then subtract two numbers and show the output
# if operator is * then multiply two numbers and show the output
# if operator is / then divide two numbers and show the output
# To add, multiply or Divide the numbers.


# a = input("Enter any number")

# b = input("Enter any number")

# try:
#     c = a + b

#     d= a * b

#     e= a / b
#     print(c)
#     print(d)
#     print(e)
# except:
#     print("Invalid Input")

# # # To do:
# a= input("Enter First Number: ")
# b= input("Enter Second Number: ")
# operator= input("Enter operator +,-,* or / :")
# try:
#     if operator == "+":
#         print(a+b)
#     elif operator == "-":
#         print(a-b)
#     elif operator == "*":
#         print(a*b)
#     elif operator == "/":
#         print(a/b)
#     else:
#         print('invalid operator')
# except:
#     print("Invalid input")   
