import pygame as pg
import random

from ressources.ressources import *
from ressources.settings import *
from ressources.functions import *

from ressources.classes.projectile import Projectile

class Rayon(Projectile):
    def __init__(self, x, y, is_player, param):
        super().__init__(x, y, is_player, 'rayon', param)
        # self.targets = targets
        self.top = -5

    def move(self):
        pass

    
    def draw(self, window):
        pg.draw.rect(window, self.color, ((self.x - self.surface.get_width()/2, -5), (5, self.y)))