import pygame
from game.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from game.components.spaceship import SPACESHIP
from game.components.enemys import ENEMY_1, ENEMY_2

class Name:

    def __init__(self):
        self.time = 0
        self.spaceship = SPACESHIP ("xwing")
        self.enemy_1 = ENEMY_1 ("dv1")
        self.enemy_2 = ENEMY_2 ("dv2")


    def draw (self, screen, keys):
        if  self.spaceship.draw(screen):

            self.spaceship.update(keys)
        else:
            self.enemy_1.draw(screen)
            self.enemy_2.draw(screen)
    