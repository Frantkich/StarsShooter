import pygame as pg

from .. import ressources
from .. import settings
from .. import functions

class PowerUp:
    def __init__(self, x, y, powerup):
        self.x = x
        self.y = y
        self.color, self.time, self.mod, self.var = ressources.powerup_list[powerup]
        self.speed = 10
        self.time *= settings.fps
        self.save = None
        self.surface = pg.Surface((50, 50))
        self.mask = pg.mask.from_surface(self.surface)
        

    def check_time(self, obj):
        if 0 < self.time:
            self.time -= 1
        else:
            exec(''.join(('obj.', self.var, ' = self.save')))
            obj.powerups.remove(self)
            

    def move(self):
        self.y += self.speed


    def update(self, target):
        self.move()
        if settings.screen.get_height() < self.y:
            return self
        if functions.collide(self, target):
            target.powerups.append(self)
            self.save = eval('target.' + self.var)
            exec(''.join(('target.', self.var, ' = self.mod * ', 'target.', self.var)))
            return self

    def draw(self, window):
        pg.draw.circle(window, self.color, (self.x, self.y), int(self.surface.get_height()/4))
