class Square:
    def __init__(self,side):
        self.side=side
    def Info(self):
        print(f"The area of the square is {self.side*self.side}")

class Circle:
    def __init__(self,radius):
        self.radius=radius
    def Info(self):
        print(f"The area of the circle is {3.14*self.radius*self.radius}")

sq=Square(2)
c1=Circle(2)
for i in (sq,c1):
    i.Info()