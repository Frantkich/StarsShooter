import pygame, math, sys, os

keydict = {"space": pygame.K_SPACE, "esc": pygame.K_ESCAPE, "up": pygame.K_UP, "down": pygame.K_DOWN,
           "left": pygame.K_LEFT, "right": pygame.K_RIGHT, "return": pygame.K_RETURN,
           "a": pygame.K_a,
           "b": pygame.K_b,
           "c": pygame.K_c,
           "d": pygame.K_d,
           "e": pygame.K_e,
           "f": pygame.K_f,
           "g": pygame.K_g,
           "h": pygame.K_h,
           "i": pygame.K_i,
           "j": pygame.K_j,
           "k": pygame.K_k,
           "l": pygame.K_l,
           "m": pygame.K_m,
           "n": pygame.K_n,
           "o": pygame.K_o,
           "p": pygame.K_p,
           "q": pygame.K_q,
           "r": pygame.K_r,
           "s": pygame.K_s,
           "t": pygame.K_t,
           "u": pygame.K_u,
           "v": pygame.K_v,
           "w": pygame.K_w,
           "x": pygame.K_x,
           "y": pygame.K_y,
           "z": pygame.K_z,
           "1": pygame.K_1,
           "2": pygame.K_2,
           "3": pygame.K_3,
           "4": pygame.K_4,
           "5": pygame.K_5,
           "6": pygame.K_6,
           "7": pygame.K_7,
           "8": pygame.K_8,
           "9": pygame.K_9,
           "0": pygame.K_0}

def spritesheet(image, frames=1):
    images = []
    originalWidth = image.get_width() // frames
    originalHeight = image.get_height()
    frameSurf = pygame.Surface((originalWidth, originalHeight), pygame.SRCALPHA, 32)
    x = 0
    for _ in range(frames):
        frameSurf = pygame.Surface((originalWidth, originalHeight), pygame.SRCALPHA, 32)
        frameSurf.blit(image, (x, 0))
        images.append(frameSurf.copy())
        x -= originalWidth
    return images

def keyPressed(keyCheck=""):
    global keydict
    keys = pygame.key.get_pressed()
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
    # if pygame.mixer.music.get_busy():
    #     pygame.mixer.music.fadeout(1000)      #bug / freeze
        
    pygame.mixer.music.load(os.path.join(os.path.dirname(__file__), 'assets') + "/music/" + music_name)
    pygame.mixer.music.play(-1, 0, 5000)

def save(player):
    with open('save', 'w') as file_write:
        file_write.write(player.name + '\n' + str(player.money) + '\n'+ str(player.max_score) + '\n')
        for weapon in player.weapons:
            if weapon.weapon:
                file_write.write(weapon.weapon + '\n')
            else:
                file_write.write('None\n')


def load(player):
    with open('save', 'r') as file_read:
        lines = file_read.readlines()
        player.name = lines[0][:-1]
        player.money = int(lines[1])
        player.max_score = int(lines[2])
        n = 0
        for weapon in lines[3:]:
            if not(weapon[:-1] == "None"):
                player.weapons[n].change_weapon(weapon[:-1])
            n += 1
    return player
