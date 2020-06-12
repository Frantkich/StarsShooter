import random, math, pygame, sys, os
from pygame.locals import *

random.seed()
WINSIZE = (600, 1000)
WINCENTER = (WINSIZE[0]/2, WINSIZE[1]/2)
SCREEN = pygame.display.set_mode(WINSIZE)


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


def keyPressed(keyCheck=""):
    global keydict
    keys = pygame.key.get_pressed()
    if sum(keys) > 0:
        if keyCheck == "" or keys[keydict[keyCheck.lower()]]:
            return True
    return False


class Star:
    def __init__(self, pos, width, heritage=None):
        self.x, self.y = pos
        if heritage:
            self.width = width
        else:
            if 0 <= width < 80:
                self.width = 0
            if 80 <= width < 95:
                self.width = 1
            if 95 <= width <= 100:
                self.width = 2
        self.color = (255, 240, 200)
        self.vel = [random.uniform(-1, 1), random.uniform(-1, 1)]
        self.acc = (random.uniform(0.005, 0.05) * self.width) + 1
        if not(self.acc):
            self.acc = 1.005

    def move(self):
        self.vel[0] *= self.acc
        self.vel[1] *= self.acc
        
        self.x += self.vel[0]
        self.y += self.vel[1]
    
    def draw(self, surface):
        if 0 < self.x < surface.get_width() or 0 < self.y < surface.get_height():
            pygame.draw.line(surface, (255, 240, 200), (int(self.x - self.vel[0]), int(self.y - self.vel[1])), (int(self.x), int(self.y)), self.width)
            if self.width:
                pygame.draw.circle(surface, (255, 240, 200), (int(self.x), int(self.y)), self.width)
            else:
                surface.set_at((int(self.x), int(self.y)), self.color)
        else:
            return True
        
        
class Label():
    def __init__(self, x, y, text, color):
        self.x = x
        self.y = y
        self.text = text
        self.color = color
        self.font = pygame.font.Font(os.path.join("assets", "fonts", 'MachineStd.otf'), 70)

    def draw(self, window, is_active = 0):
        if is_active:
            label = self.font.render("> " + self.text + " <", False, self.color)
        else:
            label = self.font.render(self.text, False, self.color)
        window.blit(label, (self.x - label.get_width()/2, self.y - label.get_height()/2))


def menu(window,clock):
    label_active = 0
    run = True
    labels = []
    labels.append(Label(window.get_width()/2, 200, "New game", (255, 240, 200)))
    labels.append(Label(window.get_width()/2, 400, "Load game", (255, 240, 200)))
    labels.append(Label(window.get_width()/2, 600, "Settings", (255, 240, 200)))
    labels.append(Label(window.get_width()/2, 800, "Exit", (255, 240, 200)))
        
    Label(window.get_width()/2, window.get_height()/2, "StarSShooterS", (255, 240, 200)).draw(window)
    pygame.display.update()

    stars = []
    for n in range(1000):
        stars.append(Star(WINCENTER, random.randint(0, 100)))
        for _ in range(500):
            stars[n].move()

    pygame.time.delay(1000)
    
    previousKey = None
    print(len(stars))
    while run:
        for e in pygame.event.get():
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
                            pass
                            #Start the game
                            print("start")
                        elif label_active == 1:
                            pass
                            # Récuperation de sauvegarde
                            print("sauvegarde")
                        elif label_active == 2:
                            #Settings
                            print("settings")
                        else:
                            #quit
                            print("quit")
                            run = False
                            break
            except KeyError:
                pass

        for star in stars:
            star.move()
            if star.draw(window):
                stars.remove(star)
                stars.append(Star(WINCENTER, star.width, 1))

        for n in range(len(labels)):
            if n == label_active:
                labels[n].draw(window, 1)
            else:
                labels[n].draw(window)
            
        pygame.display.update()
        clock.tick(60)
        pygame.display.set_caption("FPS: {}".format(int(clock.get_fps())))
        pygame.draw.rect(window, (0,0,0), ((0,0), WINSIZE))

def main(window):
    clock = pygame.time.Clock()
    pygame.init()
    menu(window, clock)

if __name__ == '__main__':
    main(SCREEN)