# todo:
# class named person, attributes name and age, method introduction
# class name student, it inherits person class, attributes class and roll number, method get_class_roll
# create object of student class, print out introduction, class and roll number

class Person:
    name = None
    age = None

    def introduction(self,name,age):
        self.name = name
        self.age = age
        print(f"Name is {self.name} and Age is {self.age}")

class student(Person):
    classs = None 
    Rollno = None

    def get_class_roll(self,classs,Rollno):
        self.classs = classs
        self.Rollno = Rollno
        print(f"Class is {self.classs} and Roll no is {self.Rollno}")

person1 = Person()
person2 = student()
person1.introduction("Parshab","18")
person2.get_class_roll("12","21")





class Person:
    def __init__(self,name,age,networth):
        self.name = name
        self.age = age
        self.networth = networth

    def Info(self):
        print(f"THe name is {self.name} who is {self.age} years old having the networth of {self.networth}")

person1 = Person("Parshab","18","1000")

person1.Info()


class Car:
    name = None
    model = None

    def intro(self,name,model):
        self.name = name
        self.model = model
        print(f"Name is {self.name} and Model is {self.model}")
class Bike(Car):
    name = None
    color = None
    def intro(self,name,color):
        self.name = name
        self.color = color
        print(f"The name is {self.name} and color is {self.color}")
car1 = Car()
car2 = Car()
bike1 = Bike()
car1.intro("BMW",'Offroading')
car2.intro("Lambo",'Off')
bike1.intro('Kawasaki',"Racing")


