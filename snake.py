from snake_classes import *
from turtle import Screen

game_on = True
snake = Snake()
food = Food()
screen = Screen()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(snake.move_up, "Up")
screen.onkeypress(snake.move_down, "Down")
screen.onkeypress(snake.move_left, "Left")
screen.onkeypress(snake.move_right, "Right")


while game_on:
    snake.move()

    # controlla se il serpente mangia il cibo
    if snake.snake_element[0].distance(food) < 15:
        food.refresh()
        snake.add_segment()
        scoreboard.refresh_score()

    # controlla se il serpente supera i bordi della mappa
    if snake.snake_element[0].xcor() > 285 or snake.snake_element[0].xcor() < -285 or snake.snake_element[0].ycor() > 285 or snake.snake_element[0].ycor() < -285:
        game_on = False

    # controlla se il serpente non mangia se stesso
    for item in snake.snake_element[1:]:
        if item.distance(snake.snake_element[0]) < 10:
            game_on = False

scoreboard.game_over()