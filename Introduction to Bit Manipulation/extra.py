class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def display_name(self):
        print(f"{self.name} is in grade {self.grade}")

s1= Student("Rohan",9)
s2= Student("Rahul",10)

s1.display_name()
s2.display_name()