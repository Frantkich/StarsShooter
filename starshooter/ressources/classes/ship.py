import pygame as pg
import random

from .. import ressources
from .weapon import Weapon
from .. import settings
from .. import functions

class Ship:
    def __init__(self, x, y, spaceship, player=0):
        self.x = x
        self.y = y
        self.img, self.health_max, self.speed, self.slot_size = ressources.spaceship_list[spaceship]
        self.health = self.health_max
        self.speed += self.speed*random.randint(-25, 25)/100
        self.player = player
        if player:
            self.img = pg.transform.rotate(self.img, 180)
        self.mask = pg.mask.from_surface(self.img)
        self.weapons = [Weapon() for _ in range(self.slot_size)]
        self.slot_active = 0
        self.lasers = []

    def new_weapon(self, x, y, slot, weapon):
        self.weapons[slot] = Weapon(weapon, x, y)
        self.slot_active = slot

    def shoot(self):
        laser = self.weapons[self.slot_active].shoot(self.x, self.y, self.player)
        if laser:
            self.lasers.append(laser)

    def move_lasers(self, objs):
        for weapon in self.weapons:
            weapon.check_cooldown()
        for laser in self.lasers:
            laser.move()
            if laser.off_screen(settings.screen.get_height()):
                self.lasers.remove(laser)
            for obj in objs:
                if functions.collide(laser, obj) and not(obj in laser.hit):
                    obj.health -= laser.damage
                    if laser in self.lasers:
                        if laser.penetration:
                            laser.penetration -= 1
                            laser.hit.append(obj)
                        else:
                            self.lasers.remove(laser)

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))
        self.weapons[self.slot_active].draw(window)
        for laser in self.lasers:
            laser.draw(window)
        
    def get_width(self):
        return self.img.get_width()

    def get_height(self):
        return self.img.get_height()