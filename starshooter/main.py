#
import pygame as pg
import os
import time
import random


from ressources.ressources import *
from ressources.settings import *
from ressources.functions import *

from ressources.classes.player import Player
from ressources.classes.enemy import Enemy
from ressources.classes.boss import Boss
from ressources.classes.weapon import Weapon
from ressources.classes.powerup import PowerUp
from ressources.classes.star import Star
from ressources.classes.label import Label

def main():
    screen
    run = True

    player = Player(0, screen.get_height()-screen.get_height()/4)
    player.weapons[0].change_weapon('BFG')
    player.weapons[1].change_weapon('laser')
    player.weapons[2].change_weapon('blaster')

    enemies = []
    powerups = []

    wave_length = 0
    level = 4
    lost = False
    lost_count = 0

    def redraw_window():
        screen.blit(BG, (0, 0))
        
        Label(screen.get_width()*0.85, 30, 'Level: {}'.format(level), (255, 240, 200), 30).draw(screen)
        Label(screen.get_width()*0.2, 30, 'Enemies remain : {}'.format(len(enemies)), (255, 240, 200), 30).draw(screen)

        for enemy in enemies:
            enemy.draw(screen)

        player.draw(screen)

        for powerup in powerups:
            powerup.draw(screen)

        if lost:
            pass
            Label(screen.get_width()/2, screen.get_height()/2, 'YOU DIED', (255, 240, 200), 100).draw(screen)

        pg.display.update()

    while run:
        pg.display.set_caption(title + str(" / FPS: {}".format(int(clock.get_fps()))))
        clock.tick(fps)
        redraw_window()

        if not(len(enemies)):
            level += 1
            wave_length += 1

            for _ in range(wave_length):
                enemy = Enemy(random.randrange(50, screen.get_width()-100), random.randrange(-500*level, -100), random.choice(['red', 'blue', 'green']))
                enemy.weapons[0].change_weapon('blaster')
                enemies.append(enemy)
            if not(level%5):
                for _ in range(int(level/5)):
                    boss = Boss(0, -1000, 'boss_1')
                    boss.weapons[0].change_weapon('blaster')
                    boss.weapons[1].change_weapon('blaster')
                    enemies.append(boss)

            for _ in range(level):
                powerups.append(PowerUp(random.randrange(50, screen.get_width()-100), random.randrange(-1500, -100), random.choice(['size', 'speed', 'damage', 'heal', 'cooldown'])))

        #update Player
        lost = player.update(enemies)
        if lost:
            lost_count += 1
            if lost_count > fps * 3:
                run = False
            else:
                continue
        
        #update Enemy 
        for enemy in enemies[:]:
            enemy_temp = enemy.update([player]) 
            if enemy_temp:
                enemies.remove(enemy_temp)
        
        #update Power-Up
        for powerup in powerups[:]:
            powerup_temp = powerup.update(player)
            if powerup_temp:
                powerups.remove(powerup_temp)
                

        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit()
            try :
                player.weapon_switch(event.dict['key']-49)
            except KeyError:
                pass
            
def menu():
    label_active = 0
    run = True
    previousKey = None
    labels = []
    labels.append(Label(screen.get_width()/2, 200, "New game", (255, 240, 200), 50))
    labels.append(Label(screen.get_width()/2, 400, "Load game", (255, 240, 200), 50))
    labels.append(Label(screen.get_width()/2, 600, "Settings", (255, 240, 200), 50))
    labels.append(Label(screen.get_width()/2, 800, "Exit", (255, 240, 200), 50))
        
    Label(180, 495, "S", (255, 240, 200), 200).draw(screen)
    Label(300, 445, "TAR", (255, 240, 200), 100).draw(screen)
    Label(380, 520, "H.Otter", (255, 240, 200), 100).draw(screen)
    pg.display.update()

    stars = []
    for n in range(1000):
        stars.append(Star((screen.get_width()/2, screen.get_height()/2), random.randint(0, 100)))
        for _ in range(500):
            stars[n].move()

    pg.time.delay(2500)
    while run:
        for e in pg.event.get():
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
                            main(screen)
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
            if star.draw(screen):
                stars.remove(star)
                stars.append(Star((screen.get_width()/2, screen.get_height()/2), star.width, 1))

        for n in range(len(labels)):
            if n == label_active:
                labels[n].draw(screen, 1)
            else:
                labels[n].draw(screen)
            
        pg.display.update()
        clock.tick(60)
        pg.display.set_caption("FPS: {}".format(int(clock.get_fps())))
        pg.draw.rect(screen, (0,0,0), ((0,0), screen.get_size()))
    pg.quit()

# menu()
main()
