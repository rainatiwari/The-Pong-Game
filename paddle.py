from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()  # super class call
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)  # Already paddle is of 20*20 size. and we need  20*100
        self.penup()
        self.goto(position)

    def go_up(self):    # Methods have first value as self
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

# turtle = Turtle()
# turtle.turtlesize(stretch_wid=20, stretch_len=100)
# turtle.setpos(x=350, height=100)
