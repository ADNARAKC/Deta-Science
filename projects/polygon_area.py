class Shape:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"This is a {self.name}.")

class Rectangle(Shape):
    def __init__(self, length, width):

        super().__init__("Rectangle")
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)
class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)
        self.name = "Square"  

rect = Rectangle(5, 3)
sq = Square(4)
rect.display()
print(f"Area: {rect.area()}")
print(f"Perimeter: {rect.perimeter()}") 

print("\n")

sq.display()
print(f"Area: {sq.area()}")
print(f"Perimeter: {sq.perimeter()}") 
