import pygame
from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_1, ENEMY_2

class Ship(Enemy): #enemy headler-subclase, ereda clases y metodos de enemt
    WIDTH = 40
    HEIGHT = 60

    def __init__(self):
        self.image_1 = ENEMY_1
        self.image_2 = ENEMY_2
        self.image = pygame.transform.scale(self.image_1, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image)
        
