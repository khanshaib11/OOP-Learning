"""Classes & Objects (FOUNDATION)"""
"""Question 1"""
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def introduce(self):
        print(f"Hi, my name is {self.name} and I am {self.age} years old ")
        
per1 = Person(name= "Khan", age =24)

per1.introduce()
      
"""Question 2"""        
class Car:
    def __init__(self,brand,year):
        self.brand = brand
        self.year = year 
        
car1 = Car(brand="Ford", year=2024)  

car2 = Car(brand="Raptor", year=2025)  

print(car1.brand)
print(car1.year)

"""Question 3"""

class Student:
    def __init__(self,name,marks):
        self.name = name 
        self.marks = marks
        
    def is_passed(self):
        if self.marks >= 50:
            return True
        else:
            return False
        
       
s1 = Student("Ali", 72)
print(s1.is_passed())

