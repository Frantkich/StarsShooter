import pygame as pg
import os

dir_asset = os.path.join(os.path.dirname(__file__), 'assets') 

BG = pg.transform.scale(pg.image.load(os.path.join(dir_asset, 'background-black.png')), (650, 1000))


weapon_list = {
#              [cooldown, ((R, G, B), (size_x, size_y), speed, damage, penetration)]
    'BFG':     [10,  ((0, 153, 51),   (20, 40), 500, 5, -1)],
    'laser':   [0,   ((0, 204, 255),  (5, 25),  5,    25, 0)],
    'sniper':  [1.5, ((255, 102, 0),  (8, 20),  150,  20, 2)],
    'blaster': [0.5, ((255, 255, 102), (8, 10), 999,  20, 0)]
}

powerup_list = {
#            [(R, G, B), time, modifier, var]
    'speed': ((255, 0, 255), 3, 1.5, "speed")
}

spaceship_list = {
#             (img, health, speed, weapon_slot_max)
    'player': (pg.image.load(os.path.join(dir_asset, 'pixel_ship_yellow.png')), 50000, 5, 4),
    'red':    (pg.image.load(os.path.join(dir_asset, 'pixel_ship_red_small.png')), 200, 1, 2),
    'green':  (pg.image.load(os.path.join(dir_asset, 'pixel_ship_green_small.png')), 150, 2, 2),
    'blue':   (pg.image.load(os.path.join(dir_asset, 'pixel_ship_blue_small.png')), 50, 4, 1)
}