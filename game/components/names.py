import pygame
from game.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from game.components.spaceship import Spaceship as spaceship
from game.components.enemys import Enemy as enemy

class Name:

    def __init__(self):
        self.time = 0
        self.spaceship = spacechip("player")
        self.enemy_1 = nemy_1 ("enemy_1")
        self.enemy_2 = enemy_2 ("enemy_2")

    def draw (self, screen, keys):
        if self.time == (FPS * 2):
            self.spaceship.draw(screen)
            self.spaceship.update(keys)
        else:
            self.enemy_1.draw(screen)
            self.enemy_2.draw(screen)