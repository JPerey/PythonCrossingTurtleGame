from turtle import Turtle



class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.hideturtle()
        self.goto(0, 280)
        self.FONT = ("Courier", 24, "normal")

    def print_score(self, level, score):
        self.clear()
        self.goto(0, 280)
        self.write(f"Level: {level} Score: {score}", True, align= "center", font=self.FONT)

    def game_over(self, level, score):
        self.clear()
        self.goto(0, 150)
        self.write(f"GAME OVER \n"
                   f"Level: {level} Score: {score}", True, align="center", font=self.FONT)


