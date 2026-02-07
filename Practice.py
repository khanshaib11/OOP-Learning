"""Classes & Objects (FOUNDATION)"""
"""Question 1"""
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def introduce(self):
        print(f"Hi, my name is {self.name} and I am {self.age} years old ")
        
        
"""Question 2"""        
class Car:
    def __init__(self,brand,year):
        self.brand = brand
        self.year = year 
        
car1 = Car(brand="Ford", year=2024)  

car1 = Car(brand="Raptor", year=2025)  

"""Question 3"""


