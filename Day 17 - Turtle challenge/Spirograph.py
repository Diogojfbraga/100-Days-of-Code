from turtle import Turtle, Screen, colormode
import random


tim = Turtle()

colormode(255)
tim.speed(0)


def draw_spirograph(size_of_gap):



    for _ in range(int(360 / size_of_gap)):

        color = (
                    random.randrange(0,256),
                    random.randrange(0,256),
                    random.randrange(0,256)            
                    
                    )
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)
        tim.pencolor(color)
        tim.pensize(1)


draw_spirograph(10)


    # tim.right(5)


screen = Screen()
screen.exitonclick()