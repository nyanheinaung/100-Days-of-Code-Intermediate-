from turtle import Turtle

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 1200
LINE_SEGMENT_NUMBER = 10
PENSIZE = 5


class UI(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.speed(0)
        self.penup()
        self.draw_mid_line()

    def draw_mid_line(self):
        line_segment_length = SCREEN_HEIGHT // (2*LINE_SEGMENT_NUMBER+1)
        self.goto(0, -SCREEN_HEIGHT/2+20)
        self.pensize(PENSIZE)
        self.left(90)
        for i in range(LINE_SEGMENT_NUMBER):
            self.pendown()
            self.forward(line_segment_length)
            self.penup()
            self.forward(line_segment_length)



