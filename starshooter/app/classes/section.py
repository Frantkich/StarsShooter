from app.ressources import *

from app.classes.label import Label


class Section():
    def __init__(self, label_text, x, y):
        self.label = Label(screen.get_width()/2, y, label_text, (255, 240, 200), 20)  #Label(self, x, y, text, color, fontSize, font=main_font)
        self.x = x
        self.y = y
        self.item_list = []
        self.equipped_list = []
        self.item_count = 0

    def draw(self, width, heigth, bias, is_active=0): 
        centerX = screen.get_width()*0.5
        offsetX = screen.get_width()*0.8 / 3
    
        if len(self.item_list) > 0:
            pos = self.item_count % (len(self.item_list))
            self.item_list[pos].draw_item(centerX - width/2 , self.y + bias, width, heigth, is_active)
            if pos-1 < 0:
                self.item_list[len(self.item_list)-1].draw_item(centerX - offsetX - width/2, self.y + bias, width, heigth, is_active)
            else:
                self.item_list[pos-1].draw_item(centerX - offsetX - width/2, self.y + bias, width, heigth, is_active) 
            if len(self.item_list) == pos+1:
                self.item_list[0].draw_item(centerX + offsetX - width/2, self.y + bias, width, heigth, is_active)
            else:
                self.item_list[pos+1].draw_item(centerX + offsetX - width/2, self.y + bias, width, heigth, is_active)

    def draw_equipped(self, width, heigth, is_active=0):
        offsetX = 0
        centerX = screen.get_width()*0.5 / len(self.equipped_list)
        for item in self.equipped_list:
                item.draw_item(offsetX + centerX - width/2, self.y + 60, width, heigth, is_active)
                offsetX += screen.get_width()*0.8 / len(self.equipped_list)

    def add_item(self, item):
        self.item_list.append(item)
    
    def add_equipped_item(self, item):
        self.equipped_list.append(item)
