# Ecommerce program

# register
# login
# usertype= seller, buyer
# seller:
#     product add
#     list your product 
#     delete
# buyer:
#     list all the products
#     buy product
#     billing

# logout

# ask user (login or register)
# if register, ask for username, usertype and password, store username, usertype, password it in a file
# if login, ask for username and password, and check if the username exist in the file and password is correct,
# if the logged in user, usertype is seller, show options(product add (name,quantity, description, price)
#     list your product 
#     delete)
# if the logged in users' usertype is buyer, show options(list product, buy produt, optional:billing)
# login crediential,not match validation error
# in a loop
import json;


def register():
    username = input("Enter your username: ")
    usertype = input("Enter whether you are a seller or a buyer: ")
    password = input("Enter your password: ")

    a = {"username" : username,
        "usertype" :usertype,
        "password": password}
    
    json_a = json.dumps(a)

    f = open('C:/Users/Acer/Desktop/Mindrisers/pp.txt','a')

    f.write(json_a+'-')

    f.close()

def login():
    username = input("Enter your name")
    password = input("Enter your password")
    print(f"My username is {username} and my password is {password}")

    f = open('C:/Users/Acer/Desktop/Mindrisers/pp.txt','r')

    a = f.read()

    list_a = a.split('-')
    
    for i in list_a:
        if i != '':
            dict_i = json.loads(i)
            if dict_i.get('username') == username and dict_i.get('password') == password:
                usertype = dict_i.get('usertype').lower()
    while True:            
        if usertype == 'seller':

            user_choice = input('''Seller options:
               1. Add Products 
               2. List product
               3. Delete product
               4. Exit''')
            if user_choice == "1":
                add_product(username)
            elif user_choice == "2":
                list_product(username)
            elif user_choice == "3":
                delete_product(username)
            elif user_choice == "4":
                break
            else:
                print("Invalid Choice")
                break    
        elif usertype == 'buyer':
            user_choice = input('''Buyer options:
                            1.List products
                            2.Buy Products
                            3.Exit>>>''')
            if user_choice == '1':
                product_list()
            elif user_choice == '2':
                buy_product()
            elif user_choice == '3':
                break
            else:
                print("Invalid Choice")
                break
        else:
            print("Invalid User Type")
            break

def add_product(seller):
    name = input("Enter product name: ")
    quantity = (input("Enter  the quantity required: "))
    description = input("Enter the decription of your product: ")
    price = (input("Enter the price of your product: "))

    a = {"name":name,
          "Quantity":quantity,
          "description":description,
          "price":price,
          "seller":seller}
          
    json_a = json.dumps(a)

    f = open("Product.txt","a")

    f.write(json_a+'-')

    f.close()

    print("Your product has been added.")

def list_product(sellername):
    
    f = open("Product.txt","r")

    a = f.read()

    list_a = a.split('-')

    for i in list_a:
        if i != '':
            dict_i = json.loads(i)
            if dict_i.get('seller') == sellername:
                print(f"Your products are {dict_i.get('name')}")


def delete_product(name):
    product = input("Enter the product you want to delete: ")

    f = open("Product.txt","r+")

    a = f.read().split('-')

   
    for i in a:
        if i != '':
            dict_i = json.loads(i)
            if dict_i.get('seller') == name and dict_i.get('name') == product:
                dict_i.clear()
    f = open("Product.txt","")
    f.write(dict_i)
    f.close()
    print("Your product has been deleted.")


def product_list():

    f = open('Product.txt','r')

    a = f.read()

    list_a = a.split('-')

    for i in list_a:
        if i != '':
            # or we can directly print(i).
            dict_i = json.loads(i)
            print(f"The products available are {dict_i.get('name')}") #either we can do this.


def buy_product():
    buy  = input("Enter the product you want to buy: ")
    quantity = int(input("Enter the quantity you want to buy: "))
    price = int(input('Enter the amount you have:'))
    f = open('Product.txt','r')

    a = f.read().split('-')

    f.close()
    
    for i in a:
        if i != '':
            dict_i = json.loads(i)
            if dict_i.get('name') == buy and int(dict_i.get('price')) <= price:
                price = dict_i.get('price') * quantity
                print(f"Your total price is: {price}")
                print(dict_i)
            else: 
                print("Insufficient Balance")
          



    
choice = input("Do you want to login or register: ").lower()
if choice == "register":
    register()
elif choice == "login":
    login()
else:
    print("Invalid input")