import pygame as pg
import os

dir_asset = os.path.join(os.path.dirname(__file__), 'assets')

main_color = (255, 240, 200)
main_font = os.path.join(dir_asset, "fonts/MachineStd.otf")

background = os.path.join(dir_asset, 'background-black.png') 
empty_sprite = (os.path.join(dir_asset, 'empty.png'), 4)

sound_list = {
    'boss'  : os.path.join(dir_asset, "sound", "boss.wav"),
    'end'   : os.path.join(dir_asset, "sound", "end.wav"),
    'intro' : os.path.join(dir_asset, "sound", "intro.wav")
}

parallaxe_list = {
#              (img, nbframe, speed)  
    'planet1': (os.path.join(dir_asset, 'planet1.png'), 1, 0.5),
    'planet2': (os.path.join(dir_asset, 'planet2.png'), 1, 0.5),
    'planet3': (os.path.join(dir_asset, 'planet3.png'), 1, 0.5),
    'sun':     (os.path.join(dir_asset, 'sun.png'),     4, 0.5),
    'earth':   (os.path.join(dir_asset, 'earth.png'),   4, 0.5)
}

weapon_list = {
#              (cooldown, ((R, G, B), (size_x, size_y), damage, speed, penetration, dispertion), nBullet, (img, nbframe), price)
    'BFG':     (10,   ((179, 27, 7),  (20, 40), 500, 2,  -1, 0),    1,  (os.path.join(dir_asset, 'bfg.png'),     4), 50000),
    'laser':   (0,    ((0,204,255),   (5, 50),  5,   50, 0,  0),    1,  (os.path.join(dir_asset, 'laser.png'),   4), 7500), 
    'sniper':  (1.5,  ((255,20,147),  (8, 20),  150, 15, 2,  0),    1,  (os.path.join(dir_asset, 'sniper.png'),  8), 4000),
    'shotgun': (1.5,  ((255,255,255), (2, 3),   25,  15, 0,  0.33), 20, (os.path.join(dir_asset, 'shotgun.png'), 4), 2000), 
    'gatling': (0.15, ((255,255,102), (5, 10),  75,  10, 0,  0.1),  1,  (os.path.join(dir_asset, 'gatling.png'), 4), 500), 
    'missile': (2,    ((205,133,63) , (5, 5),   250, 25, 0,  1),    10, (os.path.join(dir_asset, 'missile.png'), 4), 10000)
}

bonus_list = ['speed', 'damage', 'heal', 'size', 'cooldown', 'money']
item_list = ['slow', 'weak', 'bigboi', 'firerate']
powerup_list = {
#               (img, nbframe, time, modifier)
    'speed':    ((os.path.join(dir_asset, 'speed.png'),    4), 10, 1.25, 0),
    'damage':   ((os.path.join(dir_asset, 'damage.png'),   4), 10, 1.5 , 0),
    'money':   ((os.path.join(dir_asset, 'money.png'),     4), 10, 1.5 , 0),
    'heal':     ((os.path.join(dir_asset, 'heal.png'),     4), 10, 0   , 0),
    'size':     ((os.path.join(dir_asset, 'size.png'),     4), 10, 0.5 , 0),
    'cooldown': ((os.path.join(dir_asset, 'cooldown.png'), 4), 10, 0.5 , 0),
    'slow':     ((os.path.join(dir_asset, 'slow.png'),     4), 10, 0.5 , 100),
    'weak':     ((os.path.join(dir_asset, 'weak.png'),     4), 10, 0.5 , 500),
    'bigboi':   ((os.path.join(dir_asset, 'bigboi.png'),   4), 10, 1.25, 200),
    'firerate': ((os.path.join(dir_asset, 'firerate.png'), 4), 10, 2   , 500)
}


enemy_list = ['red', 'blue', 'green', 'round', 'sneaky']
boss_list = ['boss_1', 'boss_2']
spaceship_list = {
#             ((img, nbframe), (health, explosionsize, speed), (weapons1_pos, ....), price)
    'player': ((os.path.join(dir_asset, 'ship_yellow.png'), 4), (500,  70,  7.5), [(0, 0), (-17, 10), (17, 10)],                          1200),
    'red':    ((os.path.join(dir_asset, 'ship_red.png'),    4), (200,  70,  1),   [(0, 0)],                                               1200),
    'green':  ((os.path.join(dir_asset, 'ship_green.png'),  4), (150,  70,  2),   [(0, 0)],                                               1200),
    'blue':   ((os.path.join(dir_asset, 'ship_blue.png'),   4), (50,   70,  2),   [(0, 0)],                                               1200),
    'round':  ((os.path.join(dir_asset, 'ship_round.png'),  4), (100,  70,  2),   [(0, 0)],                                               2400),
    'sneaky': ((os.path.join(dir_asset, 'ship_sneaky.png'), 4), (100,  70,  2),   [(0, 0)],                                               4000),
    'boss_1': ((os.path.join(dir_asset, 'ship_boss1.png'),  4), (50000, 125, 5),   [(-135, -100), (-55, 0), (0, 0), (55, 0), (135, -100)], 22000),
    'boss_2': ((os.path.join(dir_asset, 'ship_boss2.png'),  4), (25000, 125, 3),   [(-100, -150), (100, -150)],                            22000),
}
