import pygame as pg

from ressources.ressources import *
from ressources.classes.label import Label
from ressources.settings import screen

class Shop_item():

    def __init__(self,item_name, item_price, item_img):
        self.pos = [] #x and y
        self.item_stat = [item_name, item_price, item_img]
        self.labels = []
        self.img = pg.transform.scale(pg.image.load(self.item_stat[2]), (120, 120))

    def draw_item(self, x, y, item_active):
        self.pos = [x, y]
        self.labels.append(Label(self.pos[0] + screen.get_width()/4, self.pos[1] + self.img.get_height()*6/4, self.item_stat[0], (255, 240, 200), 30))
        self.labels.append(Label(self.pos[0] + 65, self.pos[1] -10, self.item_stat[1], (255, 240, 200), 25))
        self.labels[0].draw()
        self.labels[1].draw()

        if item_active:
            self.img = pg.transform.scale(pg.image.load(self.item_stat[2]), (150, 150))
            screen.blit(self.img, (self.pos[0]+ 50, self.pos[1]))

        else:
            self.img = pg.transform.scale(pg.image.load(self.item_stat[2]), (120, 120))
            screen.blit(self.img, (self.pos[0]+ 50, self.pos[1]))
        
        
        
        
    