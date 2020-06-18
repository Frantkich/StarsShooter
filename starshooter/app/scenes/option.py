from app.ressources import *

from app.classes.soundbarre import Soundbarre  
from app.classes.label import Label
from app.classes.star import Star

from app.scenes.controls import controls

def option(stars):
    run = True
    previousKey = None
    
    label_active = 0
    labels = []
    labels.append(Label(screen.get_width()/2, screen.get_height()* 2/10, "Sound", main_color, 50))
    labels.append(Label(screen.get_width()/2, screen.get_height()* 6/10, "Controles", main_color, 50))
    labels.append(Label(screen.get_width()/2, screen.get_height()* 8/10, "Done", main_color, 50))

    
    soundbarre = Soundbarre(screen.get_width()/4, screen.get_height()* 3/10 , (4, 195, 225))

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
                    if keyPressed("space"):
                        if label_active == 1:
                            stars = controls(stars)
                        if label_active == 2:
                            run = False
                            break
            except KeyError:
                pass
        
        redraw_window()
        end()

    return stars
