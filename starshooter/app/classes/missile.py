from app.ressources import *

from app.classes.projectile import Projectile


class Missile(Projectile):
    def __init__(self, x, y, is_player, param, target=None):
        super().__init__(x, y, is_player, 'missile', param)
        self.dirX = random.uniform(-self.dispertion, self.dispertion)
        self.target = target

    def move(self):
        if self.target:
            self.distX = self.target.x + self.target.get_width()/2 - self.x
            self.distY = self.target.y + self.target.get_height()/2 - self.y
            dist = math.hypot(self.distX, self.distY)
        else:
            self.distX = self.dirX
            self.distY = self.dirY
            dist = math.hypot(self.distX, self.distY)
        self.dirX = (23*self.dirX + (self.distX / dist))/25
        self.dirY = (23*self.dirY + (self.distY / dist))/25
        self.x += self.dirX * self.speed
        self.y += self.dirY * self.speed

