class Shape:
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side * self.side

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height

shape_type = input("Enter shape type (Square, Triangle): ")

if shape_type == "Square":
    side = float(input("Enter side length: "))
    shape = Square(side)
elif shape_type == "Triangle":
    base = float(input("Enter base length: "))
    height = float(input("Enter height length: "))
    shape = Triangle(base, height)
else:
    print("Invalid shape type")
    exit()

print(f"Area: {shape.area()}")
