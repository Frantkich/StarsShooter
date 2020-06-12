import pygame as pg
import os

dir_asset = os.path.join(os.path.dirname(__file__), 'assets') 

BG = pg.transform.scale(pg.image.load(os.path.join(dir_asset, 'background-black.png')), (650, 1000))


weapon_list = {
#              [cooldown, ((R, G, B), (size_x, size_y), speed, damage, penetration)]
    'BFG':     [10,  ((0, 153, 51),    (20, 40), 500,  5, -1)],
    'laser':   [0,   ((0, 204, 255),   (5, 25),  5,    25, 0)],
    'sniper':  [1.5, ((255, 102, 0),   (8, 20),  150,  20, 2)],
    'blaster': [0.5, ((255, 255, 102), (8, 10),  75,   20, 0)]
}


powerup_list = {
#            [(R, G, B), time, modifier]
    'speed':    ((255, 255, 0),  10, 1.25),
    'damage':   ((128, 255, 0),  10, 2),
    'heal':     ((255, 0, 0),    0,  0),
    'size':     ((255, 128, 50), 10, 0.5),
    'cooldown': ((0, 255, 255),  10, 0.25)
}


spaceship_list = {
#             (img, nbframe, health, speed, weapon_slot_max)
    'player': (os.path.join(dir_asset, 'ship_yellow.png'), 4, 500, 7.5, 4),
    'red':    (os.path.join(dir_asset, 'ship_red.png'),    4, 200, 1,   4),
    'green':  (os.path.join(dir_asset, 'ship_green.png'),  4, 150, 2,   2),
    'blue':   (os.path.join(dir_asset, 'ship_blue.png'),   4, 50,  4,   1)
}