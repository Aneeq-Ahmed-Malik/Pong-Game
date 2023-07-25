from turtle import Turtle, Screen

screen = Screen()
screen.tracer(0)


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)
        screen.update()

    def move(self, down_key, up_key):
        screen.listen()
        screen.onkeypress(key=up_key, fun=self.go_up)
        screen.onkeypress(key=down_key, fun=self.go_down)

    def go_up(self):
        x_cor = self.xcor()
        y_cor = self.ycor()
        self.goto(x=x_cor, y=y_cor + 20)
        screen.update()

    def go_down(self):
        x_cor = self.xcor()
        y_cor = self.ycor()
        self.goto(x=x_cor, y=y_cor - 20)
        screen.update()
