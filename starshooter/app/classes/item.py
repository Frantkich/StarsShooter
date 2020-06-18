from app.ressources import *

from app.classes.label import *


class Item():
    def __init__(self, item_name, item_img=None, price_or_qt=None):
        if item_img:
            self.path, self.nbframe = item_img
        else:
            self.path, self.nbframe = empty_sprite
            
        self.item_name = item_name
        self.price_or_qt = price_or_qt
        self.color = (255, 240, 200)
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

    def draw_item(self, x, y, width, heigth, is_active=0):
        self.update_sprite()
        self.sprite = pg.transform.scale(self.sprite, (width, heigth))
        screen.blit(self.sprite, (x, y))
        
        Label(x + width, y + 1.1* heigth, self.item_name, self.color, 20).draw(is_active)
        if self.price_or_qt:
            Label(x + 65, y -10, self.price_or_qt, self.color, 20).draw(is_active)
    