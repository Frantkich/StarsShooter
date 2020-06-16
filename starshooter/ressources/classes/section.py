import pygame as pg

from ressources.ressources import *
from ressources.classes.label import Label
from ressources.settings import screen

class Section():
    def __init__(self, label_y, label_text, x, y):
        self.label = Label(screen.get_width()/2, label_y, label_text, (255, 240, 200), 40)  #Label(self, x, y, text, color, fontSize, font=main_font)
        self.x = x
        self.y = y
        self.item_list = []
        self.equiped_list = []
        self.item_count = 0

    def draw(self, item_active):
            pos = self.item_count % (len(self.item_list))
            self.item_list[pos].draw_item(self.x , self.y + 50, item_active)
            if pos-1 < 0:
                self.item_list[len(self.item_list)-1].draw_item(self.x -200 , self.y + 60, 0)
            else:
                self.item_list[pos-1].draw_item(self.x -200 , self.y + 60, 0) 
            if len(self.item_list) == pos+1:
                self.item_list[0].draw_item(self.x + 200 , self.y + 60, 0)
            else:
                self.item_list[pos+1].draw_item(self.x + 200 , self.y + 60, 0)

    def add_item(self, item):
        self.item_list.append(item)
    
    def add_equiped_item(self, item):
        self.equiped_list.append(item)