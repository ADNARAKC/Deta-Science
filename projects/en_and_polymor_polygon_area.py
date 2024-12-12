class Shape:
    def __init__(self, name):
        self._name = name  

    def get_name(self):
        return self._name

    def display(self):
        print(f"This is a {self.get_name()}.")

    def area(self):
        raise NotImplementedError("Subclasses must implement this method")

    def perimeter(self):
        raise NotImplementedError("Subclasses must implement this method")

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__("Rectangle")  
        self._length = length  
        self._width = width

    def get_length(self):
        return self._length

    def set_length(self, length):
        self._length = length

    def get_width(self):
        return self._width

    def set_width(self, width):
        self._width = width
    def area(self):
        return self.get_length() * self.get_width()

    def perimeter(self):
        return 2 * (self.get_length() + self.get_width())

class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length) 
        self._name = "Square" 
rect = Rectangle(5, 3)
sq = Square(4)
rect.display()
print(f"Area of Rectangle: {rect.area()}")   
print(f"Perimeter of Rectangle: {rect.perimeter()}")

print("\n")

sq.display()
print(f"Area of Square: {sq.area()}")  
print(f"Perimeter of Square: {sq.perimeter()}")  
