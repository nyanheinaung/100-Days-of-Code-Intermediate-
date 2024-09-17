import time
from turtle import Screen
from ui import UI, SCREEN_HEIGHT, SCREEN_WIDTH
from scoreboard import Scoreboard
from paddle import Paddle, PADDLE_LENGTH
from ball import Ball

screen = Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("pong")
screen.tracer(0)

ui = UI()
scoreboard = Scoreboard()
player1 = Paddle(1)
player2 = Paddle(2)
ball = Ball()

screen.listen()
screen.onkeypress(player1.move_up, "e")
screen.onkeypress(player1.move_down, "d")
screen.onkeypress(player2.move_up, "Up")
screen.onkeypress(player2.move_down, "Down")

# if paddle misses ball
# p1 score
scoreboard.update_score(1)
# p2 score
scoreboard.update_score(0)

game_is_on = True
wall = SCREEN_HEIGHT//2 - 20
player_line = SCREEN_WIDTH//2 - 40

while game_is_on:
    time.sleep(0.05)
    ball.move()

    # Check collision with walls
    if ball.ycor() > wall or ball.ycor() < -wall:
        ball.bounce(ball.heading(), "wall")

    # Check collision with paddle 1
    if ball.xcor() > -player_line and player1.distance(ball) < 21*PADDLE_LENGTH/2 and 135 < ball.heading() < 225:
        ball.bounce(ball.heading(), "player1")

    # Check collision with paddle 2
    if (ball.xcor() < player_line and player2.distance(ball) < 21*PADDLE_LENGTH/2 and
            (ball.heading() < 45 or ball.heading() > 315)):
        ball.bounce(ball.heading(), "player2")

    # player 1 scores
    if ball.xcor() > player_line + 30:
        scoreboard.update_score(1)
        ball.reset_ball()

    # player 2 scores
    if ball.xcor() < -player_line - 30:
        scoreboard.update_score(0)
        ball.reset_ball()

    screen.update()

screen.exitonclick()
