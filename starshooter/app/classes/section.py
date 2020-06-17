from app.ressources import *

from app.classes.label import Label


class Section():
    def __init__(self, label_text, x, y):
        self.label = Label(screen.get_width()/2, y, label_text, (255, 240, 200), 30)  #Label(self, x, y, text, color, fontSize, font=main_font)
        self.x = x
        self.y = y
        self.item_list = []
        self.equiped_list = []
        self.item_count = 0

    def draw(self, width, heigth, is_active=0):
        pos = self.item_count % (len(self.item_list))
        self.item_list[pos].draw_item(self.x , self.y + 50, width, heigth, is_active)
        if pos-1 < 0:
            self.item_list[len(self.item_list)-1].draw_item(self.x -200 , self.y + 60, width, heigth, is_active)
        else:
            self.item_list[pos-1].draw_item(self.x -200 , self.y + 60, width, heigth, is_active) 
        if len(self.item_list) == pos+1:
            self.item_list[0].draw_item(self.x + 200 , self.y + 60, width, heigth, is_active)
        else:
            self.item_list[pos+1].draw_item(self.x + 200 , self.y + 60, width, heigth, is_active)

    def draw_equiped(self, width, heigth):
        self.equiped_list[0].draw_item(self.x , self.y + 50, width, heigth)

    def add_item(self, item):
        self.item_list.append(item)
    
    def add_equipped_item(self, item):
        self.equiped_list.append(item)