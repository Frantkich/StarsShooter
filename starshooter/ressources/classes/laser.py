import pygame as pg

from ressources.ressources import *
from ressources.settings import *
from ressources.functions import *

class Laser:
    def __init__(self, x, y, is_player, param):
        self.x = x
        self.y = y
        self.is_player = is_player
        self.color, self.size, self.damage, self.speed, self.penetration = param
        self.surface = pg.Surface(self.size)
        self.mask = pg.mask.from_surface(self.surface)
        self.hit = []

    def move(self):
        if self.is_player:
            self.y -= self.speed
        else:
            self.y += self.speed

    def draw(self, window):
        pg.draw.rect(window, self.color, ((self.x - self.surface.get_width()/2, self.y), self.surface.get_size()))

    def off_screen(self, height):
        return not(self.y <= height and self.y >= -self.surface.get_height())
