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


