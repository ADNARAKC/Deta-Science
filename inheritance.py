class Person():
    def __init__(self,name,id_number):
        self.name=name
        self.id_number=id_number
    def display(self):
        print(self.name)
        print(self.id_number)
class Employee(Person):
    def __init__(self,name,id_number,salary,post):
        self.salary=salary
        self.post=post
        Person.__init__(self,name,id_number)
    def display1(self):
        print(self.salary)
        print(self.post)

employee1=Employee("Rakesh",20,30000,"Teacher")    
employee1.display()
employee1.display1()