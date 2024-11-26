from abc import ABC, abstractmethod
class Animal(ABC):
    def move(self):
        pass
class Human(Animal):
    def move(self):
        print("I can walk and run")
class Snake(Animal):
    def move(self):
        print("I can crawl")
class Dog(Animal):
    def move(self):
        print("I can walk in four legs")
class Bird(Animal):
    def move(self):
        print("I can fly")

h1=Human()
h1.move()

s1=Snake()
s1.move()

d1=Dog()
d1.move()

b1=Bird()
b1.move()