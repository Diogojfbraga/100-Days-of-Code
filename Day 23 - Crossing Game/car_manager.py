COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from turtle import Turtle
import random
class CarManager:
    def __init__(self):
        
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def generate_cars(self):
        # Only create a car sometimes, not every loop
        random_chance = random.randint(1, 6)

        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.color(random.choice(COLORS))

            # Start from the right side of the screen
            random_y = random.randrange(-240, 260, 20)
            new_car.goto(300, random_y)

            self.all_cars.append(new_car)
        

    def car_move(self):
        for car in self.all_cars:
            new_x = car.xcor() - self.car_speed
            new_y = car.ycor() 
            car.goto(new_x, new_y)

    
    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT

    
