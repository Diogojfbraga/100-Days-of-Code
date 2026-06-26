from turtle import Turtle, Screen, colormode
import random

tim = Turtle()

# tim.shape('turtle')
# tim.color("red", "green")

colormode(255)

## Dashed Square


# for _ in range(4):
#     for _ in range (15):
#         tim.forward(10)
#         tim.penup()
#         tim.forward(10)
#         tim.pendown()
#     tim.right(90)

## Different Shapes

# sides = 3


# while sides < 11:
#     color = (
#                 random.randrange(0,256),
#                 random.randrange(0,256),
#                 random.randrange(0,256)            
             
#              )

#     tim.pencolor(color)
#     for side in range(sides):
#         tim.forward(100)
#         tim.right(360/sides)
#     sides += 1

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