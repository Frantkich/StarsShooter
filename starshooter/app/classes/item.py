from app.ressources import *

from app.classes.label import *


class Item():

    def __init__(self, item_name, item_img, price_or_qt):  #price_or_qt can be a price for shop and a quantity for inventory
        self.pos = [] #x and y
        self.path, self.nbframe = item_img[0], item_img[1]
        self.item_stat = [item_name, price_or_qt]
        self.labels = []
        self.img = pg.transform.scale(pg.image.load(self.path), (120, 120))
        self.init_sprites(self.img)

    def init_sprites(self, img):
        self.sprites = spritesheet(img, self.nbframe)
        self.sprite = self.sprites[0]
        self.frame = 0
        self.nextFrame = 0

    def update_sprite(self):
        if self.nextFrame == 0:
            self.frame = (self.frame + 1) % self.nbframe
            self.sprite = self.sprites[self.frame]
            self.nextFrame = gif_speed
        self.nextFrame -= 1

    def draw_item(self, x, y, width, heigth):
        self.pos = [x, y]
        self.labels.clear()
        self.labels.append(Label(self.pos[0] + screen.get_width()/4, self.pos[1] + self.img.get_height()*5/4, self.item_stat[0], (255, 240, 200), 30))
        self.labels.append(Label(self.pos[0] + 65, self.pos[1] -10, self.item_stat[1], (255, 240, 200), 25))
        
        self.update_sprite()
        self.sprite = pg.transform.scale(self.sprite, (width, heigth))
        screen.blit(self.sprite, (self.pos[0]+ 50, self.pos[1]))
        #pg.draw.rect(self.sprite, (255, 240, 200), [self.pos[0], self.pos[1], 10, 10])

        self.labels[0].draw()
        self.labels[1].draw()
        
    