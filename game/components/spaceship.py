import pygame
from game.utils.constants import SPACESHIP, SPACESHIP_SHIELD, SCREEN_WIDTH, SCREEN_HEIGHT, BULLET_SPACESHIP_TYPE
from game.components.power_ups.shield import Shield

class Spaceship:
    WIDTH = 40
    HEIGTH = 60
    X_POS = (SCREEN_WIDTH // 2) - 40
    Y_POS = 500

    def __init__(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGTH))
          #  self.label = FONT_STYLE.render(f'xwing: {label}', True, (12, 159, 254))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.is_alive = True
        self.has_shield = False
        self.time_up = 0

    def update(self, user_input, bullet_handler):
        if user_input[pygame.K_LEFT]:
            self.move_left()
        elif user_input[pygame.K_RIGHT]:
            self.move_right()
        elif user_input[pygame.K_UP]:
            self.move_up()
        elif user_input[pygame.K_DOWN]:
            self.move_down()
        elif user_input[pygame.K_SPACE]:
            self.shoot(bullet_handler)
        
        if self.has_shield:
            time_to_show = round((self.time_up - pygame.time.get_ticks())/1000, 2)
            if time_to_show < 0:
                self.deactivate_power()

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move_left(self):
        if self.rect.left > 0:
            self.rect.x -= 10

    def move_right(self):
        if self.rect.right < SCREEN_WIDTH:
            self.rect.x += 10

    def move_up(self):
        if self.rect.y > SCREEN_HEIGHT // 2:
            self.rect.y -= 10
    
    def move_down(self):
        if self.rect.y < SCREEN_HEIGHT - 70:
            self.rect.y += 10
    
    def shoot(self, bullet_handler):
        bullet_handler.add_bullet(BULLET_SPACESHIP_TYPE, self.rect.center)
    
    def reset(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGTH))
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.is_alive = True

    def activate_power_up(self, power_up):
        self.time_up = power_up.time_up
        if type(power_up) == Shield:
            self.has_shield = True
            self.image = SPACESHIP_SHIELD
            self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGTH))

    def deactivate_power(self):
        self.has_shield = False
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGTH))