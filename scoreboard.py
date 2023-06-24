from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.score = 0
        with open('data.txt', 'r') as data:
            self.highscore = int(data.read())
        self.goto(x=-170, y=420)
        self.write(f"Score: {self.score}   High Score: {self.highscore}", font=('choco', 20, 'bold'))

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}   High Score: {self.highscore}", font=('choco', 20, 'bold'))

    def increase_score(self):
        self.score += 1
        if self.highscore < self.score:
            self.highscore = self.score
            with open('data.txt', 'w') as data:
                data.write(str(self.highscore))
        self.update_scoreboard()