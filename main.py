import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("grey")
screen.title("Frog Crossing Game")
screen.setup(width=600, height=600)

player = Player()
screen.tracer(0)
cars = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.up, "w")
screen.onkey(player.down, "s")
screen.onkey(player.left, "a")
screen.onkey(player.right, "d")


def game_run():
    game_time = 0
    level = 1
    score = 0
    game_over = False
    scoreboard.print_score(level, score)
    while not game_over:
        time.sleep(0.1)
        screen.update()
        cars.create_car(level)
        cars.move_right()

        for car in cars.car_list:
            if player.distance(car) < 15:
                game_over = True
                scoreboard.game_over(level, score)

        if player.ycor() > 290:
            level += 1
            score += 1
            scoreboard.print_score(level, score)
            player.goto(0, -280)

        game_time += 1


game_run()


screen.exitonclick()
