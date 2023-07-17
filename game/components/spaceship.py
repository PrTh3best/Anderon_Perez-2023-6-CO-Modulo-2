import pygame
from game.utils.constants import SPACESHIP, SCREEN_HEIGHT, SCREEN_WIDTH

class Spaceship:
    def __init__(self):
        self.spaceship = SPACESHIP 
        self.spaceship = pygame.transform.scale(self.spaceship,(40, 35))
        self.spaceship_rect = self.spaceship.get_rect()
        self.spaceship_rect.x, self.spaceship_rect.y = (SCREEN_WIDTH//2, SCREEN_HEIGHT//2)
    
    def move_up(self):
        if self.spaceship_rect.top > 0:
            self.spaceship_rect.top -= 15

    def move_down(self):
        if self.spaceship_rect.bottom  > 1: 
            self.spaceship_rect.bottom -= 15

    def move_left(self):
        if self.spaceship_rect.left > 0: 
            self.spaceship_rect.left += 15
    def move_rigth(self):
        if self.spaceship_rect.right < 1:
            self.spaceship_rect.right -= 15

    def update(self, key):
        if key[pygame.K_UP]:
            self.move_up()
        if key[pygame.K_DOWN]:
            self.move_down()
        if key[pygame.K_LEFT]:
            self.move_left()
        if key[pygame.K_RIGHT]:
            self.move_rigth()
        

    def draw(self, screen):
        screen.blit(self.spaceship, (self.spaceship_rect.x, self.spaceship_rect.y))
