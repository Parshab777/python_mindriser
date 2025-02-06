# Polymorphism:

class Dog:
    def move(self):
        return "Dog is Barking"
class Bird:
    def move(self):
        return "Bird is Flying"
class Fish:
    def move(self):
        return "Fish is Fishing"


dog = Dog()
bird = Bird()
fish = Fish()


print(dog.move())
print(bird.move())
print(fish.move())