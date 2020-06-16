import pygame as pg

from ressources.ressources import *
from ressources.classes.label import Label
from ressources.settings import screen

class Oter():

    def __init__(self, x, y):
        self.pos = (x, y) 
        self.labels = []
        self.img = pg.transform.scale(pg.image.load(self), (120, 120))
    

    def draw(self):
        #Sound
        
        screen.blit(self.img, (self.pos[0], self.pos[1]))


