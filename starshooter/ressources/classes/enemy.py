import random
from .ship import Ship
from ..settings import *
from ..functions import *

class Enemy(Ship):
    def __init__(self, x, y, model):
        super().__init__(x, y, model)
        self.speed *= random.uniform(1, 1.25)

    def move(self):
        self.y += self.speed

    def update(self, targets):
        target = targets[0]
        
        if self.health <= 0:
            return self
        if random.randrange(0, 2*fps) == 1:
            self.shoot()
        
        if self.y + self.get_height() > screen.get_height():
            target.health -= target.health_max/4
            return self
        if collide(self, target):
            target.health -= target.health_max/8
            return self

        self.move()
        self.update_all(targets)