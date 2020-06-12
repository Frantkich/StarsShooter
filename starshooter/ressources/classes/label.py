import pygame as pg

from ressources.ressources import *

class Label():
    def __init__(self, x, y, text, color, fontSize, font=main_font):
        self.x = x
        self.y = y
        self.text = text
        self.color = color
        self.fontSize = fontSize
        self.font = font
       
    def draw(self, window, is_active = 0):
        if is_active:
            label = pg.font.Font(self.font, self.fontSize+25).render(self.text, False, self.color)
        else:
            label = pg.font.Font(self.font, self.fontSize).render(self.text, False, self.color)
        window.blit(label, (self.x - label.get_width()/2, self.y - label.get_height()/2))