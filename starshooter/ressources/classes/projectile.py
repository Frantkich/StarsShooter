import pygame as pg
import random

from ressources.ressources import *
from ressources.settings import *
from ressources.functions import *

class Projectile:
    def __init__(self, x, y, is_player, name, param):
        self.x = x
        self.y = y
        self.is_player = is_player
        self.name = name
        self.color, self.size, self.damage, self.speed, self.penetration, self.dispertion= param
        self.surface = pg.Surface(self.size)
        self.mask = pg.mask.from_surface(self.surface)
        self.hit = []
        
        self.dirX = random.uniform(-self.dispertion, self.dispertion)
        if self.is_player:
            self.dirY = -1
        else:
            self.dirY = 1

    def draw(self, window):
        pg.draw.rect(window, self.color, ((self.x - self.surface.get_width()/2, self.y), self.surface.get_size()))

    def off_screen(self, width, height):
      return self.x + self.surface.get_width() < 0 or width < self.x or self.y + self.surface.get_height() < 0 or height < self.y
