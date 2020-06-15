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

    def draw(self, screen, item_active):
            self.shop_item_list[self.item_count].draw_item(screen, self.x , self.y, item_active)


    def add_shop_item(self, shop_item):
        self.shop_item_list.append(shop_item)
    