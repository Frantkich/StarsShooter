import random, math, pygame, sys, os
from pygame.locals import *

from functions import *
from ressources.classes.label import Label

WINSIZE = (600, 1000)
WINCENTER = (WINSIZE[0]/2, WINSIZE[1]/2)
SCREEN = pygame.display.set_mode(WINSIZE)

MAINCHANNEL = pygame.mixer.find_channel(True)
MAINCHANNEL.play(pygame.mixer.Sound("sound.wav"))

MAINCHANNEL.set_volume()

class SoundBarre():
    
    def __init__(self, x, y, color, window):
        self.x = x
        self.y = y
        self.color = color
        self.size = (window.get_width()/2, 10)
        self.surface = pygame.Surface(self.size)
        self.logo = pygame.image.load(os.path.join("assets", "speaker.png"))
        self.volumeMixer = pygame.Surface((10, 30))
        self.volumeLevel = 0.6
        
    def draw(self, window):
        self.surface.fill(self.color)
        self.volumeMixer.fill(self.color)
        window.blit(self.surface, (self.x, self.y))    
        window.blit(self.logo, (self.x - self.logo.get_width() - 10, self.y - self.logo.get_height()/2 + self.size[1]/2))
        window.blit(self.volumeMixer, (self.x + self.size[0] * self.volumeLevel, self.y - self.volumeMixer.get_height()/2 + self.size[1]/2))


def settingsInterface(window,clock):
    run = True
    previousKey = None
    #Initialisation
    labels = []
    controls = []
    labels.append(Label(window.get_width()/2, window.get_height()* 1.5/10, "Sound", (255, 240, 200), 60)) #Sound Label
    labels.append(Label(window.get_width()/2, window.get_height()* 5/10 , "Controls", (255, 240, 200), 60))  #Controls
    controls.append(Label(window.get_width()/2, window.get_height()* 6/10 , "Z, Q, S, D : Movement", (255, 240, 200), 40))
    controls.append(Label(window.get_width()/2, window.get_height()* 7/10 , "1, 2, 3, 4 : Switch weapons", (255, 240, 200), 40))
    controls.append(Label(window.get_width()/2, window.get_height()* 8/10 , "Space : shoot / validate", (255, 240, 200), 40))
    labels.append(Label(window.get_width()/2, window.get_height()* 9/10, "Done", (255, 240, 200), 20))  #Esc 
    
    soundBarre = SoundBarre(window.get_width()/4, window.get_height()* 3/10 , (4, 195, 225), window)

    while run:
        for label in labels:
            label.draw(window)

        for control in controls:
            control.draw(window)

        soundBarre.draw(window)
        for e in pygame.event.get():
            try:
                if previousKey != e.dict['unicode']:
                    previousKey = e
                    if keyPressed("d") and soundBarre.volumeLevel < 1:
                        soundBarre.volumeLevel += 0.2

                    if keyPressed("q") and 0 < soundBarre.volumeLevel :
                        soundBarre.volumeLevel -= 0.2
                    if keyPressed("space"):
                        break
            except KeyError:
                pass        
        pygame.display.update()
        clock.tick(60)
        pygame.display.set_caption("FPS: {}".format(int(clock.get_fps())))
        pygame.draw.rect(screen, (0,0,0), ((0,0), (screen.get_width, screen.get_height) ))

def main(window):
    clock = pygame.time.Clock()
    pygame.init()
    settingsInterface(window, clock)

if __name__ == '__main__':
    main(SCREEN)