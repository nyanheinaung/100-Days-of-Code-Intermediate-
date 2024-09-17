from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("Black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.snake_head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.total_score += 1
        scoreboard.update_scoreboard()

    # Detect collision with wall
    if (-280 > snake.snake_head.xcor() or snake.snake_head.xcor() > 280 or
            -280 > snake.snake_head.ycor() or snake.snake_head.ycor() > 280):
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail
    # If snake head collides with any segment in the tail:
    for segment in snake.snake_body[1:]:
        if snake.snake_head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
