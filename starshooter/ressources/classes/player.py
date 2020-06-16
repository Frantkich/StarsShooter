import pygame as pg

from ressources.ressources import *
from ressources.settings import *
from ressources.functions import *

from ressources.classes.ship import Ship
from ressources.classes.label import Label

class Player(Ship):
    def __init__(self, x, y):
        super().__init__(x, y, 'player', 1)
        self.x = screen.get_width()/2 - self.get_width()/2
        self.screen_shake = 0
        self.money = 0
        self.score = 0
        self.max_score = 0
        
    def move(self):
        if keyPressed("q") and self.x - self.speed > 0:
            self.x -= self.speed
        if keyPressed("d") and self.x + self.speed + self.get_width() < screen.get_width():
            self.x += self.speed
        if keyPressed("z") and self.y - self.speed > 0:
            self.y -= self.speed
        if keyPressed("s") and self.y + self.speed + self.get_height() + self.speed < screen.get_height():
            self.y += self.speed

    def check_shoot(self):
        if keyPressed("space"):
            self.shoot()

    def update(self, targets):
        if self.health <= 0:
            self.health = 0
            if self.max_score < self.score:
                self.max_score = self.score
            self.score = 0
            return True
        self.move()
        self.check_shoot()
        self.update_all(targets)

    def weapon_switch(self, key):
        if 0 <= key < len(self.weapons):
            self.slot_active = key

    def healthbar(self):
        height = 50
        width = 150
        thickness = 5
        offset = 10
        color = (255, 240, 200)

        ratio = self.health/self.health_max
        pg.draw.rect(screen, (255, 0, 0), (screen.get_width() - offset - width, screen.get_height() - int(height/2) - thickness - offset, width, int(height/2)))
        pg.draw.rect(screen, (0, 255, 0), (screen.get_width() - offset - width, screen.get_height() - int(height/2) - thickness - offset, width*ratio, int(height/2)))
        Label(screen.get_width() - (offset + width + thickness)/2, screen.get_height() - height, self.name, color, 20).draw()
        pg.draw.rect(screen, color, (screen.get_width() - offset - width, screen.get_height() - height - thickness - offset, width, height), thickness)
        pg.draw.line(screen, color, (screen.get_width() - offset - width, screen.get_height() - int(height/2) - thickness - offset), (screen.get_width() - offset, screen.get_height() - int(height/2) - thickness - offset), thickness)

    def draw(self):
        super().draw()
        self.healthbar()
        self.weapons[self.slot_active].draw()
        height = 125
        color = (255, 240, 200)
        offset = 25
        for powerup in self.powerups:
            Label((offset)/2, screen.get_height() - height, ' :'.join((powerup.name, str(int(powerup.time / fps)))), color, 20).draw(0, 0)
            height += 25