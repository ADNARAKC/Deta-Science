class Cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(f"I am a cat my name is{self.name}. My age is {self.age}")
    def Sound(self):
        print("Meow")

class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(f"I am a dog my name is{self.name}. My age is {self.age}")
    def Sound(self):
        print("Bark")

cat=Cat("Tommy",3)
dog=Dog("Bunny",4)

for animal in(cat,dog):
    animal.Sound()
    animal.info()