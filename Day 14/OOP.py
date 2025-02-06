# OOP - Object Oriented Programming

# Basic components are: Class and Objects.

# class - structure , blueprint : Keyword class is used to define class.
# Syntax:
# class class_name:
#     class attributes.

# Objects - data created using class , single class can have multiple objects, variables 
# in class are called attributes and methods are functions inside class.
# Syntax:
# object_name = class_name()

# Constructor - Special method which is used to initialize the state of an object.
# Syntax:
# def __init__(self, arguments):
# Here, self automatically passed by python.
# It is used to initialize the state of an object.
# It is automatically called when an object is created from a class and it cannot be called again once.




class Person:
    def __init__(self,name,age):         
        self.name = name
        self.age = age
    def intro (self):
        print(f"Name is {self.name} and age is {self.age}")

person1 = Person('Ram','25') 

person2 = Person('Shyam','18') # Creating an object of the class Person while calling the class we use ().

print(person1.name)
print(person1.age)
print(person2.name)
print(person2.age)


print(person1.intro()) # Calling the method intro() of the class Person using the object person1.

# create class named car
# car has attribute model and color
# one method
# 2 objects of that class.


class car:
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def intro(self):
        print(f"The car is {self.model} in {self.color} color")

car1 = car('BMW', 'Red')
car2 = car('Lambo','Blue')

print(car1.model)
print(car1.color)
print(car2.model)
print(car2.color)
car1.intro()
car2.intro()