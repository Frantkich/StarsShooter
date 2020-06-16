import pygame as pg

from ressources.ressources import *
from ressources.settings import *
from ressources.functions import *

from ressources.classes.label import Label
from ressources.classes.shop_section import Shop_section
from ressources.classes.shop_item import Shop_item

def shop():

    label_active = 0
    run = True
    previousKey = None
    
    shop_section = []  #Shop_section(self, label_y, label_text, x, y, width, height)

    #shop_section.append(Shop_section(screen.get_height()* 0.6/10, "Power-ups", screen.get_width()*1/3, screen.get_height()* 0.6/10))
    shop_section.append(Shop_section(screen.get_height()* 3.8/10 , "Weapons", screen.get_width()*1/3, screen.get_height()* 3.8/10))
    shop_section.append(Shop_section(screen.get_height()* 7/10 , "Ships", screen.get_width()*1/3, screen.get_height()* 7/10))

    for weapon in weapon_list:
        shop_section[0].add_shop_item(Shop_item(weapon, "100", weapon_list[weapon][3]))

    for ship in spaceship_list:
        shop_section[1].add_shop_item(Shop_item(ship, "100", spaceship_list[ship][0]))

    while run:
        for n in range(len(shop_section)):
            if n == label_active:
                shop_section[n].draw(1)
                shop_section[n].label.draw(1)  #Display label
            else:
                shop_section[n].draw(0)
                shop_section[n].label.draw(0)

        for e in pg.event.get():
            try:
                if previousKey != e.dict['unicode']:
                    previousKey = e
                    if keyPressed("s"):
                        label_active += 1

                    if keyPressed("z"):
                        label_active -= 1

                    if label_active < 0:
                        label_active = len(shop_section)-1

                    elif len(shop_section)-1 < label_active:
                        label_active = 0

                    if keyPressed("d"):
                        shop_section[label_active].item_count += 1

                    if keyPressed("q"):
                        shop_section[label_active].item_count -= 1


            except KeyError:
                pass

        pg.display.update()
        clock.tick(60)
        pg.display.set_caption("FPS: {}".format(int(clock.get_fps())))
        pg.draw.rect(screen, (0,0,0), ((0,0), (screen.get_width(), screen.get_height()) ))
