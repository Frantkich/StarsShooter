import random
from .ship import Ship
from ..settings import *
from ..functions import *


class Boss(Ship):
    def __init__(self, x, y, model):
        super().__init__(x, y, model)
        self.speed *= random.uniform(1, 1.25)
        self.maxHeight = random.randint(
            screen.get_height()/4, screen.get_height()/3)

    def move(self):
        if self.y < self.maxHeight:
            self.y += self.speed
        else:
            self.y -= self.speed

    def update(self, targets):
        target = targets[0]
        if self.health <= 0:
            return self
        if random.randrange(0, 2*60) == 1:
            self.shoot()
        if functions.collide(self, target):
            target.health -= 0
            return self

        self.move()
        self.update_all(targets)
