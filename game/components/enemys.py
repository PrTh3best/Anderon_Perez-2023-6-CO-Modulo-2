import pygame
from game.utils.constants import ENEMY_1,ENEMY_2, BULLET_ENEMY, SCREEN_WIDTH, SCREEN_HEIGHT

class Enemy:
    def __init__(self):
        self.enemy_1 = ENEMY_1
        self.enemy_2 = ENEMY_2
        self.enemy_1 = pygame.transform.scale(self.enemy_1,(40, 60))
      #  self.enemy_2 = pygame.transform.scale(self.enemy_2(40, 60))
        self.enemy_1_rect = self.enemy_1.get_rect()
        self.enemy_1_rect.x, self.enemy_1_rect.y = (SCREEN_WIDTH//2, SCREEN_HEIGHT//2)
        self.enemy_2_rect = self.enemy_2.get_rect()
        self.enemy_2_rect.x, self.enemy_2_rect.y = (SCREEN_WIDTH, SCREEN_HEIGHT)

    def draw(self, screen):
        screen.blit(self.enemy_1, (self.enemy_1_rect.x, self.enemy_1_rect.y))
        #screen.blit(self.enemy_2, (self.enemy_2_rect.x, self.enemy_2_rect.y))