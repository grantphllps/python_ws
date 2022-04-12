class Doge:
    
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting")

    def roll_over(self):
        print(f"{self.name} rolled over")

my_doge = Doge('Willie',6)

print(my_doge.name)

my_doge.roll_over()