from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass
    
    
    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def go(self):
        print("you drive the car")
        
    def stop(self):
        print("you stop the car ")
        
class Motorcycle(Vehicle):
    def go(self):
        print("you ride the motocycle")
        
    def stop(self):
        print("you stop the motocycle ")
    
class Boat(Vehicle):
    def go(self):
        print("You sail the boat")
    def stop(self):
        print("you stop the boat")
        
        
        
        
car = Car()
car.stop()
car.go()

boat = Boat()
boat.stop()
boat.go()