from game.utils.constants import BULLET_ENEMY, BULLET_ENEMY
from game.components.bullets.bullet_enemy import BulletEnemy
from game.components.bullets.bullet_spaceship import BulletSpaceship

class BulletHandler:
    def __init__(self):
        self.bullets = []
#        # las constantes BULLET_ENEMY y BULLET_ENEMY 
    def update(self, player, enemies):#Recorre cada bala en la lista bullets
        for bullet in self.bullets:
            if not bullet.is_alive:
                self.remove_bullet(bullet)  #RECUERDAA!
            else:
                if bullet.type == BULLET_ENEMY: #llama al método
                #update(player) para actualizar su posición según el jugador actual.
                    bullet.update(player)
                else:
                    for enemy in enemies:
                        bullet.update(enemy)
    
    def draw(self, screen):
        for bullet in self.bullets:
            bullet.draw(screen)
    
    def add_bullet(self, type, center):
        if type == BULLET_ENEMY:
            self.bullets.append(BulletEnemy(center))
        else:
            self.bullets.append(BulletSpaceship(center))
    
    def remove_bullet(self, bullet):
        self.bullets.remove(bullet)
    
    def reset(self):
        self.bullets = []
