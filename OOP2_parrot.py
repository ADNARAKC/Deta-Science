class Parrot:
    species="Bird"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def sing(self,song):
        return f"{self.name} sings {song}"
    
    def dance(self,dance):
        return f"{self.name} dances {dance}"

    def printInfo(self):
        return f"{self.name} is {self.age} years old"
p1=Parrot("Tommy",2)
p2=Parrot("Mittu",3)
print(p1.sing("Twinkle"))
print(p2.sing("Star"))
print(p1.dance("Rock"))
print(p2.dance("Hip Hop"))
print(p1.printInfo())
print(p2.printInfo())
