from app.ressources import *

from app.classes.soundbarre import Soundbarre  
from app.classes.label import Label
from app.classes.star import Star


def option(stars):
    run = True
    previousKey = None
    
    label_active = 0
    labels = []
    labels.append(Label(screen.get_width()/2, screen.get_height()* 1/10, "Sound", main_color, 50))
    labels.append(Label(screen.get_width()/2, screen.get_height()* 3/10, "Done", main_color, 50))

    controls = []
    controls.append(Label(screen.get_width()/2, screen.get_height()* 6/10 , "Controls", main_color, 50))
    controls.append(Label(screen.get_width()/2, screen.get_height()* 7/10 , "Z, Q, S, D : Move", main_color, 30))
    controls.append(Label(screen.get_width()/2, screen.get_height()* 8/10 , "1, 2, 3 ... : Switch weapons", main_color, 30))
    controls.append(Label(screen.get_width()/2, screen.get_height()* 9/10 , "space : Shoot", main_color, 30))
    
    soundbarre = Soundbarre(screen.get_width()/4, screen.get_height()* 2/10 , (4, 195, 225))

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

        for control in controls:
            control.draw()

        soundbarre.draw()

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

                    if label_active == 0:
                        if keyPressed("d") and pg.mixer.music.get_volume() < 1:
                            soundbarre.volumeUp()
                        if keyPressed("q") and 0 < pg.mixer.music.get_volume():
                            soundbarre.volumeDown()
                    if keyPressed("space") and label_active == 1:
                            run = False
                            break

            except KeyError:
                pass
        
        redraw_window()
        end()

    return stars
