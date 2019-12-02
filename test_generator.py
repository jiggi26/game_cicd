import unittest

from game import pong
def test_game():
    asset = 2
    version = 5
    assert pong.game_add(asset, version) == 7