import pygame as pg
from .. import ressources
from .. import settings
from .laser import Laser

class Weapon:
    def __init__(self, weapon=None, x=None, y=None):
        self.weapon = weapon
        self.x = x
        self.y = y
        if self.weapon:
            self.cooldown_max = ressources.weapon_list[weapon][0] * settings.fps
            self.cooldown = 0

    def check_cooldown(self):
        if self.weapon:
            if self.cooldown < self.cooldown_max:
                self.cooldown += 1


    def shoot(self, x, y, is_player):
        if self.weapon:
            if self.cooldown == self.cooldown_max:
                self.cooldown = 0
                return Laser(x + self.x, y + self.y, is_player, ressources.weapon_list[self.weapon][1])
        
    
    def cooldownbar(self, window):
        bar_height = 50
        if self.cooldown_max:
            if self.cooldown_max == -1:
                ratio = 0
            else:
                ratio = self.cooldown/self.cooldown_max
        else:
            ratio = 1
        pg.draw.rect(window, ressources.weapon_list[self.weapon][1][0], (settings.screen.get_width() - 40, settings.screen.get_height() - bar_height - 10, 10, bar_height))
        pg.draw.rect(window, (0, 255, 0), (settings.screen.get_width() - 20, settings.screen.get_height() - bar_height - 10, 10, bar_height))
        pg.draw.rect(window, (255, 0, 0), (settings.screen.get_width() - 20, settings.screen.get_height() - bar_height - 10, 10, bar_height - bar_height * ratio))
    
    def draw(self, window):
        if self.weapon:
            self.cooldownbar(window)
