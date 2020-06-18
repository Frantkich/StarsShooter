from app.ressources import *

from app.classes.label import Label
from app.classes.star import Star


def controls(stars):
    run = True
    previousKey = None

    controls = []
    controls.append(Label(screen.get_width()/2, screen.get_height()
                    * 2/10, "Controls", main_color, 60))
    controls.append(Label(screen.get_width()/2, screen.get_height()
                    * 4/10, "Escape : Go back", main_color, 30))
    controls.append(Label(screen.get_width()/2, screen.get_height()
                    * 6/10, "Z, Q, S, D : Move", main_color, 30))
    controls.append(Label(screen.get_width()/2, screen.get_height()
                    * 7/10, "1, 2, 3 ... : Switch weapons", main_color, 30))
    controls.append(Label(screen.get_width()/2, screen.get_height()
                    * 8/10, "W, X, C, V : Use items", main_color, 30))
    controls.append(Label(screen.get_width()/2, screen.get_height()
                    * 9/10, "space : Shoot", main_color, 30))

    def redraw_window():
        pg.draw.rect(screen, (0, 0, 0),
                     ((0, 0), (screen.get_width(), screen.get_height())))

        for star in stars:
            star.move()
            if star.draw():
                stars.remove(star)
                stars.append(
                    Star((screen.get_width()/2, screen.get_height()/2), star.width, 1))

        for control in controls:
            control.draw()
            
    while run:
        for e in pg.event.get():
            try:
                if previousKey != e.dict['unicode']:
                    previousKey = e
                    if keyPressed("esc"):
                        run = False
                        break
            except KeyError:
                pass
        redraw_window() 
        end()

    return stars
