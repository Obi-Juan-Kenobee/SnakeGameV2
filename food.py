import random
from turtle import Turtle


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('green')
        self.penup()
        self.goto(x=random.randint(-430, 430), y=random.randint(-430, 430))
