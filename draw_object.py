import turtle
from abc import ABC

class draw_objects(ABC):
    """
    abstract class, inherited by Ball, Paddle and Scoreboard
    """
    def __init__(self, position, dims):
        self.turtle_object = turtle.Turtle()
        self.turtle_object.speed(0) #speed of animation, max possible speed
        self.turtle_object.color("white") #color of paddle
        self.turtle_object.shapesize(stretch_wid=dims[0], stretch_len=dims[1]) 
        self.turtle_object.penup()
        self.turtle_object.goto(position[0], position[1]) #position of paddle.
        #centre is (0,0)

class Ball(draw_objects):

    def __init__(self, position, dims, shape):
        draw_objects.__init__(self, position, dims)
        self.turtle_object.shape(shape)
        self.turtle_object.dx = 0.35
        self.turtle_object.dy = 0.35
    
    def ball_setx(self):
        self.turtle_object.setx(self.turtle_object.xcor() + 
                                self.turtle_object.dx)
    
    def ball_sety(self):
        self.turtle_object.sety(self.turtle_object.ycor() + 
                                self.turtle_object.dy)

class Paddle(draw_objects):
    
    def __init__(self, position, dims, shape):
        draw_objects.__init__(self, position, dims)
        self.turtle_object.shape(shape)
    
    def paddle_up(self):
        y = self.turtle_object.ycor()
        y += 20
        self.turtle_object.sety(y)

    def paddle_down(self):
        y = self.turtle_object.ycor()
        y -= 20
        self.turtle_object.sety(y)

class ScoreBoard(draw_objects):
    def __init__(self, position, dims):
        draw_objects.__init__(self, position, dims)
        self.turtle_object.hideturtle()

    def score_write(self, score_a, score_b):
        self.turtle_object.write("Player A: {}   Player B: {}".
                                format(score_a, score_b), align='center',
                                font=('Courier', 24, 'normal'))