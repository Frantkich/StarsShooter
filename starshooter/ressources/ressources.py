import pygame as pg
import os, random

from ressources.settings import *

pg.font.init()
random.seed()

dir_asset = os.path.join(os.path.dirname(__file__), 'assets')


font = os.path.join(dir_asset, "fonts/MachineStd.otf")

main_font = font = os.path.join(dir_asset, "fonts/MachineStd.otf")
hover_font = pg.font.Font(os.path.join(dir_asset, "fonts/MachineStd.otf"), 60)
title_font = pg.font.Font(os.path.join(dir_asset, "fonts/MachineStd.otf"), 100)

background = os.path.join(dir_asset, 'background-black.png') 

weapon_list = {
#              (cooldown, ((R, G, B), (size_x, size_y), damage, speed, penetration, dispertion))
    'BFG':     (10,  ((0, 153, 51),    (20, 40),  500,  2,  -1, 0)),
    'rayon':   (0,   ((0, 204, 255),   (5, 1),   500,  0,  0,  0)),
    'sniper':  (1.5, ((255, 102, 0),   (8, 20),   150,  15, 2,  0)),
    'blaster': (0.5, ((255, 255, 102), (8, 10),   75,   10, 0,  0)),
    'missile': (0.5, ((255, 255, 102), (5, 5),    10,   25, 0,  1))
}


powerup_list = {
#               ((R, G, B), time, modifier)
    'speed':    ((255, 255, 0),   10, 1.25),
    'damage':   ((128, 255, 0),   10, 2),
    'heal':     ((255, 0,   0),   0,  0),
    'size':     ((255, 128, 50),  10, 0.5),
    'cooldown': ((0,   255, 255), 10, 0.25)
}


enemy_list = ['red', 'blue', 'green', 'round', 'sneaky']
boss_list = ['boss_1', 'boss_2']

spaceship_list = {
#             ((img, nbframe), health, speed, (weapons1_pos, ....))
    'player': ((os.path.join(dir_asset, 'ship_yellow.png'), 4), (500, 7.5),  [(0, 0), (-17, 0), (17, 0)]),
    'red':    ((os.path.join(dir_asset, 'ship_red.png'),    4), (200, 1),    [(0, 0)]),
    'green':  ((os.path.join(dir_asset, 'ship_green.png'),  4), (150, 2),    [(0, 0)]),
    'blue':   ((os.path.join(dir_asset, 'ship_blue.png'),   4), (50,  3),    [(0, 0)]),
    'round':  ((os.path.join(dir_asset, 'ship_round.png'),  4), (100,  2.5), [(0, 0)]),
    'sneaky': ((os.path.join(dir_asset, 'ship_sneaky.png'), 4), (100,  2),   [(0, 0)]),
    'boss_1': ((os.path.join(dir_asset, 'ship_boss1.png'),  4), (5000, 1),   [(-135, -100), (-55, 0), (0, 0), (55, 0), (135, -100)]),
    'boss_2': ((os.path.join(dir_asset, 'ship_boss2.png'),  4), (2500, 3),   [(-100, -100), (100, -100)]),
}

sound_list = {
    'test1' : os.path.join(dir_asset, "sound", "test1.wav"),
    'test2' : os.path.join(dir_asset, "sound", "test2.wav")
}

pg.mixer.init(frequency=44100, size=-16, channels=2, buffer=512, devicename="mixer", allowedchanges=0)