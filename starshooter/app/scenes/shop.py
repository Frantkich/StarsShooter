from app.ressources import *

from app.classes.section import Section
from app.classes.label import Label
from app.classes.item import Item
from app.classes.star import Star


def shop(player, stars):
    run = True
    previousKey = None

    section_active = 0
    section = []
    section.append(Section("Power-up", screen.get_width()*1/3, screen.get_height()* 1/10))
    section.append(Section("Weapons", screen.get_width()*1/3, screen.get_height()* 3.8/10))
    section.append(Section("Ships", screen.get_width()*1/3, screen.get_height()* 7/10))

    for bonus in item_list:
        section[0].add_item(Item(bonus, powerup_list[bonus][0], str(powerup_list[bonus][3])))

    for weapon in weapon_list:
        section[1].add_item(Item(weapon, weapon_list[weapon][3], str(weapon_list[weapon][4])))

    for ship in spaceship_list:
        section[2].add_item(Item(ship, spaceship_list[ship][0], str(spaceship_list[ship][3])))

    def redraw_window():
        pg.draw.rect(screen, (0,0,0), ((0,0), (screen.get_width(), screen.get_height())))
        for star in stars:
            star.move()
            if star.draw():
                stars.remove(star)
                stars.append(Star((screen.get_width()/2, screen.get_height()/2), star.width, 1))

        for n in range(len(section)):
            if n == section_active:
                section[n].draw(150, 150, 1)
                section[n].label.draw(1)
            else:
                section[n].draw(120, 120)
                section[n].label.draw()

        Label(screen.get_width()*0.85, 30, '$ : {}'.format(player.money), (255, 240, 200), 30).draw()

    def buy(item, price):
        if price <= player.money:
            player.money -= price
            if item in item_list:
                player.inventory[item] += 1
            if item in spaceship_list:
                player.inventory['ships'].append(item)
            if item in weapon_list:
                for el in player.inventory['weapons']:
                    if item == el[1]:
                        el[0] += 1
                        return
                player.inventory['weapons'].append([1, item])
        else:
            print('u r broke...')


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
                    if keyPressed("space"):
                        for n in range(3):
                            if section_active == n:
                                item = section[n].item_list[section[n].item_count % (len(section[n].item_list))]
                                buy(item.item_name, int(item.price_or_qt))
                    if keyPressed("esc"):
                        run = False
            except KeyError:
                pass

        redraw_window()
        end()
        
    return stars