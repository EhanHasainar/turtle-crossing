import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car_manager = CarManager()
scoreboard=Scoreboard()
player.goto(0, -280)
screen.onkey(player.forward, 'w')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    scoreboard.update_scoreboard()

    car_manager.create_car() 
    car_manager.move_cars()  

    if player.ycor()>280:
        player.goto(player.xcor(), -280)
        scoreboard.increase_level()
        car_manager.level_up()
    if scoreboard.level > 3:
        scoreboard.game_over()
        game_is_on = False

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    
screen.exitonclick()

