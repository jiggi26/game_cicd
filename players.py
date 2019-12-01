import turtle
from draw_object import Paddle

class Player():
    def __init__(self, pos):
        self.score = 0
        self.paddle = Paddle(position=pos, dims=(5, 0.5), shape="square")