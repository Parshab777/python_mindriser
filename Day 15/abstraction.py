# Abstraction = hiding the implementation details from the user


class Bike:
    clutch = False
    acc = False

    def start(self):
        clutch = True
        acc = True
        return "Bike start" #clutch and acc are unnecessary here for showing the user.


b1 = Bike()

print(b1.start())