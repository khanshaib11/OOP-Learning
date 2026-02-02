class Car:
    def __init__(self,model,year,color,for_sale):
        self.model = model 
        self.year = year 
        self.color = color 
        self.for_sale = for_sale
        
    def drive(self):
        print(f"You drive the {self.color} {self.model}")
        
    def stop(self):
        print(f"you stop the {self.color} {self.model}")
        
    def describe(self):
        print(f"{self.year} {self.color} {self.model}")
    

car1 = Car("Lambo",2026,"red",True)
car2 = Car("Ferrari",2026,"yellow",False)
car3 = Car("Bugati",2026,"pink",True)

print(car3.model)   
print(car3.year)
print(car3.color)
print(car3.for_sale)

car1.drive()
car2.stop()
car3.drive()
car1.describe()
car2.describe()
    