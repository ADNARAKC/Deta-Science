class Srudent:
    def __init__(self,name,grade,city):
        self.name=name
        self.grade=grade
        self.city=city
    def printInfo(self):
        return f"{self.name} from grade {self.grade} is from {self.city}"

o1=Srudent("Rahul","IX","Guwahati")
o2=Srudent("Kaushik","X","Tezpur")
print(o1.printInfo())
print(o2.printInfo())