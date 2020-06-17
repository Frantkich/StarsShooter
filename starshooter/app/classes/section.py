from app.ressources import *

from app.classes.label import Label


class Section():
    def __init__(self, label_text, x, y):
        self.label = Label(screen.get_width()/2, y, label_text, (255, 240, 200), 30)  #Label(self, x, y, text, color, fontSize, font=main_font)
        self.x = x
        self.y = y
        self.item_list = []
        self.equipped_list = []
        self.item_count = 0

    def draw(self, width, heigth):
        pos = self.item_count % (len(self.item_list))
        self.item_list[pos].draw_item(self.x , self.y + 50, width, heigth)
        if pos-1 < 0:
            self.item_list[len(self.item_list)-1].draw_item(self.x -200 , self.y + 60, width, heigth)
        else:
            self.item_list[pos-1].draw_item(self.x -200 , self.y + 60, width, heigth) 
        if len(self.item_list) == pos+1:
            self.item_list[0].draw_item(self.x + 200 , self.y + 60, width, heigth)
        else:
            self.item_list[pos+1].draw_item(self.x + 200 , self.y + 60, width, heigth)

    def add_item(self, item):
        self.item_list.append(item)
    
    def add_equipped_item(self, item):
        self.equipped_list.append(item)
