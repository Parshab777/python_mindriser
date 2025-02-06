# function : Like variables, but stores block of codes, multi-lined , reusability, clean coding.


#  Syntax:

# def function_name():
     # code to be executed
# For function call we simply use,
# function_name()



# def hello():
#     print("Hello, World!")
#     print("Hello, World!")
#     print("Hello, World!")

# hello()




# # # local Variable: variable defined inside function is called local variable, can only accessed withing the function.
# # # global variable: variable defined outside function is called global variable and can be accessed in any function we want.
# # for modifying the global variable inside the function we use the global keyword.
# glo = "global"
# print(glo)    #this is global variable.
# def hello():
#     global glo
#     a = "abc"   #this is local variable.
#     print(a)
#     print(glo)

# a = 10
# def sum():
#     print(a)
#     print(a*5)

# sum()





# # Variables used in paranthesis of function are called parameters.
# # data send to function is called arguments.
# # positional_argument - order of arguments matters.def student(firstname , lastname):
# print("Hello")
# print(f"My name is {firstname} {lastname}")
# first = "Hari"
# Last = "bahadur"
# student(first , Last)

# Keyword Argument: keyword is used to assign the value when calling the function.
# def student(firstname , lastname):
#     print("Hello")
#     print(f"My name is {firstname} {lastname}")
# first = "Hari"
# Last = "bahadur"
# student(firstname=first , lastname=Last)


