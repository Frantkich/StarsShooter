import pygame as pg

from .. import ressources
from .. import settings
from .. import functions

class PowerUp:
    def __init__(self, x, y, powerup):
        self.x = x
        self.y = y
        self.powerup = powerup
        self.color, self.time, self.mod = ressources.powerup_list[powerup]
        self.speed = 10
        self.time *= settings.fps
        self.save = ()
        self.surface = pg.Surface((50, 50))
        self.mask = pg.mask.from_surface(self.surface)


    def move(self):
        self.y += self.speed


    def check_time(self, obj):
        if 0 < self.time:
            self.time -= 1
        else:
            self.effect(obj, 0)
            obj.powerups.remove(self)
            

    def effect(self, obj, add):
        if self.powerup == "speed":
            if add:
                self.save = (obj.speed)
                obj.speed *= self.mod
            else:
                obj.speed = self.save


    def update(self, obj):
        self.move()
        if settings.screen.get_height() < self.y:
            return self
        if functions.collide(self, obj):
            obj.powerups.append(self)
            self.effect(obj, 1)
            return self

    def draw(self, window):
        pg.draw.circle(window, self.color, (self.x, self.y), int(self.surface.get_height()/4))
