"""
Day 01: Introduction to Classes and Objects
==============================================
OOP Concept: Classes are blueprints, Objects are instances of those blueprints

Think of it like this:
- Class = Cookie Cutter (the template)
- Object = Actual Cookie (made from the template)
"""

# ============================================
# LESSON 1: Creating Your First Class
# ============================================

class Dog:
    """A simple class representing a dog."""
    
    # This is the CONSTRUCTOR - it runs when you create an object
    def __init__(self, name, age):
        # 'self' refers to the object being created
        # These are ATTRIBUTES (properties of the object)
        self.name = name
        self.age = age
    
    # This is a METHOD (function that belongs to the class)
    def bark(self):
        return f"{self.name} says: Woof!"
    
    def describe(self):
        return f"{self.name} is {self.age} years old."


# ============================================
# LESSON 2: Creating Objects (Instances)
# ============================================

# Creating objects from our Dog class
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

# Using the objects
print("=== My Dogs ===")
print(dog1.describe())  # Output: Buddy is 3 years old.
print(dog1.bark())      # Output: Buddy says: Woof!

print(dog2.describe())  # Output: Max is 5 years old.
print(dog2.bark())      # Output: Max says: Woof!


# ============================================
# PRACTICE: Try creating your own class!
# ============================================

class Student:
    """Practice: A class representing a student."""
    
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    def study(self):
        return f"{self.name} is studying hard!"
    
    def get_info(self):
        return f"Student: {self.name}, Grade: {self.grade}"


# Create a student object - try changing the values!
my_student = Student("Ilyas", "A")
print("\n=== Student Info ===")
print(my_student.get_info())
print(my_student.study())


# ============================================
# KEY TAKEAWAYS:
# ============================================
# 1. class ClassName:  -> Defines a new class
# 2. def __init__(self):  -> Constructor, runs when object is created
# 3. self.attribute = value  -> Creates an attribute
# 4. def method(self):  -> Creates a method (function)
# 5. object = ClassName()  -> Creates an instance (object)

print("\n[OK] Day 01 Complete! You learned about Classes and Objects!")
