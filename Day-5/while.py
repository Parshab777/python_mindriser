# while loop : multi lined Statement, conditional statement
# if the while condition is true, while vitra vako statements haru run huni vayo.
# while should contain logics that converts the true condition into false.
# Syntax:
# while True:
#     print("Hello World")


# a = 10
# b = 20

# while a < b:
#     print("A is smaller")
#     a += 2

# Create a program that takes an integer input from the user and counts down to 0, displaying each number.

# num = int(input("Enter the  number"))

# while num >= 0:
#     print(num)
#     num -= 1



# Ask the user for a number and use a while loop to determine if it's a prime number.

# num = int(input("Enter a number to check if it's prime: "))

# if num <= 1:
#     print(f"{num} is not a prime number.")
# else:
#     divisor = 2
#     while divisor < num:
#         if num % divisor == 0:
#             print(f"{num} is not a prime number.")
#             break
#         divisor += 1
#     else:
#         print(f"{num} is a prime number.")



# Write a program that calculates the factorial of a user-provided number using a while loop.

num = int(input("Enter the number to find the factorial of:"))
factorial = 1   
if num < 0:
    print("Factorial is not defined for negative number")
else:
    while num > 1:
        factorial = factorial * num
        num -= 1
    print(f"The factorial is {factorial}")