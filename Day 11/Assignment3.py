# Accounting Task

# create a dictionary that stores username as key and password as value

# create a dictionary that stores username and balance as key and value respectively {"ram":"100000"}

# ask user for username and password, check if it exist in the dictionay

# if yes,(login) show them three option (check balance, add balance, withdraw balance)

# if user choise is check print the initial balance

# if add ask user the amount to add and add it with the balance

#  if withdraw, ask the amount, check if the amount is greater than the balance, if the yes break but if no subtract the amount with the balance

# if username and password doesnot match, print some remark.



# dictionary1 = {"parshab":"123","Ram": "234","Hari":"678"}

# dictionary2 = {"parshab":"100000","Ram":"50000","Hari":"200000"}


# username = input("Enter your username: ")


# password = input("Enter your password: ")


# if username in dictionary1 and dictionary1[username] == password:

#     print("Login Successfull")


#     while True:

#         print( "Show following Options:")

#         print( "1. Check Balance")

#         print( "2. Add balance")

#         print( "3. Withdraw Balance")        

#         user_choice = input("Enter your choice:")


#         if user_choice == 1:

#             print(f"Your current balance is {dictionary2[username]}")

#         elif user_choice == 2:

#             amount = float(input("Enter the amount to add: "))

#             try:

#                 if amount > 0:

#                     dictionary2[username] += amount
#                 else:

#                     print("Amount must be greater than 0")

#             except ValueError:

#                 print("Invalid input")

#         elif user_choice == 3:

#             amount = float(input("Enter the amount to withdraw: "))

#             try:

#                 if amount > dictionary2[username]:

#                     print("Insufficient balance")
#                 else:

#                     dictionary2[username] -= amount

#             except ValueError:

#                 print("Invalid Data")
#         else:

#             print("Invalid Input")
# else:

#     print("Username doesnot exist")




# user_credentials = {

#     "ram": "password123",

#     "sita": "secure456",

#     "hari": "mypassword789"

# }


# user_balances = {

#     "ram": 100000,

#     "sita": 75000,

#     "hari": 50000

# }


# # Ask user for username and password

# username = input("Enter your username: ")

# password = input("Enter your password: ")


# # Check if username and password match

# if username in user_credentials and user_credentials[username] == password:

#     print("\nLogin successful!\n")
    

#     while True:

#         print("Choose an option:")

#         print("1. Check Balance")

#         print("2. Add Balance")

#         print("3. Withdraw Balance")

#         print("4. Logout")


#         choice = input("Enter your choice (1-4): ")


#         if choice == "1":

#             # Check balance

#             print(f"Your current balance is: {user_balances[username]}\n")

#         elif choice == "2":

#             # Add balance

#             try:

#                 amount = float(input("Enter amount to add: "))

#                 if amount > 0:

#                     user_balances[username] += amount

#                     print(f"Amount added successfully! New balance is: {user_balances[username]}\n")
#                 else:

#                     print("Amount must be greater than zero.\n")

#             except ValueError:

#                 print("Invalid input. Please enter a valid amount.\n")

#         elif choice == "3":

#             # Withdraw balance

#             try:

#                 amount = float(input("Enter amount to withdraw: "))

#                 if amount > user_balances[username]:

#                     print("Insufficient balance.\n")

#                 elif amount > 0:

#                     user_balances[username] -= amount

#                     print(f"Withdrawal successful! Remaining balance is: {user_balances[username]}\n")
#                 else:

#                     print("Amount must be greater than zero.\n")

#             except ValueError:

#                 print("Invalid input. Please enter a valid amount.\n")

#         elif choice == "4":

#             # Logout

#             print("\nLogged out successfully. Goodbye!")

#             break
#         else:

#             print("Invalid choice. Please try again.\n")
# else:

#     print("\nInvalid username or password. Please try again.")


# Accounting Task

# create a dictionary that stores username as key and password as value

# create a dictionary that stores username and balance as key and value respectively {"ram":"100000"}

# ask user for username and password, check if it exist in the dictionay

# if yes,(login) show them three option (check balance, add balance, withdraw balance)

# if user choise is check print the initial balance

# if add ask user the amount to add and add it with the balance

#  if withdraw, ask the amount, check if the amount is greater than the balance, if the yes break but if no subtract the amount with the balance

# if username and password doesnot match, print some remark.



user_credentials = {

    "parshab":"123",

    "ram":"456"

}


user_balance={

    "parshab":12345,

    "ram":100000

}


username = input("Enter your username: ")

password = input("Enter your password: ")


def sum (a,b):

    return a+b
     

def subtract(a,b):
    return a-b


if username in user_credentials and user_credentials[username] == password:

   print("\nWelcome to the banking system!") 

   while True:

        print("Show Following Options:")

        print("1.Check Balance")

        print("2.Add Balance")

        print("3.Withdraw Balance")

        print("4.Logout")

        user_choice = input("Enter your choice: ")

        if user_choice == "1":

            print(f"Your Balance is {user_balance[username]}")

        elif user_choice == "2":

            amount = int(input("Enter the amount to add: "))

            if amount > 0:

                user_balance[username] = sum(user_balance[username], amount)

                print(f"Your new balance is {user_balance[username]}")
            else:

                    print("Amount must be greater than 0.")

        elif user_choice == "3":

            amount = int(input("Enter the amount to withdraw: "))

            if amount < user_balance[username]:

                user_balance[username] = subtract(user_balance[user], amount)

                print(f"Your new balance is: {user_balance[username]}")
            else:

                print("You don't have that much money in your account.")

        elif user_choice == "4":

            print("You logged out successfully")
        else:

            print("Invalid choice. Please try again.")
else:

    print("Invalid username or password")


