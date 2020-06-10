import pygame as pg
from .. import ressources
from .. import settings
from .. import functions

class Laser:
    def __init__(self, x, y, player, param):
        self.x = x
        self.y = y
        self.player = player
        self.color, self.size, self.damage, self.speed, self.penetration = param
        self.surface = pg.Surface(self.size)
        self.mask = pg.mask.from_surface(self.surface)
        self.hit = []

    def move(self):
        if self.player:
            self.y -= self.speed
        else:
            self.y += self.speed

    def draw(self, window):
        pg.draw.rect(window, self.color, ((self.x - self.surface.get_width()/2, self.y), self.surface.get_size()))
        # pg.draw.circle(window, self.color, (self.x, self.y), int(self.surface.get_height()/4), int(self.surface.get_width()/4), 1, 1)

    def off_screen(self, height):
        return not(self.y <= height and self.y >= -self.surface.get_height())

    def collision(self, obj):
        return functions.collide(self, obj)
