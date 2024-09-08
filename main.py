from turtle import Turtle,Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
snake=Snake()
food=Food()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(snake.up,"w")
screen.onkey(snake.down,"s")
screen.onkey(snake.right,"d")
screen.onkey(snake.left,"a")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detection of food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extent()

        scoreboard.increase_score()

    #collision with  the wall
    if snake.head.xcor() >283 or snake.head.xcor() <-283 or snake.head.ycor() >283 or snake.head.ycor() <- 283:
        scoreboard.reset()
        snake.reset()

    #detect collison with tail
    for segement in snake.segments:
        if segement == snake.head:
            pass
        elif snake.head.distance(segement) <10:
            scoreboard.reset()
            snake.reset()
            












screen.exitonclick()



