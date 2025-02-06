# Encapsulation : encapsulating attributes and method in a single unit, data hiding.




# class login:
#     __email = None
#     __password = None

#     def get_detail(self,email,password):
#         self.__email = email
#         self.__password = password
        
#     def __details(self):
#         print(f"My email is {self.__email} and my password is {self.__password}")

#     def printout(self):
#         a = self.__details()
#         print(a)


# l1 = login()

# l1.get_detail('ppapa@gmail.com','123')

# print(l1.printout)





class  info:
    __name = None
    __age = None

    def get_details(self,name,age):
        self.__name = name
        self.__age = age
    
    def __intro(self):
        print(f"The name is {self.__name} and age is {self.__age}")

    def printout(self):
        a = self.__intro()
    print(a)


l1 = info()

l1.get_details("Parshab",18)

l1.printout()