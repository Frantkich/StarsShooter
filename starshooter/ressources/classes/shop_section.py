import pygame as pg

from ressources.ressources import *
from ressources.classes.label import Label
from ressources.settings import screen

class Shop_section():
    def __init__(self, label_y, label_text, x, y):
        self.label = Label(screen.get_width()/2, label_y, label_text, (255, 240, 200), 40)  #Label(self, x, y, text, color, fontSize, font=main_font)
        self.x = x
        self.y = y
        self.shop_item_list = []
        self.item_count = 0

    def draw(self, item_active):
            pos = self.item_count % (len(self.shop_item_list))
            self.shop_item_list[pos].draw_item(self.x , self.y + 50, item_active)
            if pos-1 < 0:
                self.shop_item_list[len(self.shop_item_list)-1].draw_item(self.x -200 , self.y + 60, 0)
            else:
                self.shop_item_list[pos-1].draw_item(self.x -200 , self.y + 60, 0) 
            if len(self.shop_item_list) == pos+1:
                self.shop_item_list[0].draw_item(self.x + 200 , self.y + 60, 0)
            else:
                self.shop_item_list[pos+1].draw_item(self.x + 200 , self.y + 60, 0)

    def add_shop_item(self, shop_item):
        self.shop_item_list.append(shop_item)
    