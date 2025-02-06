#  break - it is the condition used in while loop to stop the looping.

# a = 0
# b= 3
# while a<b:
#     print("hello")
#     a += 1
#     break

# Continue - condition use in while loop to continue the loop.

# a = 2
# b= 3
# while a<b:
#     a += 1
#     if a==3:
#       continue
#     print("A is greater")


a= int(input("Enter First Number: "))
b= int(input("Enter Second Number: "))
while True:
    operator= input("Enter operator +,-,* or / :")

    if operator == "+":
        print(a+b)
    elif operator == "-":
        print(a-b)
    elif operator == "*":
        print(a*b)
    elif operator == "/":
        print(a/b)
    else:
        print('invalid operator')
        
    user_choice = input("Do you wish to continue?(y/n)")
    if user_choice == "y":
        continue
    else:
        break
    