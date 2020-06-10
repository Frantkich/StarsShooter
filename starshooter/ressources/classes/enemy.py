import random
from .ship import Ship
from .. import settings
from .. import functions

class Enemy(Ship):
    def __init__(self, x, y, model):
        super().__init__(x, y, model)

    def move(self):
        self.y += self.speed

    def update(self, targets):
        target = None
        try:
            if targets[0].is_player:
                target = targets[0]
        except NameError:
            pass

        if self.health <= 0:
            return self
        if random.randrange(0, 2*60) == 1:
            self.shoot()
        
        if target:
            if self.y + self.get_height() > settings.screen.get_height():
                target.health -= target.health_max/4
                return self
            if functions.collide(self, target):
                target.health -= target.health_max/8
                return self
        self.move()
        self.update_all(targets)