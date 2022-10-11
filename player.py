from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
LEFT = 180
RIGHT = 0
DOWN = 270
UP = 90
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.seth(UP)
        self.goto(STARTING_POSITION)

    def up(self):
        self.seth(UP)
        self.forward(MOVE_DISTANCE)

    def left(self):
        self.seth(LEFT)
        self.forward(MOVE_DISTANCE)

    def right(self):
        self.seth(RIGHT)
        self.forward(MOVE_DISTANCE)

    def down(self):
        self.seth(DOWN)
        self.forward(MOVE_DISTANCE)
