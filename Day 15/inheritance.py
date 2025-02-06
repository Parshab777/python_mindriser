# # Inheritance : Parent Class and Child class.
# # PArent Class : should be defined inside the parenthesis of the child class
# # Child class can use the attrtibutes and methods of parent class.
# # Child class can have their own attributes and methods as well.
# # Parents Class ko methods and attributes can be overridden in child class.

# class car:
#     model = None
#     color = None


#     def get_car_details(self,model,color):
#         self.model = model
#         self.color = color

# # c1 = car()
# # c1.get_car_details("Toyota", "Red")
# # print(c1.model)
# # print(c1.color)








# class EV(car):
#     speed = None

#     def get_speed(self,speed):
#         self.speed = speed


#     def get_car_details(self,model):
#         self.model = model

# ev1 = EV()

# ev1.get_car_details("Tesla")

# ev1.get_speed("20000")
# print(ev1.model)

# # print(ev1.color)

# print(ev1.speed)


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

