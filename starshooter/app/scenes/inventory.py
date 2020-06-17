from app.ressources import *

from app.classes.section import Section
from app.classes.label import Label
from app.classes.item import Item


def inventory(player):
    run = True
    previousKey = None

    section_active = 0
    section = []
    section.append(Section("Power-ups", screen.get_width()*1/3, screen.get_height()* 0.6/10))
    section.append(Section("Weapons", screen.get_width()*1/3, screen.get_height()* 3.8/10))
    section.append(Section("Ships", screen.get_width()*1/3, screen.get_height()* 7/10))

    for name in item_list:  #Gestion des bonus
        section[0].add_equipped_item(Item(name, powerup_list[name][0], str(player.inventory[name]))) 
    
    for weapon in player.weapons:  #Armes équipées
        if weapon.weapon:
            section[1].add_equipped_item(Item(weapon.weapon, weapon_list[weapon.weapon][3]))
        else:
            section[1].add_equipped_item(Item(weapon.weapon))
    section[2].add_equipped_item(Item(player.name, spaceship_list[player.name][0]))

    def redraw_window():
        for n in range(len(section)):
            if n == section_active:
                section[n].draw_equipped(150, 150, 1)
                section[n].label.draw(1)
            else:
                section[n].draw_equipped(120, 120)
                section[n].label.draw()
        pg.display.update()

    while run:
        for e in pg.event.get():
            try:
                if previousKey != e.dict['unicode']:
                    previousKey = e
                    if keyPressed("s"):
                        section_active += 1

                    if keyPressed("z"):
                        section_active -= 1

                    if section_active < 0:
                        section_active = len(section)-1

                    elif len(section)-1 < section_active:
                        section_active = 0

                    if keyPressed("d"):
                        section[section_active].section += 1

                    if keyPressed("q"):
                        section[section_active].section -= 1

                    if keyPressed("esc"):
                        run = False

            except KeyError:
                pass

        redraw_window()
        end()
        
