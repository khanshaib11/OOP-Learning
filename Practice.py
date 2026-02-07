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


"""Question 4"""

class Rectangle:
    def __init__(self,length,width):
        self.length = length 
        self.width = width
        
    def area(self):
        return self.length * self.width
    
rec1 = Rectangle(length=10, width=20)

print(rec1.area())

"""Question 5"""

class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
    
    def describe_book(self):
        print(f"Book Title is {self.title} and its author is {self.author} ") 
        
book1 = Book(title="Acha Dost..." , author= "Bilal Ahmed khan Niazi ")  
    
book1.describe_book()


"""Question 6"""

class BankAccount:
    def __init__(self,balance):
        self.balance = balance
    
    def Deposit(self,amount):
         self.balance += amount
         
    def Withdraw(self,amount):
        if self.balance < amount:
            return False
        self.balance -= amount
        
    def Show_balance(self):
        print(f"You have {self.balance} amount of balance left, have a nice day sir!!! ")

bank1 = BankAccount(balance=0)
bank1.Deposit(100)
bank1.Withdraw(100)
bank1.Show_balance()
