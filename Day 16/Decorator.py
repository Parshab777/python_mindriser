# Decorator : @ followed by the function name is used to define a decorator.
# decorator must be placed one step above the function that is to be sent in decorator.
# using decorator is alternative for called a function like [function(arko_function)]



# def program(function):
#     print("Before the function is called")
#     function()
#     print("End of code")

# # @function_name.
# @program
# def hello():
#     print("Hello, world!")
#     print("Hello, world!")
#     print("Hello, world!")
#     print("Hello, world!")

# # hello()

# # # Using decorator we have to print the absolute positive integer.
# def div(a,b):

#     return num()


# @div
# def num(x,y):
#     x = int(input("enter the number:"))
#     y = int(input("enter the number:"))

#     if x > 0 and y > 0:
#         if x > y:
#             print(f"Divison is :{x/y}")
#         else:
#             print("Division cannot be performed")
#     else:
#         print("Please enter positive number")



# def ensure_integer_division(func):
#     def wrapper(a, b):
#         result = func(a, b)
#         if a < b:
#             return 1  # Ensuring the result is not a decimal
#         return result
#     return wrapper

# @ensure_integer_division
# def divide(a, b):
#     if a % b == 0: 
#         return a // b 
#     else:
#         a / b  # Normal division

# # Test cases
# print(divide(2, 10))  # Output: 1
# print(divide(10, 2))  # Output: 5



# def divison(func):
#     def wrapper(a,b):
#         result = func(a,b)
#         if a < b:
#             return 1
#         return result
#     return wrapper
        
# @divison
# def printout(a, b):
#     if a % b == 0:
#         return a // b
#     else:
#         return a / b

# printout(10,3)
# printout(10,2) 






def actual_divison(func):
    def wrapper(a,b):
        result = func(a,b)
        if a < b:
            return 1
        return result
    return wrapper


@actual_divison
def output(a,b):
    if a % b == 0:
        return a // b
    else: 
        return a / b

print(output(5,10))
print(output(10,2))


    