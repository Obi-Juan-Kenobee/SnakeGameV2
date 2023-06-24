from turtle import Turtle


class Snake:

    def __init__(self):
        turtle = Turtle('square')
        turtle.color('black')
        turtle.penup()
        self.segments = []
        self.segments.append(turtle)
        self.head = self.segments[0]

    def add_segment(self, position):
        new_segment = Turtle('square')
        new_segment.color('yellow')
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def move(self):
        for seg in range(len(self.segments)-1, 0, -1):
            pos = self.segments[seg - 1].pos()
            self.segments[seg].goto(pos)
        self.head.forward(15)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)