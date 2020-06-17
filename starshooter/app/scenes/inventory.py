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

    inventory_section.append(Section("power-ups", screen.get_width()*1/3, screen.get_height()* 0.6/10))
    inventory_section.append(Section( "Weapons", screen.get_width()*1/3, screen.get_height()* 3.8/10))
    inventory_section.append(Section("Ships", screen.get_width()*1/3, screen.get_height()* 7/10))

    for name in bonus_names:  #Gestion des bonus
        inventory_section[0].add_item(Item(name, powerup_list[name][image], item_quantity=player.inventory[name])) #Récuperer nom image
    
    inventory_section[2].add_equipped_item(Item(str(player.name) + ": equiped", spaceship_list[player.name][0], str(player.inventory['ships'].count(player.name))))  #Item(self, item_name, item_img, price_or_qt)
    
    #print(type(player.weapons[0].weapon))

    for weapon in player.weapons:  #Armes équipées
        if weapon.weapon:
            inventory_section[1].add_equipped_item(Item(weapon.weapon, weapon_list[weapon.weapon][3], str(player.inventory['weapons'].count(weapon.weapon))))

    while run:

        for item in inventory_section[1].equipped_list:
            item.draw_item(100, 100, 100, 100)
           

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