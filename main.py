import time
from operator import index
from turtle import Turtle,Screen
import random

from food import Food
from snake import Snake
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.onkey(key = "Up" ,fun = snake.up)
screen.onkey(key = "Down", fun = snake.down)
screen.onkey(key = "Left", fun = snake.left)
screen.onkey(key = "Right", fun = snake.right)
screen.listen()


game_running = True
while game_running:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()



    #When the snake eats one of the food it will grow
    if snake.head.distance(food) < 15:
        food.spawn_different_location()
        scoreboard.increase_score()








# for turtle in snake_body:
#     x_difference = 0 - (snake_body.index(turtle)*20)
#     turtle.goto(x_difference,0)




























screen.exitonclick()