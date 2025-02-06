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