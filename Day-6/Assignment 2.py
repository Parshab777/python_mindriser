# ask user for their age
#  if user age is greater then or equal to 18, print they are eligible for license,
#  ask if they have any vehicle, if yes print some remark, if no print some remarks,

#  if user age is smaller than 18, print they are not eligible for license, ask if they have want any vehicle, 
# if yes ask what is it, if no  print some remark


age = int(input("Enter your age:"))

if age >= 18:
    print("You are eligible for license")
    ask_user = input("Do you have any vehicle?(y/n)")
    if ask_user == 'y':
        print("Drive by following the safety measures")
    else:
        print("You should get one")

elif age < 18:
    print("Not eligible for license")
    ask_user2 = input(("Do you want to buy any vehicle?(y/n)"))
    if ask_user2 == "y":
        ask = input("Which vehicle you want")
    else:
        print("You are under-age you should not buy the vehicle now")