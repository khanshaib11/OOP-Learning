#inheritance allows a class to inherit attributes and methods from another class 

class Animal:
    def __init__(self,name):
        self.name = name 
        self.is_alive = True
        
    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is sleeping")
        
    
class Dog(Animal):
    pass

class Cat(Animal):
    pass

class Mouse(Animal):
    pass

dog = Dog("Scooby")
mouse = Mouse("jerry")
cat = Cat("Tom")

print(dog.name)
print(dog.is_alive)

dog.eat()
dog.sleep()

print(cat.name)
cat.eat()
cat.sleep()