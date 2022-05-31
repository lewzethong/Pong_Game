from turtle import Turtle
RIGHT_PADDLE_COORDINATE = (350, 0)
LEFT_PADDLE_COORDINATE = (-350, 0)
UP = 90
DOWN = 270

class Paddles(Turtle):
    def __init__(self, coordinate):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.pu()
        self.goto(coordinate)


    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
