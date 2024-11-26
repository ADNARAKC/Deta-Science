import turtle
my_turtle=turtle.Turtle()
s = turtle.Screen()
s.bgcolor("Black")
for i in range(3): 
    my_turtle.pencolor("Cyan")
    my_turtle.fd(100)
    my_turtle.left(120)

my_turtle.penup()
my_turtle.fd(-100)
my_turtle.pendown()

for j in range(4):
    my_turtle.pencolor("Purple")
    my_turtle.fd(100)
    my_turtle.left(90)

my_turtle.right(90)
my_turtle.penup()
my_turtle.fd(100)
my_turtle.pendown()

for j in range(6):
    my_turtle.pencolor("Lightgreen")
    my_turtle.fd(100)
    my_turtle.left(60)
turtle.done()

