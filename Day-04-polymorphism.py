"""two ways to acheive polymorphism 
1> inheritance
2> duck typing
"""
from abc import ABC, abstractmethod
class Shape():
    
    @abstractmethod
    def area(self):
        pass

class Triangle(Shape):
    def __init__(self,base,height):
        self.base = base 
        self.height = height
    
    def area(self):
        return self.base * self.height  * 0.5
    
    
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
    
class Square(Shape):
    def __init__(self,side):
        self.side = side

    def area(self):
        return self.side ** 2
        
class Pizza(Circle):
    def __init__(self,radius,topping):
        self.radius = radius 
        self.topping = topping  
        
#list of shapes as this are shapes
shapes = [Circle(4), Square(5), Triangle(6,7), Pizza(15,"Pepperoni")]


for shape in shapes:
    print(f"{shape.area()}cm²")