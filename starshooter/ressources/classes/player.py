import pygame as pg

from ressources.ressources import *
from ressources.settings import *
from ressources.functions import *

from ressources.classes.ship import Ship

class Player(Ship):
    def __init__(self, x, y):
        super().__init__(x, y, 'player', 1)
        self.x = screen.get_width()/2 - self.get_width()/2
        self.screen_shake = 0

    def move(self):
        key = pg.key.get_pressed()
        if key[pg.K_q] and self.x - self.speed > 0:
            self.x -= self.speed
        if key[pg.K_d] and self.x + self.speed + self.get_width() < screen.get_width():
            self.x += self.speed
        if key[pg.K_z] and self.y - self.speed > 0:
            self.y -= self.speed
        if key[pg.K_s] and self.y + self.speed + self.get_height() + self.speed < screen.get_height():
            self.y += self.speed

    def check_shoot(self):
        key = pg.key.get_pressed()
        if key[pg.K_SPACE]:
            self.shoot()

    def update(self, targets):
        if keyPressed("return"):
            return True
        if self.health <= 0:
            self.health = 0 
            return True
        self.move()
        self.check_shoot()
        self.update_all(targets)

    def weapon_switch(self, key):
        if 0 <= key < len(self.weapons):
            self.slot_active = key

    def healthbar(self, window):
        pg.draw.rect(window, (255, 0, 0), (self.x, self.y + self.sprite.get_height() + 10, self.sprite.get_width(), 10))
        pg.draw.rect(window, (0, 255, 0), (self.x, self.y + self.sprite.get_height() + 10, self.sprite.get_width() * (self.health/self.health_max), 10))

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)
