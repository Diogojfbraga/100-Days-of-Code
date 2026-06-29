from turtle import Turtle, Screen, colormode
import random

tim = Turtle()

colormode(255)

## Random Walk

run = True

tim.shape('arrow')

direction_options = [0, 90, 180, 270]
tim.pensize(5)

while run:
    direction = random.choice(direction_options)
    color = (
                random.randrange(0,256),
                random.randrange(0,256),
                random.randrange(0,256)            
             
             )

    tim.pencolor(color)
    tim.setheading(direction)
    tim.forward(20)
    tim.speed(0)


screen = Screen()
screen.exitonclick()