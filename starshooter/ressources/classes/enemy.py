import random

from ressources.ressources import *
from ressources.settings import *
from ressources.functions import *

from .ship import Ship

class Enemy(Ship):
    def __init__(self, x, y, model):
        super().__init__(x, y, model)
        self.speed *= random.uniform(1, 1.25)

    def move(self):
        self.y += self.speed

    def check_shoot(self):
        if random.randrange(0, (2*fps) * firerateMod) == 1:
            self.shoot()

    def update(self, targets):
        target = targets[0]
        if self.y + self.get_height() > screen.get_height():
            target.health -= target.health_max/4
            return self
        if collide(self, target):
            target.health -= target.health_max/8
            return self
        if self.health <= 0:
            target.money += 10
            target.score += 10
            return self
        self.move()
        self.check_shoot()
        self.update_all(targets)