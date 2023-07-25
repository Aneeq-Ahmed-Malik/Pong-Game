from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 60, "normal"))
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 60, "normal"))

    def draw_line(self, y_cor):
        self.goto(0, y_cor)
        self.setheading(270)
        for i in range(0, 20):
            self.pendown()
            self.forward(20)
            self.penup()
            y_cor -= 30
            self.goto(0, y_cor)
