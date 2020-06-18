from app.ressources import *

from app.classes.section import Section
from app.classes.label import Label
from app.classes.star import Star
from app.classes.item import Item


def inventory(player, stars):
    run = True
    previousKey = None

    section_active = 0
    section = []
    section.append(Section("Power-ups", 0, screen.get_height()* 0.3/10))
    section.append(Section("Weapons", 0, screen.get_height()* 2.8/10))
    section.append(Section("Ships", 0, screen.get_height()* 6.5/10))

    for name in item_list:  #Gestion des bonus
        section[0].add_equipped_item(Item(name, powerup_list[name][0], str(player.inventory[name]))) 

    for weapon in player.inventory['weapons']:
        section[1].add_item(Item(weapon[1], weapon_list[weapon[1]][3]))
 
    
    for ship in player.inventory['ships']:
        section[2].add_item(Item(ship, spaceship_list[ship][0]))


    def weapon_equipped():
        section[1].equipped_list = []
        for n, weapon in enumerate(player.weapons):  #Armes équipées
            if weapon.weapon:
                section[1].add_equipped_item(Item(weapon.weapon, weapon_list[weapon.weapon][3], str(n+1)))
            else:
                section[1].add_equipped_item(Item(weapon.weapon, None, str(n+1)))

    def ship_equipped(ship):
        player.init_ship(ship)
        weapon_equipped()
        section[2].equipped_list = []
        section[2].add_equipped_item(Item(player.name, spaceship_list[player.name][0]))

    weapon_equipped()
    section[2].add_equipped_item(Item(player.name, spaceship_list[player.name][0]))

    def redraw_window():
        pg.draw.rect(screen, (0,0,0), ((0,0), (screen.get_width(), screen.get_height())))

        for star in stars:
            star.move()
            if star.draw():
                stars.remove(star)
                stars.append(Star((screen.get_width()/2, screen.get_height()/2), star.width, 1))

        for n in range(len(section)):
            if n == section_active:
                section[n].draw_equipped(100, 100, 1)
                section[n].draw(100, 100, 200, 1)
            else:
                section[n].draw_equipped(80, 80, 0)
                section[n].draw(80, 80, 180, 0)

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

                    if section_active == 1:
                        try :
                            pos = e.dict['key']-49
                            if 0 <= pos < len(player.weapons):
                                player.weapons[pos].change_weapon(section[1].item_list[section[1].item_count % (len(section[1].item_list))].item_name)
                                weapon_equipped()
                        except KeyError:
                            pass
                    if section_active == 2 and keyPressed('space'):
                        ship_equipped(section[2].item_list[section[2].item_count % (len(section[2].item_list))].item_name)
                    if keyPressed("esc"):
                        run = False
            except KeyError:
                pass
        redraw_window()
        end()
    return stars
