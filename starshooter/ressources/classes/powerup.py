import pygame as pg

from .. import ressources
from .. import settings
from .. import functions

class PowerUp:
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name
        self.color, self.time, self.mod = ressources.powerup_list[name]
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
        if self.name == "speed":
            if add:
                self.save = (obj.speed)
                obj.speed *= self.mod
            else:
                obj.speed = self.save
        if self.name == "heal":
            obj.health = obj.health_max
        if self.name == "damage":
            if add:
                obj.damage_mod = self.mod
            else:
                obj.damage_mod = 1
        if self.name == "size":
            if add:
                self.save = (obj.img)
                obj.img = pg.transform.scale(obj.img, (int(obj.img.get_width() * self.mod), int(obj.img.get_height() * self.mod)))
                obj.mask = pg.mask.from_surface(obj.img)
                obj.sizeX_mod = int(obj.get_width()/2)
                obj.sizeY_mod = int(obj.get_height()/2)
            else:
                obj.img = self.save
                obj.mask = pg.mask.from_surface(obj.img)
                obj.sizeX_mod = int(obj.get_width()/2)
                obj.sizeY_mod = int(obj.get_height()/2)
        if self.name == "cooldown":
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
            for powerup in obj.powerups:
                if powerup.name == self.name:
                    powerup.time += self.time
                    return self
            obj.powerups.append(self)
            self.effect(obj, 1)
            return self

    def draw(self, window):
        pg.draw.circle(window, self.color, (self.x, self.y), int(self.surface.get_height()/4))
