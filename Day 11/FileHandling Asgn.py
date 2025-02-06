# ask user (login or register)
# if register, ask for username and password, store username in a file
# if login, ask for username and password, and check if the username exist in the file, if yes print login, if not print something

# while True:
#     ask_user = input("Do you want to login or register or exit? ")
#     if ask_user == "register":
#         username = input("Enter your username: ")
#         password = input("Enter your password: ")
#         a = open('C:/Users/Acer/Desktop/Mindrisers/pp.txt','a')
#         a.write( username + '\n' )
#         a.close()
#         print("You have been registered successfully")
#     elif ask_user == "login":
#         username = input("Enter your username: ")
#         password = input("Enter your password: ")
#         try:
#             b = open('C:/Users/Acer/Desktop/Mindrisers/pp.txt','r')
#             if username in b.read():
#                 print("Login successful")
#             else:
#                 print("Invalid username or password")
#         except:
#             print("Invalid username or password")
#     elif ask_user == "exit":
#         print("Thank you")
#         break
#     else:
#         print("Invalid choice")








import json


def register():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    a = {username:password}

    json_a = json.dumps(a)

    f = open('C:/Users/Acer/Desktop/Mindrisers/pp.txt','a')

    f.write(json_a+'-')

    f.close()

def login():
    username = input("Enter username")
    password = input("Enter password")
    
    f = open('C:/Users/Acer/Desktop/Mindrisers/pp.txt','r')

    a = f.read().split('-')
    try:
        for i in a:
            if i != '':
                dict_i = json.loads(i)
                if username in dict_i and dict_i.get(username) == password:
                    print("Login successful")
                    return
                else:
                    print("Login Failed")
    except ValueError:
        print("Invalid username or password")




