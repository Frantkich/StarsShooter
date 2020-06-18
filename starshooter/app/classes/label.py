import pygame as pg

from app.ressources import *


class Label():
    def __init__(self, x, y, text, color, fontSize, font=main_font):
        self.x = x
        self.y = y
        self.text = text
        self.color = color
        self.fontSize = fontSize
        self.font = main_font
       
    def draw(self, is_active = 0, center = 0):
        if is_active:
            label = pg.font.Font(self.font, self.fontSize+20).render(self.text, False, self.color)
        else:
            label = pg.font.Font(self.font, self.fontSize).render(self.text, False, self.color)
        if center == 0:
            screen.blit(label, (self.x - label.get_width()/2, self.y - label.get_height()/2))
        elif center == 1:
            screen.blit(label, (self.x, self.y))
        elif center == 2:
            screen.blit(label, (self.x - label.get_width(), self.y - label.get_height()))

    def move(self, x=None, y=None):
        if x:
            self.x += x
        if y:
            self.y += y