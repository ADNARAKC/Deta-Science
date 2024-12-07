from abc import ABC, abstractmethod

class Polygon(ABC):
    
    @abstractmethod
    def calculate_area(self):
        pass

class Rectangle(Polygon):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    
    def calculate_area(self):
        return self.length * self.breadth

class Triangle(Polygon):
    
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def calculate_area(self):
        return 0.5 * self.base * self.height

class Square(Polygon):    
    def __init__(self, side):
        self.side = side
    
    def calculate_area(self):
        return self.side ** 2

class Circle(Polygon):
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return 3.14159 * (self.radius ** 2)
if __name__ == "__main__":
    shapes = [
        Rectangle(length=10, breadth=5),
        Triangle(base=8, height=6),
        Square(side=4),
        Circle(radius=7)
    ]
    
    for shape in shapes:
        print(f"The area of {shape.__class__.__name__} is: {shape.calculate_area()}")
