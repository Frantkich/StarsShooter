from app.ressources import *

from app.scenes.inventory import inventory
from app.classes.label import Label
from app.classes.star import Star
from app.scenes.game import game
from app.scenes.shop import shop


def headquarter(player, stars):
    run = True
    previousKey = None

    label_active = 0
    labels = []
    labels.append(Label(screen.get_width()/2, 200, "Start", (255, 240, 200), 50))
    labels.append(Label(screen.get_width()/2, 400, "Inventory", (255, 240, 200), 50))
    labels.append(Label(screen.get_width()/2, 600, "Shop", (255, 240, 200), 50))
    labels.append(Label(screen.get_width()/2, 800, "Save & Exit", (255, 240, 200), 50))
    
    change_music("transition")

    def redraw_window():
        pg.draw.rect(screen, (0,0,0), ((0,0), (screen.get_width(), screen.get_height())))

        for star in stars:
            star.move()
            if star.draw():
                stars.remove(star)
                stars.append(Star((screen.get_width()/2, screen.get_height()/2), star.width, 1))

        for n in range(len(labels)):
            if n == label_active:
                labels[n].draw(1)
            else:
                labels[n].draw()

    while run:
        for e in pg.event.get():
            try:
                if previousKey != e.dict['unicode']:
                    previousKey = e

                    if keyPressed("s"):
                        label_active += 1
                    if keyPressed("z"):
                        label_active -= 1
                    if label_active < 0:
                        label_active = len(labels)-1
                    elif len(labels)-1 < label_active:
                        label_active = 0

                    if keyPressed("space"):
                        if label_active == 0:
                            game(player) #start the game
                        elif label_active == 1:
                            stars = inventory(player, stars) #open the inventory
                        elif label_active == 2:
                            stars = shop(player, stars)
                        elif label_active == 3:
                            save(player)
                            run = False
                            break
            except KeyError:
                pass

        redraw_window()
        end()

    return stars