from turtle import Turtle

ALIGNMENT = "center"
FONT=("Arial", 20, "italic")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.score = 0
        with open("data.txt") as data:
            self.highscore=int(data.read())
        self.hideturtle()
        self.update_scoreboard()
# updating the score board
    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"SCORE: {self.score} HIGH SCORE:{self.highscore}", align=ALIGNMENT, font=FONT)
# Resets the snake coordinates
    def reset(self):
        if self.score>self.highscore:
            self.highscore=self.score
            with open("data.txt",mode="w") as data:
                data.write(f"{self.highscore}")
        self.score=0
        self.update_scoreboard()
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score +=1
        self.update_scoreboard()
