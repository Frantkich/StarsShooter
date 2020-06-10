import pygame as pg
import random

from .. import ressources
from .weapon import Weapon
from .. import settings
from .. import functions

class Ship:
    def __init__(self, x, y, spaceship, is_player=0):
        self.x = x
        self.y = y
        
        self.img, self.health_max, self.speed, self.slot_size = ressources.spaceship_list[spaceship]
        self.health = self.health_max
        self.speed += self.speed*random.randint(-25, 25)/100
        self.is_player = is_player
        self.mask = pg.mask.from_surface(self.img)
        
        self.weapons = [Weapon() for _ in range(self.slot_size)]
        self.slot_active = 0
        self.lasers = []

        self.powerups = []


    def new_weapon(self, x, y, slot, weapon):
        self.weapons[slot] = Weapon(weapon, x, y)
        self.slot_active = slot


    def shoot(self):
        laser = self.weapons[self.slot_active].shoot(self.x, self.y, self.is_player)
        if laser:
            self.lasers.append(laser)


    def update_weapons(self):
        for weapon in self.weapons:
            weapon.check_cooldown()


    def update_powerups(self):
        for powerup in self.powerups:
            powerup.check_time(self)


    def update_lasers(self, targets):
        for laser in self.lasers:
            laser.move()
            if laser.off_screen(settings.screen.get_height()):
                self.lasers.remove(laser)
            for target in targets:
                if functions.collide(laser, target) and not(target in laser.hit):
                    target.health -= laser.damage
                    if laser in self.lasers:
                        if laser.penetration:
                            laser.penetration -= 1
                            laser.hit.append(target)
                        else:
                            self.lasers.remove(laser)


    def update_all(self, targets):
        self.update_weapons()
        self.update_lasers(targets)
        self.update_powerups()


    def draw(self, window):
        window.blit(self.img, (self.x, self.y))
        self.weapons[self.slot_active].draw(window)
        for laser in self.lasers:
            laser.draw(window)


    def get_width(self):
        return self.img.get_width()


    def get_height(self):
        return self.img.get_height()