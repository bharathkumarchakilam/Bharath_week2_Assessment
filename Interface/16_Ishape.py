#importing the abstractmethod from abc module
from abc import ABC, abstractmethod

#interface to calculate the area
class IShape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass
    
#derived class rectangle from IShape
class Rectangle(IShape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def calculate_area(self):
        return self.length * self.width

class Circle(IShape):
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return 3.14 * self.radius * self.radius

shape_type = input("Enter shape type (Rectangle, Circle): ")

if shape_type == "Rectangle":
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    shape = Rectangle(length, width)
elif shape_type == "Circle":
    radius = float(input("Enter radius: "))
    shape = Circle(radius)
else:
    print("Invalid shape type")
    exit()

print(f"Area: {shape.calculate_area()}")
