# Exception handle
# make it function based calculator
# get  2 numbers from user
# get a operator from user(+,-,*,/)
# if operator is + then add two numbers and show the output
# if operator is - then subtract two numbers and show the output
# if operator is * then multiply two numbers and show the output
# if operator is / then divide two numbers and show the output


num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))


operator = input("Enter operator (+,-,*,/): ")

if operator == "+":
    def add (a,b):
        c = a + b
        print(f"The sum is: {c}")
    add(num1,num2)
elif operator == "-":
    def subtract(a,b):
        d = a - b
        print(f"The difference is: {d}")
    subtract(num1,num2)
elif operator == "*":
    def multiply(a,b):
        e = a*b
        print(f"The product is: {e}")
    multiply(num1,num2)
elif operator == "/":
    def divide(a,b):
        if b == 0:
            print("Enter the number other than 0")
        else:
            f = a/b
            print(f"The quotient is: {f}")
    divide(num1,num2)
else:
    print("Invalid operator")




num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))


operator = input("Enter operator (+,-,*,/): ")

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide (a,b):
    return a/b


if operator == "+":
    print(f"The sum is : {add(num1,num2)}")
if operator == "-":
    print(f"The subtraction is : {sub(num1,num2)}")
if operator == "*":
    print(f"The multiply is : {multiply(num1,num2)}")
if operator == "/":
    print(f"The divide is : {divide(num1,num2)}")
else:
    print("Invalid Operator")



while True:
   def add(a,b):
      return a + b
      
   def sub(a,b):
      return a - b
      
   def mul(a,b):
      return a * b 
      
   def div(a,b):
      return a / b  
   try:
      a = int(input("Enter first number: "))
      b = int(input("Enter second number: "))
   
      operator = input("Enter operator (+,-,*,/): ")
   
      if operator == "+":
         result = add(a,b)
         print(f"The result of {a} + {b} is {result}.")
      elif operator == "-":
         result = sub(a,b)
         print(f"The result of {a} - {b} is {result}.")
      elif operator == "*":
         result = mul(a,b)
         print(f"The result of {a} * {b} is {result}.")
      elif operator == "/":
         if b == 0:
            print("Division by 0 is not allowed.")
         result = div(a,b)
         print(f"The result of {a} / {b} is {result}.")
      else:
         print("Invalid operator. Please use one of +, -, *, /.")
   
   except ValueError:
      print("Invalid input. Please enter a number.")
   except NameError:
      print("name error")
      
   user_choice  = input("Do you want to continue (y/n): ")
   if user_choice == "y":
      continue
   elif user_choice == "n":
      break
   else:
      print("Invalid choice. Please enter y or n.")
   




while True:
    def add(a,b):
        return a+b
    def sub(a,b):
        return a-b
    def multiply(a,b):
        return a*b
    def divide(a,b):
        return a/b
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter another number: "))

        operator = input("Give the operator '+','-','*','/': ")
        if operator == "+":
            result = add(num1,num2)
            print(f"The result of {num1} + {num2} is {result}.")
        elif operator == "-":
            result = sub(num1,num2)
            print(f"The result of {num1} + {num2} is {result}.")
        elif operator == "*":
            result = multiply(num1,num2)
            print(f"The result of {num1} + {num2} is {result}.")
        elif operator == "/":
            result = divide(num1,num2)
            print(f"The result of {num1} + {num2} is {result}.")
    except ValueError:
        print("Enter accurate value: ")
    except NameError:
        print("Name error")
    except ZeroDivisionError:
        print("Enter number other than 0")
    user_choice = input("Do you want to continue (y/n): ")
    if user_choice == "y":
        continue
    elif user_choice == "n": 
        break
    else:
        print("Invalid choice. Please enter y or n.")

