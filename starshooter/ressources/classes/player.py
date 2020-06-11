import pygame as pg
from .. import ressources
from .ship import Ship
from .. import settings
from .. import functions

class Player(Ship):
    def __init__(self, x, y):
        super().__init__(x, y, 'player', 1)
        # self.sprite = functions.makeSprite(self.link ,4)

    def move(self):
        key = pg.key.get_pressed()
        if key[pg.K_q] and self.x - self.speed > 0:
            self.x -= self.speed
        if key[pg.K_d] and self.x + self.speed + self.get_width() < settings.screen.get_width():
            self.x += self.speed
        if key[pg.K_z] and self.y - self.speed > 0:
            self.y -= self.speed
        if key[pg.K_s] and self.y + self.speed + self.get_height() + self.speed < settings.screen.get_height():
            self.y += self.speed
        if key[pg.K_SPACE]:
            self.shoot()

    def update(self, targets):
        if self.health <= 0:
            self.health = 0 
            return True
        self.move()
        self.update_all(targets)

    def weapon_switch(self, key):
        if 0 <= key < self.slot_size:
            self.slot_active = key

    def healthbar(self, window):
        pg.draw.rect(window, (255, 0, 0), (self.x, self.y + self.img.get_height() + 10, self.img.get_width(), 10))
        pg.draw.rect(window, (0, 255, 0), (self.x, self.y + self.img.get_height() + 10, self.img.get_width() * (self.health/self.health_max), 10))

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)
