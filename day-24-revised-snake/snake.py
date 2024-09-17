from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.snake_head = self.snake_body[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.setposition(position)
        self.snake_body.append(segment)

    def extend(self):
        self.add_segment(self.snake_body[-1].position())

    def move(self):
        for segment_no in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[segment_no - 1].xcor()
            new_y = self.snake_body[segment_no - 1].ycor()
            self.snake_body[segment_no].goto(new_x, new_y)
        self.snake_head.forward(MOVE_DISTANCE)
        # self.snake_head.left(90)

    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)

    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)

    def reset(self):
        for segment in self.snake_body:
            segment.hideturtle()
        self.snake_body.clear()
        self.create_snake()
        self.snake_head = self.snake_body[0]
