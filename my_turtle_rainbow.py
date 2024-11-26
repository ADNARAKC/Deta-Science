import turtle
import random
my_turtle=turtle.Turtle()
s = turtle.Screen()
colors = ['red','blue','green','cyan','purple','yellow']
s.bgcolor("Black")
my_turtle.speed('fastest')
my_turtle.hideturtle()
while True:
    for x in range(200):
        my_turtle.pencolor(random.choice(colors))
        my_turtle.width(x/100+1)
        my_turtle.fd(x)
        my_turtle.left(59)
    my_turtle.right(239)
    for x in range(200, 0, -1):
        my_turtle.pencolor("black")
        my_turtle.width(x/100+7)
        my_turtle.right(59)
turtle.done()

