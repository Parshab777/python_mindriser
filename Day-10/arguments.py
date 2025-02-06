# default argument : used in case that if the user does not provide the argument then it will take the default value.

def student(firstname = "firstname" , lastname = "lastname" , age = 18):
    print("Hello")
    print(f"My name is {firstname} {lastname} {age}")
first = "Hari"
last = "bahadur"
age = 10
student(first , last ,age)

# args(arguments) - (*args_name) is used to defined it, multiple data or value can be passed, give output in the form of tuple.

def numbers(a,b,c):
    print(a,b,c)  #this is only for limited parameters.
numbers(1,2,3)


def numbers(*args):
    print(args)
    for i in args:
        print(i)
numbers('ram','shyam','gopal')



def add(*args):
    a = 0
    for i in args:
        a += i
    print(a)
add(8,10,11,12,13)


# kwargs(Keyword arguments) - (**) used to define kwargs,
# multiple keyword arguments accept garxa, accept dictionary data type, methods 
# of dictionary is used to access and manipulate kwargs.



def person(**kwargs):
    print(kwargs)
    for key in kwargs.values():
        print(key)
person(name = "ram" , age = 20, phone = 98989889, address = "dhng")


# Positional argument, args and kwargs : follows this sequence.
def person(age, *a, **kwargs):
    print(a)
    print(f"Age : {age}")
    print(kwargs)
person("25","Ram", "ktm", "989283498384", dob = "200", home = "Dhangadhi")



def add(*args):
    sum = 0
    for i in args:
        sum += i
    print(sum)
add(1,2,2,3,3,4,4,5,5,5,5)


def person_detail(*args,**kwargs):
    for arg in args:
        print(arg)
    for key , value in kwargs.items():
        print(f"{key}: {value}")
person_detail("Parshab","Kunwar",Location = "Dhangadhi", House_Number = 123)





