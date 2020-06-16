import random

from ressources.ressources import *
from ressources.settings import *
from ressources.functions import *

from ressources.classes.ship import Ship

class Boss(Ship):
    def __init__(self, x, y, model):
        super().__init__(x, y, model)
        self.destX = int(screen.get_width()/2 - self.get_width()/2)
        self.destY = int(random.randint(0, int(screen.get_height()/2)))
        self.firerateMod = 1

    def move(self):
        self.distX = self.destX - self.x
        self.distY = self.destY - self.y
        dist = math.hypot(self.distX, self.distY)
        self.dirX = self.distX / dist
        self.dirY = self.distY / dist

        self.x += self.dirX * self.speed
        self.y += self.dirY * self.speed

        if dist < self.speed: 
            self.destX = random.randint(0, screen.get_width() - self.get_width())
            self.destY = random.randint(0, int(screen.get_height()/4))

    def update(self, targets):
        target = targets[0]
        if self.health <= 0:
            return self
        if random.randrange(0, fps * self.firerateMod) == 1:
            for self.slot_active in range(len(self.weapons)):
                self.shoot()
        if collide(self, target):
            target.money += 1000
            target.score += 1000
            return self
        self.move()
        self.update_all(targets)
    
