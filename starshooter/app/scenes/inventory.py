from app.ressources import *

from app.classes.section import Section
from app.classes.label import Label
from app.classes.item import Item


def inventory(player):
    section_active = 0
    run = True
    previousKey = None
        
    inventory_section = [] #Sectiona
    bonus_names = ['slow', 'weak', 'bigboi', 'firerate']

    inventory_section.append(Section("power-ups", screen.get_width()*1/3, screen.get_height()* 0.6/10))
    inventory_section.append(Section( "Weapons", screen.get_width()*1/3, screen.get_height()* 3.8/10))
    inventory_section.append(Section("Ships", screen.get_width()*1/3, screen.get_height()* 7/10))

    for name in bonus_names:  #Gestion des bonus
        inventory_section[0].add_item(Item(name, powerup_list[name][0], str(player.inventory[name]))) 
    
    for weapon in player.weapons:  #Armes équipées
        if weapon.weapon:
            inventory_section[1].add_equipped_item(Item(weapon.weapon, weapon_list[weapon.weapon][3], str(player.inventory['weapons'].count(weapon.weapon))))
    
    inventory_section[2].add_equipped_item(Item(player.name, spaceship_list[player.name][0], str(player.inventory['ships'].count(player.name))))  #Item(self, item_name, item_img, price_or_qt)

    while run:
        for n in range(len(inventory_section)):
            print(n)
            if n > 0:
                inventory_section[n].label.draw(1)
                for item in inventory_section[n].equipped_list:
                    item.draw_item(100, 100, 100, 100)
            else:
                inventory_section[n].label.draw(0)
                inventory_section[n].draw(120, 120)
           

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
