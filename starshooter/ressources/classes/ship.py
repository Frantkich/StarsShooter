import pygame as pg
import random

from ..ressources import *
from ..settings import *
from ..functions import *

from .weapon import Weapon


class Ship:
    def __init__(self, x, y, spaceship, is_player=0):
        #pos
        self.x = x
        self.y = y
        self.is_player = is_player
        # basic stats
        self.health_max, self.speed = spaceship_list[spaceship][1]
        self.health = self.health_max
        #prites
        self.path, self.nbframe = spaceship_list[spaceship][0]
        if not(is_player):
            self.img= pygame.transform.flip(pygame.image.load(self.path), 0, 1)
        else:
            self.img = pygame.image.load(self.path)
        self.init_sprites(self.img)
        #weapons
        self.weapons = [Weapon(pos) for pos in spaceship_list[spaceship][2]]
        self.slot_active = 0
        #lasers
        self.lasers = []
        #powerups
        self.powerups = []
        self.damage_mod = 1
        self.size_mod = 1

    def init_sprites(self, img):
        self.sprites = spritesheet(img, self.nbframe)
        self.sprite = self.sprites[0]
        self.mask = pg.mask.from_surface(self.sprite)
        self.frame = 0
        self.nextFrame = 0

    def shoot(self):
        laser = self.weapons[self.slot_active].shoot(self.x + self.get_width()/2, self.y + self.get_height()/2, self.size_mod, self.is_player)
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
        for laser in self.lasers:
            laser.draw(window)
        window.blit(self.sprite, (self.x, self.y))
        self.weapons[self.slot_active].draw(window)        

    def get_width(self):
        return self.sprite.get_width()

    def get_height(self):
        return self.sprite.get_height()