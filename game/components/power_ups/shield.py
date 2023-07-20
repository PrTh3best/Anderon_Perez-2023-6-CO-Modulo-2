from game.components.power_ups.power_up import PowerUp
from game.utils.constants import SHIELD, INVISIBLE_PW

class Shield(PowerUp):
    def __init__(self):
        self.image = SHIELD
        self.image = INVISIBLE_PW
        super().__init__(self.image)

