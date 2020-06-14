import pygame as pg

from ressources.ressources import *

class Shop_section():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.surface = pg.Surface((self.width, self.height))
        self.shop_item = []

    def draw(self, screen):
        self.surface.fill((255, 0, 0))
        screen.blit(self.surface, (self.width, self.height))
    
    def add_shop_item(self, shop_item):
        self.shop_item.append(shop_item)
    