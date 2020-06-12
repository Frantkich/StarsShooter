import pygame as pg

from ..ressources import *
from ..settings import *
from ..functions import *

from .laser import Laser

class Weapon:
    def __init__(self, pos, weapon=None):
        self.x, self.y = pos
        self.change_weapon(weapon)

    def change_weapon(self, weapon):
        self.weapon = weapon
        if self.weapon:
            self.cooldown_max = weapon_list[self.weapon][0] * fps
            self.cooldown = 0

    def check_cooldown(self):
        if self.weapon:
            if self.cooldown < self.cooldown_max:
                self.cooldown += 1

    def shoot(self, shipX, shipY, is_player):
        if self.weapon:
            if self.cooldown == self.cooldown_max:
                self.cooldown = 0
                return Laser(shipX + self.x, shipY + self.y, is_player, weapon_list[self.weapon][1])
    
    def cooldownbar(self, window):
        bar_height = 50
        if self.cooldown_max:
            if self.cooldown_max == -1:
                ratio = 0
            else:
                ratio = self.cooldown/self.cooldown_max
        else:
            ratio = 1
        pg.draw.rect(window, weapon_list[self.weapon][1][0], (screen.get_width() - 40, screen.get_height() - bar_height - 10, 10, bar_height))
        pg.draw.rect(window, (0, 255, 0), (screen.get_width() - 20, screen.get_height() - bar_height - 10, 10, bar_height))
        pg.draw.rect(window, (255, 0, 0), (screen.get_width() - 20, screen.get_height() - bar_height - 10, 10, bar_height - bar_height * ratio))
    
    def draw(self, window):
        if self.weapon:
            self.cooldownbar(window)
