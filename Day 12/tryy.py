# ask user (login or register)
# if register, ask for username and password, store username, password it in a file
# if login, ask for username and password, and check if the 
# username exist in the file and password is correct, if yes print login, if not print something



import json

def register():
    username = input("Enter your name: ")
    password = input("Enter your password: ")

    a = {username:password}

    f = open('C:/Users/Acer/Desktop/Mindrisers/pp.txt','a')

    json_f = json.dumps(a)

    f.write(json_f+'-')
    f.close()

def login():
    try:
        Username = input("Enter your name: ")
        password = input("Enter your password: ")
        f = open('C:/Users/Acer/Desktop/Mindrisers/pp.txt','r')
        a = f.read().split('-')
        f.close()
        for i in a:
            if i != '':
                dict_i = json.loads(i)
                if dict_i.get(Username) == password:
                    print("Login successful")
                    return
                else:
                    print("Username not available")    
    except ValueError:
        print("Invalid username or password")
        


user_choice = input("Do you want to login or register:")
if user_choice == "register":
    register()
elif user_choice == "login":
    login()
else:
    print("Invalid choice")

