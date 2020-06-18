from app.ressources import *

from app.classes.section import Section
from app.classes.label import Label
from app.classes.item import Item
from app.classes.star import Star

def credits(stars):
    run = True
    previousKey = None

    labels= []
    labels.append(Label(screen.get_width()/2, screen.get_height(), "Credits", main_color, 70))  #self, x, y, text, color, fontSize, font=main_font
    labels.append(Label(screen.get_width()/2, screen.get_height()* 1.2, "STAR H.Otter", main_color, 70))
    labels.append(Label(screen.get_width()/2, screen.get_height()* 1.5, "Developped  by", main_color, 50))
    labels.append(Label(screen.get_width()/2, screen.get_height()* 1.6, "O.Charlon  &  F.Guern", main_color, 40))
    labels.append(Label(screen.get_width()/2, screen.get_height()* 1.9, "Game  designed  by", main_color, 50))
    labels.append(Label(screen.get_width()/2, screen.get_height()* 2, "F.Guern", main_color, 40))
    labels.append(Label(screen.get_width()/2, screen.get_height()* 2.3, "Music  by", main_color, 50))
    labels.append(Label(screen.get_width()/2, screen.get_height()* 2.4, "Bizoo", main_color, 40))
    labels.append(Label(screen.get_width()/2, screen.get_height()* 2.7, "Sprites  by", main_color, 50))
    labels.append(Label(screen.get_width()/2, screen.get_height()* 2.8, "BarbeRousse,  Fess,", main_color, 40))
    labels.append(Label(screen.get_width()/2, screen.get_height()* 2.85, "F.Guern  &  Pomz.er", main_color, 40))

    def redraw_window():
        pg.draw.rect(screen, (0,0,0), ((0,0), (screen.get_width(), screen.get_height())))
        
        for star in stars:
            star.move()
            if star.draw():
                stars.remove(star)
                stars.append(Star((screen.get_width()/2, screen.get_height()/2), star.width, 1))

        for label in labels:
            label.move(y=-1)
            label.draw()
            
        pg.display.update()
    
    while run:
        for e in pg.event.get():
            try:
                if previousKey != e.dict['unicode']:
                    previousKey = e

                    if keyPressed("esc"):
                        run = False

            except KeyError:
                pass
        if labels[-1].y <= 200:
            run = False
        redraw_window()
        end()
    
    return stars