import pygame as pg

from ressources.ressources import *
from ressources.settings import *
from ressources.functions import *

from ressources.classes.label import Label
from ressources.classes.section import Section
from ressources.classes.item import Item

def inventory():
    label_active = 0
    run = True
    previousKey = None
    
    inventory_section = [] #Section
    bonus_names = ['slow', 'weak', 'bigboi', 'firerate']

    inventory_section.append(Section(screen.get_height()* 0.6/10, "Power-ups", screen.get_width()*1/3, screen.get_height()* 0.6/10))
    inventory_section.append(Section(screen.get_height()* 3.8/10 , "Weapons", screen.get_width()*1/3, screen.get_height()* 3.8/10))
    inventory_section.append(Section(screen.get_height()* 7/10 , "Ships", screen.get_width()*1/3, screen.get_height()* 7/10))

    for name in bonus_names:  #Gestion des bonus
        inventory_section[0].add_item(Item(name, powerup_list[name][image], item_quantity=player.inventory[name])) #Récuperer nom image

    inventory_section[1].add_equiped_item(Item(player.name), spaceship_list[player.name])  #Vaisseau équipé

    for weapon in player.self.weapons:  #Armes équipé
        inventory_section[2].add_equiped_item(weapon)

    while run:
        for n in range(len(inventory_section)):
            if n == label_active:
                #inventory_section[n].draw(1)
                inventory_section[n].label.draw(1)  #Display label
            else:
                #inventory_section[n].draw(0)
                inventory_section[n].label.draw(0)

        for e in pg.event.get():
            try:
                if previousKey != e.dict['unicode']:
                    previousKey = e
                    if keyPressed("s"):
                        label_active += 1

                    if keyPressed("z"):
                        label_active -= 1

                    if label_active < 0:
                        label_active = len(inventory_section)-1

                    elif len(inventory_section)-1 < label_active:
                        label_active = 0

                    if keyPressed("d"):
                        shop_section[label_active].item_count += 1

                    if keyPressed("q"):
                        shop_section[label_active].item_count -= 1

                    if keyPressed("esc"):
                        run = False

            except KeyError:
                pass

        pg.display.update()
        clock.tick(60)
        pg.display.set_caption("FPS: {}".format(int(clock.get_fps())))
        pg.draw.rect(screen, (0,0,0), ((0,0), (screen.get_width(), screen.get_height()) ))