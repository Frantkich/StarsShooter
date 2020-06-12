import random
from .ship import Ship
from ..settings import *
from ..functions import *


class Boss(Ship):
    def __init__(self, x, y, model):
        super().__init__(x, y, model)
        self.x = screen.get_width()/2 - self.get_width()/2
        self.maxY = random.randint(0, int(screen.get_height()/2))

    def move(self):
        if self.y < self.maxY:
            self.y += self.speed
        elif self.maxY < self.y:
            self.y -= self.speed
        else:
            self.maxY = random.randint(0, int(screen.get_height()/4))

    def shoot(self):
        for weapon in self.weapons:
            laser = weapon.shoot(self.x + self.sizeX_mod, self.y + self.sizeY_mod, self.is_player)
            if laser:
                self.lasers.append(laser)

    def update(self, targets):
        target = targets[0]
        if self.health <= 0:
            return self
        if random.randrange(0, 100) < 75:
            self.shoot()
        if collide(self, target):
            target.health -= 0
            return self

        self.move()
        self.update_all(targets)
    
