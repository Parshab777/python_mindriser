# ask user (login or register)
# if register, ask for username and password, store username, password it in a file
# if login, ask for username and password, and check if the username exist in the file and password is correct
# if yes, show them three option (check balance, add balance, withdraw balance)
# if user choise is check print the initial balance, if balance is 0 of no data, print they have to add balance first
# if add ask user the amount to add and add it with the balance, data lai next file ma save, {username:added_balance}
# if withdraw, ask the amount, check if the amount is greater than the balance, if the yes break but if no subtract the amount with the balance
# if username and password doesnot match, print some you have register first.
import json

def add_balance(username):
   amount = input("Enter the amount to add: ")
   a = {username:amount}
   json_a = json.dumps(a)

   f = open('useraccount.txt','a')
  
   f.write(json_a+'-')
   f.close()
   print("Your amount has been added:")

def check_balance(username):

   f = open('useraccount.txt','r')
   
   a = f.read().split('-')

   total = 0

   for i in a:
      if i != '':
         dict_i = json.loads(i)
         if username in dict_i:
            total += int(dict_i.get(username))
            print("Your current balance is: ",total)


# def withdraw_balance(username):
#    amount = int(input("Enter the amount to withdraw:"))
   
#    f = open('useraccount.txt','r')
   
#    a = f.read().split('-')
#    f.close()
#    for i in a:
#       dict_i = json.loads(i)
#       if i != '':
#          total_amount = int(dict_i.get(username))
#          if amount <= total_amount:
#             total_amount -= int(amount)
#             print("Your money has been withdrawn.")
#             print("Your current balance is: ",total_amount)
#             b = open('useraccount.txt','a')
#             c = {username:total_amount}
#             json_c = json.dumps(c)
#             b.write(json_c)
#             b.close()
#          else:
#             print("You dont have sufficient balance.")
         





                  
def register():
   username = input("Enter username:")
   password = input("Enter password:")
   
   a = {username:password}
   
   json_a = json.dumps(a) #converts dictionay into json format
   f = open('C:/Users/Acer/Desktop/Mindrisers/pp.txt','a')
   f.write(json_a+'-')
   f.close()

def login():
   is_login = False
   username = input("Enter username:")
   password = input("Enter password:")
   
   f = open('C:/Users/Acer/Desktop/Mindrisers/pp.txt','r')
   a = f.read().split("-")
   f.close()
   for i in a:
      if i != '':
         dict_i = json.loads(i)
         if dict_i.get(username) == password:
            print("Login success")
            is_login = True


   if is_login:
      ask_user = input(''' 1. Add Balance
         2. Show Balance
         3. Withdraw Balance>>>''')
      if ask_user == "1":
         add_balance(username)
      elif ask_user == "2":
         show_balance(username)
      elif ask_user == "3":
         withdraw_balance(username)
      else:
         print("Invalid Choice")
         



choice = input("Register/Login: ").lower()
if choice == "register":
   register()
elif choice == "login":
   login()