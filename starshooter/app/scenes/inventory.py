from app.ressources import *

from app.classes.section import Section
from app.classes.label import Label
from app.classes.item import Item


def inventory(player):
    label_active = 0
    run = True
    previousKey = None
    
    inventory_section = [] #Section
    bonus_names = ['slow', 'weak', 'bigboi', 'firerate']

    inventory_section.append(Section(screen.get_height()* 0.6/10, "power-ups", screen.get_width()*1/3, screen.get_height()* 0.6/10))
    inventory_section.append(Section(screen.get_height()* 3.8/10 , "Weapons", screen.get_width()*1/3, screen.get_height()* 3.8/10))
    inventory_section.append(Section(screen.get_height()* 7/10 , "Ships", screen.get_width()*1/3, screen.get_height()* 7/10))

    #for name in bonus_names:  #Gestion des bonus
    #    inventory_section[0].add_item(Item(name, powerup_list[name][image], item_quantity=player.inventory[name])) #Récuperer nom image
    #print(spaceship_list[player.name])
    inventory_section[2].add_equiped_item(Item(str(player.name) + ": equiped", spaceship_list[player.name][0], str(player.inventory['ships'].count(player.name)) ))  #Item(self, item_name, item_img, price_or_qt)
    
    for weapon in player.weapons:  #Armes équipées
        if weapon:
            inventory_section[1].add_equiped_item(Item(weapon, weapon_list[weapon][4], str(player.inventory['weapons'].count(weapon)) ))

    while run:
        
        #inventory_section[2].draw_equiped(100, 100)
        #inventory_section[2][0].draw_equiped(100, 100)

        for item in inventory_section[1]:
            item.draw_equiped(100, 100)
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