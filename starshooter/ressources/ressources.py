import pygame as pg
import os, random

from ressources.settings import *

pg.init()
pg.font.init()
random.seed()

dir_asset = os.path.join(os.path.dirname(__file__), 'assets')


font = os.path.join(dir_asset, "fonts/MachineStd.otf")

main_font = font = os.path.join(dir_asset, "fonts/MachineStd.otf")
hover_font = pg.font.Font(os.path.join(dir_asset, "fonts/MachineStd.otf"), 60)
title_font = pg.font.Font(os.path.join(dir_asset, "fonts/MachineStd.otf"), 100)

background = os.path.join(dir_asset, 'background-black.png') 

weapon_list = {
#              (cooldown, ((R, G, B), (size_x, size_y), damage, speed, penetration, dispertion), nBullet, (img, nbframe), price)
    'BFG':     (10,   ((0,153,51),    (20, 40), 500, 2,  -1, 0),    1,  (os.path.join(dir_asset, 'ship_yellow.png'), 4), 650),
    'laser':   (0,    ((0,204,255),   (5, 50),  5,   50, 0,  0),    1,  (os.path.join(dir_asset, 'laser.png'),       4), 800), 
    'sniper':  (1.5,  ((255,20,147),  (8, 20),  150, 15, 2,  0),    1,  (os.path.join(dir_asset, 'ship_yellow.png'), 4), 400),
    'shotgun': (1.5,  ((255,255,255), (2, 3),   25,  15, 0,  0.33), 20, (os.path.join(dir_asset, 'shotgun.png'),     4), 400), 
    'gatling': (0.15, ((255,255,102), (5, 10),  75,  10, 0,  0),    1,  (os.path.join(dir_asset, 'gatling.png'),     4), 800), 
    'missile': (2,    ((205,133,63) , (5, 5),   250, 25, 0,  1),    10, (os.path.join(dir_asset, 'missile.png'),     4), 650) 
}    


bonus = ['speed', 'damage', 'heal', 'size', 'cooldown'] 

powerup_list = {
#               ((R, G, B), time, modifier)
    'speed':    ((255, 255, 0),   3, 1.25),
    'damage':   ((128, 255, 0),   3, 1.5),
    'heal':     ((255, 0,   0),   0, 0),
    'size':     ((255, 128, 50),  3, 0.5),
    'cooldown': ((0,   255, 255), 3, 0.5),
    'slow':     ((255, 255, 0),   3, 0.5),
    'weak':     ((128, 255, 0),   3, 0.5),
    'bigboi':   ((255, 128, 50),  3, 1.25),
    'firerate': ((0,   255, 255), 3, 2)
}



parallaxe_list = {
#              (img, nbframe, speed)  
    'planet1': (os.path.join(dir_asset, 'planet1.png'), 1, 0.5),
    'planet2': (os.path.join(dir_asset, 'planet2.png'), 1, 0.5),
    'planet3': (os.path.join(dir_asset, 'planet3.png'), 1, 0.5),
    'sun': (os.path.join(dir_asset, 'sun.png'),         4, 0.5)
}


enemy_list = ['red', 'blue', 'green', 'round', 'sneaky']
boss_list = ['boss_1', 'boss_2']

spaceship_list = {
#             ((img, nbframe), (health, explosionsize, speed), (weapons1_pos, ....), price)
    'player': ((os.path.join(dir_asset, 'ship_yellow.png'), 4), (500,  70,  7.5), [(0, 0), (-17, 10), (17, 10)],                          1200),
    'red':    ((os.path.join(dir_asset, 'ship_red.png'),    4), (200,  70,  1),   [(0, 0)],                                               1200),
    'green':  ((os.path.join(dir_asset, 'ship_green.png'),  4), (150,  70,  2),   [(0, 0)],                                               1200),
    'blue':   ((os.path.join(dir_asset, 'ship_blue.png'),   4), (50,   70,  3),   [(0, 0)],                                               1200),
    'round':  ((os.path.join(dir_asset, 'ship_round.png'),  4), (100,  70,  2.5), [(0, 0)],                                               2400),
    'sneaky': ((os.path.join(dir_asset, 'ship_sneaky.png'), 4), (100,  70,  2),   [(0, 0)],                                               4000),
    'boss_1': ((os.path.join(dir_asset, 'ship_boss1.png'),  4), (5000, 125, 1),   [(-135, -100), (-55, 0), (0, 0), (55, 0), (135, -100)], 22000),
    'boss_2': ((os.path.join(dir_asset, 'ship_boss2.png'),  4), (2500, 125, 3),   [(-100, -150), (100, -150)],                            22000),
}

sound_list = {
    'boss'  : os.path.join(dir_asset, "sound", "boss.wav"),
    'end'   : os.path.join(dir_asset, "sound", "end.wav"),
    'intro' : os.path.join(dir_asset, "sound", "intro.wav")
}

pg.mixer.init(frequency=44100, size=-16, channels=2, buffer=512, devicename="mixer", allowedchanges=0)
pg.mixer.music.set_volume(0.5)