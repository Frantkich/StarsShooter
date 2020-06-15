import pygame as pg
import random

from ressources.ressources import *
from ressources.settings import *
from ressources.functions import *

from ressources.classes.projectile import Projectile

class Laser(Projectile):
    def __init__(self, x, y, is_player, param):
        super().__init__(x, y, is_player, 'laser', param)

    def move(self):
        self.x += int(self.dirX * self.speed)
        self.y += int(self.dirY * self.speed)