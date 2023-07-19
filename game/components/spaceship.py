import pygame
import game
from game.utils.constants import SPACESHIP, SCREEN_HEIGHT, SCREEN_WIDTH, HEART, BULLET, FONT_STYLE

class Spaceship:
    def __init__(self, label):
        super(Spaceship, self).__init__()
        self.type = "player"
        self.spaceship = SPACESHIP 
        self.spaceship = pygame.transform.scale(self.spaceship,(40, 35))
        self.spaceship_rect = self.spaceship.get_rect()
        self.spaceship_rect.x, self.spaceship_rect.y = (SCREEN_WIDTH//2, SCREEN_HEIGHT//2)
       # self.label = FONT_STYLE.render(f'PLAYER: {label}', True, (12, 159, 254))
        self.bullets = []
        self.buller_counter = 0
      #  self.update_counter_text()

    
    def move_up(self):
        if self.spaceship_rect.top > 0:
            self.spaceship_rect.top -= 15

    def move_down(self):
        if self.spaceship_rect.bottom  < 0: 
            self.spaceship_rect.bottom += 15

    def move_left(self):
        if self.spaceship_rect.left > 0: 
            self.spaceship_rect.left -= 15
    def move_rigth(self):
        if self.spaceship_rect.right > 0:
            self.spaceship_rect.right += 15



    def update(self, key):
        if key[pygame.K_UP]:
            self.move_up()
        if key[pygame.K_DOWN]:
            self.move_down()
        if key[pygame.K_LEFT]:
            self.move_left()
        if key[pygame.K_RIGHT]:
            self.move_rigth()
        elif key[pygame.K_SPACE]:
            self.shoot(game)
        
        



    def draw(self, screen):
        screen.blit(self.spaceship, (self.spaceship_rect.x, self.spaceship_rect.y))
        font = pygame.font.font(None, 20) #selecciona la fuente y tamaño
        label = font.render(self.name, True, (255, 255, 255))
        screen.blit(label, (self.spaceship_rect.x, self.spaceship_rect.y - 20))
        

    #def fire_bullet(self):