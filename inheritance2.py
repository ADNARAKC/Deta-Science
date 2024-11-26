class Person():
    def __init__(self,firstname,lastname):
        self.firstname=firstname
        self.lastname=lastname
    def display(self):
        print(self.firstname,self.lastname)
class Student(Person):
    def __init__(self,firstname,lastname,year):
        super().__init__(firstname,lastname)
        self.graduationyear=year

p1=Student("Rohit","Sarmah",2013)
p1.display()
print(p1.graduationyear)