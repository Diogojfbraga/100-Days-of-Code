from turtle import Turtle, Screen, colormode
import random

tim = Turtle()

colormode(255)

# Different Shapes
sides = 3

while sides < 11:
    color = (
                random.randrange(0,256),
                random.randrange(0,256),
                random.randrange(0,256)            
             
             )

    tim.pencolor(color)
    for side in range(sides):
        tim.forward(100)
        tim.right(360/sides)
    sides += 1


screen = Screen()
screen.exitonclick()