from turtle import Screen
from paddle import Paddle
import time
from ball import Ball
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

r_paddle.move(down_key="Down", up_key="Up")
l_paddle.move(down_key="s", up_key="w")
ball = Ball()
score = ScoreBoard()
score.draw_line(300)
screen.update()

delay = 0.1
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(delay)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()
        delay *= 0.9
    elif ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        delay *= 0.9

    if ball.xcor() > 380:
        ball.reset_screen()
        score.l_score += 1
        score.update_score()
        score.draw_line(300)
        delay = 0.1

    elif ball.xcor() < -380:
        ball.reset_screen()
        score.r_score += 1
        score.update_score()
        score.draw_line(300)
        delay = 0.1


screen.exitonclick()
