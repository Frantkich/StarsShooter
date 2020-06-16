import pygame as pg

from ressources.ressources import *
from ressources.settings import *
from ressources.functions import *

from ressources.classes.label import Label
from ressources.classes.section import Section
from ressources.classes.item import Item
from ressources.classes.star import Star


def shop(player, stars):
    run = True
    previousKey = None

    section_active = 0
    section = []
    section.append(Section(screen.get_height()* 3.8/10 , "Weapons", screen.get_width()*1/3, screen.get_height()* 3.8/10))
    section.append(Section(screen.get_height()* 7/10 , "Ships", screen.get_width()*1/3, screen.get_height()* 7/10))

    for weapon in weapon_list:
        section[0].add_item(Item(weapon, str(weapon_list[weapon][4]), weapon_list[weapon][3]))
    for ship in spaceship_list:
        section[1].add_item(Item(ship, str(spaceship_list[ship][3]), spaceship_list[ship][0]))

    def redraw_window():
        pg.draw.rect(screen, (0,0,0), ((0,0), (screen.get_width(), screen.get_height())))
        for star in stars:
            star.move()
            if star.draw():
                stars.remove(star)
                stars.append(Star((screen.get_width()/2, screen.get_height()/2), star.width, 1))

        for n in range(len(section)):
            if n == section_active:
                section[n].draw(1)
                section[n].label.draw(1)
            else:
                section[n].draw(0)
                section[n].label.draw(0)

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
                        section[section_active].item_count += 1
                    if keyPressed("q"):
                        section[section_active].item_count -= 1
                    if keyPressed("esc"):
                        run = False
            except KeyError:
                pass
            
        redraw_window()
        end()
        
    return stars