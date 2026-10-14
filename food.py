from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid = 0.5, stretch_len = 0.5)
        self.color("green")
        self.speed("fastest")

        food_spawn_x = random.randrange(-280,280)
        food_spawn_y = random.randrange(-280, 280)

        self.goto(food_spawn_x,food_spawn_y)

    def spawn_different_location(self):
        food_spawn_x = random.randrange(-280, 280)
        food_spawn_y = random.randrange(-280, 280)

        self.goto(food_spawn_x, food_spawn_y)

