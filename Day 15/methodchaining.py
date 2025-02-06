class burger:
    def bun(self):
        print("Bun")
        return self
    def patty(self):
        print("Patty") 
        return self
    def sauce(self):
        print("sauce") 
        return self

burger1 = burger()

# normal method call:
burger1.bun()
burger1.patty()
burger1.sauce()

# Method chaining
burger1.bun().patty().sauce() 