import turtle
from assets import Assets, Window

class Game_launch():
    def __init__(self):
        # Window
        self.window_object = Window()

        # Assets
        self.assets = Assets()

        # Keyboard binding set up player 1 and player 2 objects
        self.window_object.window.listen()
        self.window_object.window.onkeypress(self.assets.player_a.paddle.paddle_up, 
                                            "w")
        self.window_object.window.onkeypress(self.assets.player_a.paddle.paddle_down, 
                                            "s")
        self.window_object.window.onkeypress(self.assets.player_b.paddle.paddle_up, 
                                            "Up")
        self.window_object.window.onkeypress(self.assets.player_b.paddle.paddle_down, 
                                            "Down")
 