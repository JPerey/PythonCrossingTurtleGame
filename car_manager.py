from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.car_list = []
        self.hideturtle()
        self.x_move = MOVE_INCREMENT

    def create_car(self, level):
        while self.check_amount(level):
            new_car = Turtle()
            new_car.shape("square")
            new_car.speed(random.randint(0, 10))
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_len=2)
            new_car.goto((-280, random.randint(-250, 280)))
            self.car_list.append(new_car)

    def move_right(self):
        for i in range(len(self.car_list)):
            if self.car_list[i].xcor() > 300:
                self.move_back(i)

            new_x = self.car_list[i].xcor() + random.randint(5, 15)
            self.car_list[i].goto(new_x, self.car_list[i].ycor())

    def move_back(self, car_index):
        self.car_list[car_index].goto(-280, random.randint(-250, 280))

    def check_amount(self, level):
        if level%2 == 1 and len(self.car_list) < 5*level:
            return True

        elif level%2 == 0 and len(self.car_list) < 5*level:
            return True

        elif len(self.car_list) < 5:
            return True
        else:
            return False

