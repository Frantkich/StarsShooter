import pygame as pg

from ressources.ressources import *

class Soundbarre():
    def __init__(self, x, y, color, screen):
        self.x = x
        self.y = y
        self.color = color
        self.width = screen.get_width()/2
        self.height = 10
        self.surface = pg.Surface((self.width, self.height))
        self.logo = pg.image.load(dir_asset + "/speaker.png")
        self.volumeMixer = pg.Surface((10, 30))
        self.volumeLevel = 5
        
    def draw(self, screen):
        self.surface.fill(self.color)
        self.volumeMixer.fill(self.color)
        screen.blit(self.surface, (self.x, self.y))    
        screen.blit(self.logo, (self.x - self.logo.get_width() - 10, self.y - self.logo.get_height()/2 + self.height/2))
        screen.blit(self.volumeMixer, (int(self.x + self.width * self.volumeLevel / 10), self.y - self.volumeMixer.get_height()/2 + self.height/2))
    
    def up_volumeLevel(self):
        self.volumeLevel += 1
    
    def down_volumeLevel(self):
        self.volumeLevel -= 1