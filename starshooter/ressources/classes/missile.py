import pygame as pg
import random

from ressources.ressources import *
from ressources.settings import *
from ressources.functions import *

from ressources.classes.projectile import Projectile

class Missile(Projectile):
    def __init__(self, x, y, is_player, param, target=None):
        super().__init__(x, y, is_player, 'missile', param)
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
        self.dirX = (self.dirX + (self.distX / dist / 6))/2
        self.dirY = (self.dirY + (self.distY / dist / 6))/2
        self.x += self.dirX * self.speed
        self.y += self.dirY * self.speed

