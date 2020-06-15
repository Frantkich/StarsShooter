import pygame as pg

from ressources.ressources import *
from ressources.classes.label import Label
from ressources.settings import screen

class Shop_item():

    def __init__(self,item_name, item_price, item_img):
        self.pos = [] #x and y
        self.item_stat = [item_name, item_price, item_img]
        self.labels = []
        self.img = pg.transform.scale( pg.image.load(dir_asset + "/" + self.item_stat[2]), (200, 200))

    def draw_item(self, screen, x, y, item_active):
        self.pos = [x, y]
        self.labels.append(Label(self.pos[0], self.pos[1] + self.img.get_height(), self.item_stat[0], (255, 240, 200), 30))
        self.labels.append(Label(self.pos[0] + 25, self.pos[1] + 25, self.item_stat[1], (255, 240, 200), 25))

        if item_active:
            self.img = pg.transform.scale( pg.image.load(dir_asset + "/" + self.item_stat[2]), (230, 230))
            screen.blit(self.img, (self.pos[0] - 15, self.pos[1]))
        else:
            self.img = pg.transform.scale( pg.image.load(dir_asset + "/" + self.item_stat[2]), (200, 200))
            screen.blit(self.img, (self.pos[0], self.pos[1]))
        
        

        
        
        
    