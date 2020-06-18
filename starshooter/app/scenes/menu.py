from app.ressources import *

from app.scenes.headquarter import headquarter
from app.classes.player import Player
from app.scenes.option import option
from app.scenes.credits import credits
from app.classes.label import Label
from app.classes.star import Star


def menu():
    run = True
    previousKey = None

    change_music("intro")

    label_active = 0
    labels = []
    labels.append(Label(screen.get_width()/2, 160, "Continue", main_color, 50))
    labels.append(Label(screen.get_width()/2, 320, "New game", main_color, 50))
    labels.append(Label(screen.get_width()/2, 600, "Settings", main_color, 50))
    labels.append(Label(screen.get_width()/2, 750, "Credits", main_color, 50))
    labels.append(Label(screen.get_width()/2, 900, "Exit", main_color, 50))

    Label(180, 495, "S", main_color, 200).draw()
    Label(300, 445, "TAR", main_color, 100).draw()
    Label(380, 520, "H.Otter", main_color, 100).draw()
    
    
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
                        elif label_active == 3: # open credits
                            stars =  credits(stars)
                        elif label_active == 4:
                            run = False
                            break
            except KeyError:
                pass 
        redraw_window()
        end()