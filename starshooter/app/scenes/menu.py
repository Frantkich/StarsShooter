from app.ressources import *

from app.scenes.headquarter import headquarter
from app.classes.player import Player
from app.scenes.option import option
from app.classes.label import Label
from app.classes.star import Star


def menu():
    run = True
    previousKey = None

    label_active = 0
    labels = []
    labels.append(Label(screen.get_width()/2, 200, "Continue", (255, 240, 200), 50))
    labels.append(Label(screen.get_width()/2, 400, "New game", (255, 240, 200), 50))
    labels.append(Label(screen.get_width()/2, 600, "Settings", (255, 240, 200), 50))
    labels.append(Label(screen.get_width()/2, 800, "Exit", (255, 240, 200), 50))

    Label(180, 495, "S", (255, 240, 200), 200).draw()
    Label(300, 445, "TAR", (255, 240, 200), 100).draw()
    Label(380, 520, "H.Otter", (255, 240, 200), 100).draw()
    pg.display.update()
    
    change_music("credits")
    
    stars = []
    for n in range(1000):
        stars.append(Star((screen.get_width()/2, screen.get_height()/2), random.randint(0, 100)))
        for _ in range(500):
            stars[n].move()

    # pg.time.delay(2500)
    
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
                        if label_active == 0: #load game 
                            stars= headquarter(load(Player(screen.get_width()/2, screen.get_height()-screen.get_height()/4)), stars)
                        elif label_active == 1: #start a game
                            stars = headquarter(Player(screen.get_width()/2, screen.get_height()-screen.get_height()/4), stars)
                        elif label_active == 2: # open settings
                            stars =  option(stars)
                        elif label_active == 3:
                            run = False
                            break
            except KeyError:
                pass 
        redraw_window()
        end()