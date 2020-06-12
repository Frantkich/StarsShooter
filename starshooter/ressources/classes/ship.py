import pygame as pg
import random

from .. import ressources
from .weapon import Weapon
from ..settings import *
from ..functions import *

class Ship:
    def __init__(self, x, y, spaceship, is_player=0):
        self.x = x
        self.y = y
        self.is_player = is_player

        self.path, self.nbframe, self.health_max, self.speed, self.slot_size = ressources.spaceship_list[spaceship]
        self.health = self.health_max
        if not(is_player):
            self.img= pygame.transform.flip(pygame.image.load(self.path), 0, 1)
        else:
            self.img = pygame.image.load(self.path)

        self.init_sprites(self.img)
        self.init_weapons(self.slot_size)
        self.lasers = []

        self.powerups = []
        self.damage_mod = 1
        self.sizeX_mod = int(self.get_width()/2)
        self.sizeY_mod = int(self.get_height()/2)

    def init_sprites(self, img):
        self.sprites = spritesheet(img, self.nbframe)
        self.sprite = self.sprites[0]
        self.mask = pg.mask.from_surface(self.sprite)
        self.frame = 0
        self.nextFrame = 0
    
    def init_weapons(self, slot_size):
        self.weapons = [Weapon() for _ in range(self.slot_size)]
        self.slot_active = 0


    def new_weapon(self, x, y, slot, weapon):
        self.weapons[slot] = Weapon(weapon, x, y)
        self.slot_active = slot


    def shoot(self):
        laser = self.weapons[self.slot_active].shoot(self.x + self.sizeX_mod, self.y + self.sizeY_mod, self.is_player)
        if laser:
            self.lasers.append(laser)


    def update_sprite(self):
        if self.nextFrame == 0:
            self.frame = (self.frame + 1) % self.nbframe
            self.sprite = self.sprites[self.frame]
            self.mask = pg.mask.from_surface(self.sprite)
            self.nextFrame = gif_speed
        self.nextFrame -= 1

    def update_weapons(self):
        for weapon in self.weapons:
            weapon.check_cooldown()

    def update_powerups(self):
        for powerup in self.powerups:
            powerup.check_time(self)

    def update_lasers(self, targets):
        for laser in self.lasers:
            laser.move()
            if laser.off_screen(screen.get_height()):
                self.lasers.remove(laser)
            for target in targets:
                if collide(laser, target) and not(target in laser.hit):
                    target.health -= laser.damage * self.damage_mod
                    if laser in self.lasers:
                        if laser.penetration:
                            laser.penetration -= 1
                            laser.hit.append(target)
                        else:
                            self.lasers.remove(laser)

    def update_all(self, targets):
        self.update_sprite()
        self.update_weapons()
        self.update_lasers(targets)
        self.update_powerups()


    def draw(self, window):
        window.blit(self.sprite, (self.x, self.y))
        for laser in self.lasers:
            laser.draw(window)
        self.weapons[self.slot_active].draw(window)        


    def get_width(self):
        return self.sprite.get_width()

    def get_height(self):
        return self.sprite.get_height()