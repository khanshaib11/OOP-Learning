#ducking a duck
class Animal():
    alive = True
    
    
class Dog(Animal):
    def speak(self):
        print("WOOF!")
        
class Cat(Animal):
    def speak(self):
        print("MEOW!")
        
class Cars():
    alive = True
    def speak(self):
        print("HONK!") 
               
animals = [Dog(), Cat(),Cars()]

for animal in animals:
    animal.speak()
    print(animal.alive)