import time
from turtle import Turtle, Screen
import random
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# Screen setup
window = Screen()
window.setup(width=900, height=900)
window.tracer(0)
window.bgcolor('blue')
window.listen()

scoreboard = Scoreboard()
snake = Snake()
food = Food()

# Keybind setup
window.onkey(fun=snake.up, key='w')
window.onkey(fun=snake.down, key='s')
window.onkey(fun=snake.left, key='a')
window.onkey(fun=snake.right, key='d')

# Game loop
game_on = True
while game_on:
    window.update()
    time.sleep(0.09)
    head_pos = snake.head.pos()
    snake.move()

    # detect food collision
    if snake.head.distance(food) < 15:
        snake.add_segment(head_pos)
        food.goto(x=random.randint(-435, 435), y=random.randint(-435, 435))
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 435 or snake.head.xcor() < -435:
        game_on = False

    if snake.head.ycor() < -440 or snake.head.ycor() > 440:
        game_on = False

    # Detect collision with tail
    for seg in snake.segments:
        if seg == snake.head:
            pass
        elif snake.head.distance(seg) < 10:
            game_on = False

window.exitonclick()