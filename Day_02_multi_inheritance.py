class Animal():
    def __init__(self,name):
        self.name = name 
        
    def eat(self):
        print(f"{self.name} is eating YUM YUJM ")
        
    def sleep(self):
        print(f"{self.name} is sleeping right now DON'T DISTRUB!!!")

class Pray(Animal):
    def flee(self):
        print(f"{self.name} is fleeing")
        

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting ")

class Rabbit(Pray):
    pass

class Fish(Pray,Predator):
    pass

class Hawk(Predator):
    pass

hawk = Hawk("Tony")
rabbit = Rabbit("Michale")

rabbit.flee()
hawk.hunt()
rabbit.sleep()
rabbit.eat()

rabbit.flee()