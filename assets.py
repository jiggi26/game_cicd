import turtle
import winsound
from draw_object import Paddle, Ball, ScoreBoard
from players import Player

class Window():
    def __init__(self):
        self.window = turtle.Screen()
        self.window.title("Pong by NAmadao")
        self.window.bgcolor("black")
        self.window.setup(width=800, height= 600)
        self.window.tracer(0)

class Assets():
    def __init__(self):
        # Scoreboard
        self.score_board = ScoreBoard(position=(0, 260), dims=(1, 1))

        # Paddle A
        self.player_a = Player(pos=(-350, 0))

        # Paddle B
        self.player_b = Player(pos=(350, 0))

        # Write score
        self.score_board.score_write(self.player_a.score, self.player_b.score)

        # Ball
        self.Ball = Ball(position=(0, 0), dims=(1, 1), shape="circle")

    def collision_detection(self):
        ball_xcor = self.Ball.turtle_object.xcor()
        ball_ycor = self.Ball.turtle_object.ycor()
        player_a_ycor =  self.player_a.paddle.turtle_object.ycor()
        player_b_ycor =  self.player_b.paddle.turtle_object.ycor()

        # Right paddle collision
        if (ball_xcor > 340 and ball_xcor < 350) and (ball_ycor < 
        player_b_ycor + 40 and ball_ycor > player_b_ycor - 40):
            self.Ball.turtle_object.setx(340)
            self.Ball.turtle_object.dx *= -1
            self.play_sound()

        # Left paddle collision
        if (ball_xcor < -340 and ball_xcor > -350) and (ball_ycor < 
        player_a_ycor + 40 and ball_ycor > player_a_ycor - 40):
            self.Ball.turtle_object.setx(-340)
            self.Ball.turtle_object.dx *= -1
            self.play_sound()

    def border_checking_y(self):
        if self.Ball.turtle_object.ycor() > 290:
            self.Ball.turtle_object.sety(240)
            self.Ball.turtle_object.dy *= -1
            self.play_sound()

        if self.Ball.turtle_object.ycor() < -290:
            self.Ball.turtle_object.sety(-240)
            self.Ball.turtle_object.dy *= -1
            self.play_sound()

    def border_checking_x(self):
        if self.Ball.turtle_object.xcor() > 390:
            self.Ball.turtle_object.goto(0, 0)
            self.Ball.turtle_object.dx *= -1
            self.player_a.score += 1
            self.score_board.turtle_object.clear()
            self.score_board.score_write(self.player_a.score, self.player_b.score)
            self.play_sound()
        
        if self.Ball.turtle_object.xcor() < -390:
            self.Ball.turtle_object.goto(0, 0)
            self.Ball.turtle_object.dx *= -1
            self.player_b.score += 1
            self.score_board.turtle_object.clear()
            self.score_board.score_write(self.player_a.score, self.player_b.score)
            self.play_sound()

    def play_sound(self):
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)