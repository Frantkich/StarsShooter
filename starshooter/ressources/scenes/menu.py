import pygame as pg
import random

from ressources.ressources import *
from ressources.settings import *
from ressources.functions import *

from ressources.classes.star import Star
from ressources.classes.label import Label
from ressources.classes.soundbarre import Soundbarre

from ressources.scenes.game import game
from ressources.scenes.option import option

from ressources.classes.player import Player

def menu():
    label_active = 0
    run = True
    previousKey = None
    labels = []
    labels.append(Label(screen.get_width()/2, 200, "New game", (255, 240, 200), 50))
    labels.append(Label(screen.get_width()/2, 400, "Load game", (255, 240, 200), 50))
    labels.append(Label(screen.get_width()/2, 600, "Settings", (255, 240, 200), 50))
    labels.append(Label(screen.get_width()/2, 800, "Exit", (255, 240, 200), 50))
        
    Label(180, 495, "S", (255, 240, 200), 200).draw()
    Label(300, 445, "TAR", (255, 240, 200), 100).draw()
    Label(380, 520, "H.Otter", (255, 240, 200), 100).draw()
    pg.display.update()

    soundbarre = Soundbarre(screen.get_width()/4, screen.get_height()* 3/10 , (4, 195, 225))

    stars = []
    change_music("generic.mp3")
    
    for n in range(1000):
        stars.append(Star((screen.get_width()/2, screen.get_height()/2), random.randint(0, 100)))
        for _ in range(500):
            stars[n].move()

    pg.time.delay(2500)
    
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
                            game(Player(0, screen.get_height()-screen.get_height()/4))
                        elif label_active == 1:
                            game(load(Player(0, screen.get_height()-screen.get_height()/4)))
                        elif label_active == 2:
                            option(soundbarre)
                        else:
                            save(player)
                            run = False
                            break
            except KeyError:
                pass

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
            
        pg.display.update()
        clock.tick(60)
        pg.display.set_caption("FPS: {}".format(int(clock.get_fps())))
        pg.draw.rect(screen, (0,0,0), ((0,0), screen.get_size()))
    pg.quit()
