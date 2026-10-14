import time
from operator import index
from turtle import Turtle,Screen
import random
from snake import Snake


screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
snake = Snake()


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











# for turtle in snake_body:
#     x_difference = 0 - (snake_body.index(turtle)*20)
#     turtle.goto(x_difference,0)




























screen.exitonclick()