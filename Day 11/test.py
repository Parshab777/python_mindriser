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

            print(f"Your Balance is {float(user_balance[username])}")

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