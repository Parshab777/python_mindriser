a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
operator = input("Enter operator +,-,* or / :")
c = 10
if operator == "+":
    print(a+b)
    if a == 10:
        print("It is equal to 10")
elif operator == "-":
    print(a-b)
    if a == 10:
        print("It is equal to 10")
elif operator == "*":
    print(a*b)
    if a == 10:
        print("It is equal to 10")
elif operator == "/":
    print(a/b)
    if a == 10:
        print("It is equal to 10")
else:
    print('invalid operator')