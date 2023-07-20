from game.components.power_ups.power_up import PowerUp
from game.utils.constants import INVISIBLE_PW

class InvisiblePowerUp(PowerUp):
    def __init__(self):
        
        super().__init__(INVISIBLE_PW)

    def update(self, player):
        super().update(player)

def add_invisible_powerup(self, center):
    self.power_ups.append(InvisiblePowerUp())