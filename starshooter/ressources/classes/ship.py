import pygame as pg
import random

from ressources.ressources import *
from ressources.settings import *
from ressources.functions import *

from ressources.classes.weapon import Weapon
from ressources.classes.explosion import Explosion


class Ship:
    def __init__(self, x, y, spaceship, is_player=0):
        #pos
        self.x = x
        self.y = y
        self.is_player = is_player
        self.name = spaceship
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
        self.weapons = [Weapon(pos, is_player) for pos in spaceship_list[spaceship][2]]
        self.slot_active = 0
        #projectiles
        self.projectiles = []
        self.explosions = []
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
        projectiles = self.weapons[self.slot_active].shoot(self.x + self.get_width()/2, self.y + self.get_height()/2, self.size_mod)
        if projectiles:
            for projectile in projectiles:
                self.projectiles.append(projectile)

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

    def update_projectiles(self, targets):
        for projectile in self.projectiles:
            projectile.move()
            if projectile.off_screen(screen.get_width(), screen.get_height()):
                self.projectiles.remove(projectile)
            for target in targets:
                if collide(projectile, target) and not(target in projectile.hit):
                    if projectile.name == 'missile':
                        self.explosions.append(Explosion((int(target.x + target.get_width()/2), int(target.y + target.get_height()/2)), 40))
                    target.health -= projectile.damage * self.damage_mod
                    if target.is_player:
                        target.screen_shake = 30
                    if projectile in self.projectiles:
                        if projectile.penetration:
                            projectile.penetration -= 1
                            projectile.hit.append(target)
                        else:
                            self.projectiles.remove(projectile)
            
            if projectile.name == 'missile':
                if len(targets):
                    if projectile.target:
                        if projectile.target.health <= 0:
                            projectile.target = None
                    else:
                        projectile.target = homingHead(self.x + self.get_width()/2, self.y + self.get_height()/2, targets)
                else:
                    projectile.target = None

    def update_all(self, targets):
        self.update_sprite()
        self.update_weapons()
        self.update_projectiles(targets)
        self.update_powerups()

    def draw(self, window):
        for projectile in self.projectiles:
            projectile.draw(window)
        window.blit(self.sprite, (self.x, self.y))
        for explosion in self.explosions:
            explosion.draw()
        self.weapons[self.slot_active].draw(window)        

    def get_width(self):
        return self.sprite.get_width()

    def get_height(self):
        return self.sprite.get_height()