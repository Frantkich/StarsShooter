import pygame as pg
import os, math

from app.settings import *

def spritesheet(image, frames=1):
    sprites = []
    originalWidth = image.get_width() // frames
    originalHeight = image.get_height()
    frameSurf = pg.Surface((originalWidth, originalHeight), pg.SRCALPHA, 32)
    cut = 0
    for _ in range(frames):
        frameSurf = pg.Surface((originalWidth, originalHeight), pg.SRCALPHA, 32)
        frameSurf.blit(image, (cut, 0))
        sprites.append(frameSurf.copy())
        cut -= originalWidth
    return sprites

def keyPressed(keyCheck=""):
    keys = pg.key.get_pressed()
    if sum(keys) > 0:
        if keyCheck == "" or keys[keydict[keyCheck.lower()]]:
            return True

def collide(obj1, obj2):
    offset_x = int(obj2.x - obj1.x)
    offset_y = int(obj2.y - obj1.y)
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None

def homingHead(shipX, shipY, targets):
    closestTarget = [1080, targets[0]]
    for target in targets:
        dx = target.x + target.get_width()/2 - shipX
        dy = target.y + target.get_height()/2 - shipY
        if math.hypot(dx, dy) < closestTarget[0]:
            closestTarget = (math.hypot(dx, dy), target)
    return closestTarget[1]

def change_music(music_name):        
    pg.mixer.music.load(os.path.join(os.path.dirname(__file__), 'assets/music/{}.mp3'.format(music_name)))
    pg.mixer.music.play(-1, 0, 5000)

def save(player):
    with open('save', 'w') as file_write:
        file_write.write('{}\n{}\n{}\n'.format(player.name, str(player.money), str(player.max_score))) 
        print(player.inventory, file=file_write)
        for weapon in player.weapons:
            if weapon.weapon:
                file_write.write('{}\n'.format(weapon.weapon))
            else:
                file_write.write('None\n')
            
def load(player):
    with open('save', 'r') as file_read:
        lines = file_read.readlines()
        player.init_ship(lines[0][:-1])
        player.money = int(lines[1])
        player.max_score = int(lines[2])
        exec('player.inventory = {}'.format(lines[3]))
        n = 0
        for weapon in lines[4:]:
            if not(weapon[:-1] == "None"):
                player.weapons[n].change_weapon(weapon[:-1])
            n += 1
    return player

def end():
    pg.display.update()
    clock.tick(fps)
    pg.display.set_caption("FPS: {}".format(int(clock.get_fps())))

keydict = {"esc": pg.K_ESCAPE, 
           "return": pg.K_RETURN,
           "space": pg.K_SPACE, 
           "up": pg.K_UP, 
           "down": pg.K_DOWN,
           "left": pg.K_LEFT, 
           "right": pg.K_RIGHT, 
           "a": pg.K_a,
           "b": pg.K_b,
           "c": pg.K_c,
           "d": pg.K_d,
           "e": pg.K_e,
           "f": pg.K_f,
           "g": pg.K_g,
           "h": pg.K_h,
           "i": pg.K_i,
           "j": pg.K_j,
           "k": pg.K_k,
           "l": pg.K_l,
           "m": pg.K_m,
           "n": pg.K_n,
           "o": pg.K_o,
           "p": pg.K_p,
           "q": pg.K_q,
           "r": pg.K_r,
           "s": pg.K_s,
           "t": pg.K_t,
           "u": pg.K_u,
           "v": pg.K_v,
           "w": pg.K_w,
           "x": pg.K_x,
           "y": pg.K_y,
           "z": pg.K_z,
           "1": pg.K_1,
           "2": pg.K_2,
           "3": pg.K_3,
           "4": pg.K_4,
           "5": pg.K_5,
           "6": pg.K_6,
           "7": pg.K_7,
           "8": pg.K_8,
           "9": pg.K_9,
           "0": pg.K_0
}
