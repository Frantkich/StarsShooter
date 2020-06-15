import pygame as pg

from ressources.ressources import *
from ressources.settings import *
from ressources.functions import *

from ressources.classes.soundbarre import Soundbarre  
from ressources.classes.label import Label

def option(soundbarre):
    run = True
    previousKey = None
    
    labels = []
    controls = []
    labels.append(Label(screen.get_width()/2, screen.get_height()* 1.5/10, "Sound", (255, 240, 200), 60)) #Sound Label
    labels.append(Label(screen.get_width()/2, screen.get_height()* 5/10 , "Controls", (255, 240, 200), 60))  #Controls
    controls.append(Label(screen.get_width()/2, screen.get_height()* 6/10 , "Z, Q, S, D : Movement", (255, 240, 200), 40))
    controls.append(Label(screen.get_width()/2, screen.get_height()* 7/10 , "1, 2, 3 ... : Switch weapons", (255, 240, 200), 40))
    controls.append(Label(screen.get_width()/2, screen.get_height()* 8/10 , "Space : shoot", (255, 240, 200), 40))
    labels.append(Label(screen.get_width()/2, screen.get_height()* 9/10, "Escape : Done", (255, 240, 200), 40))  #Esc 
    
    while run:
        for label in labels:
            label.draw()

        for control in controls:
            control.draw()

        soundbarre.draw()
        for e in pg.event.get():
            try:
                if previousKey != e.dict['unicode']:
                    previousKey = e
                    if keyPressed("d") and soundbarre.volumeLevel < 10:
                        soundbarre.up_volumeLevel()
                        pg.mixer.music.set_volume(soundbarre.volumeLevel/10)
                    if keyPressed("q") and 0 < soundbarre.volumeLevel:
                        soundbarre.down_volumeLevel()
                        pg.mixer.music.set_volume(soundbarre.volumeLevel/10)
                    if keyPressed("f"):  #Test son
                        pg.mixer.Sound(sound_list['boss']).play()
                    if keyPressed("g"): #test son
                        pg.mixer.Sound(sound_list['end']).play()
                    if keyPressed('esc'):
                            run = False
            except KeyError:
                pass        

        pg.display.update()
        clock.tick(60)
        pg.display.set_caption("FPS: {}".format(int(clock.get_fps())))
        pg.draw.rect(screen, (0,0,0), ((0,0), (screen.get_width(), screen.get_height()) ))
