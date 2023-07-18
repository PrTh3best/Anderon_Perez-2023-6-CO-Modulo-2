import pygame
import random
from game.utils.constants import ENEMY_1,ENEMY_2, BULLET_ENEMY, SCREEN_WIDTH, SCREEN_HEIGHT, FONT_STYLE

class Enemy:
    def __init__(self, label):
        self.img_1 = ENEMY_1
        self.enemy_2 = ENEMY_2
        self.enemy_1 = pygame.transform.scale(self.img_1,(40, 60))
        self.enemy_2 = pygame.transform.scale(self.enemy_2,(40, 60))
        font = pygame.font.Font(FONT_STYLE, 20)
        self.label = font.render(f'ENEMY: {label}', True, (240, 50, 50))
        self.enemy_1_rect = self.img_1.get_rect()
        self.enemy_1_rect.x, self.enemy_1_rect.y = (SCREEN_WIDTH/ 240, SCREEN_HEIGHT/ 400)
        #self.moveen_1 = 
        self.enemy_2_rect = self.enemy_2.get_rect()
        self.enemy_2_rect.x, self.enemy_2_rect.y = (SCREEN_WIDTH/ 275, SCREEN_HEIGHT/ 200)
        #self.moveen_2 =

    def draw(self, screen):
        screen.blit(self.enemy_1, (self.enemy_1_rect.x, self.enemy_1_rect.y))
        screen.blit(self.enemy_2, (self.enemy_2_rect.x, self.enemy_2_rect.y))