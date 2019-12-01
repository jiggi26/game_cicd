# Pong game in Python using Turtle
# By NAmadao

import turtle
from game_definitions import Game_launch

def game_loop():
    game = Game_launch()

    # Main game loop
    while True:
        game.window_object.window.update()

        # Ball movement
        game.assets.Ball.ball_setx()
        game.assets.Ball.ball_sety()

        # Border checking
        game.assets.border_checking_y()
        game.assets.border_checking_x()

        # Collision checking
        game.assets.collision_detection()

if __name__ == '__main__':
    game_loop()