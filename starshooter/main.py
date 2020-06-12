#
import pygame as pg
import os
import time
import random

pg.font.init()
random.seed()

from ressources import ressources
from ressources.settings import *

from ressources.classes.player import Player
from ressources.classes.enemy import Enemy
from ressources.classes.weapon import Weapon
from ressources.classes.powerup import PowerUp

def main(window):
    screen
    run = True

    player = Player(0, window.get_height()-window.get_height()/4)
    player.x = window.get_width()/2 - player.get_width()/2
    player.new_weapon(0, 0, 0, 'blaster')
    player.new_weapon(0, 0, 1, 'sniper')
    # player.new_weapon(0, 0, 2, 'laser')
    # player.new_weapon(0, 0, 3, 'BFG')

    enemies = []
    powerups = []

    wave_length = 0
    level = 0
    lost = False
    lost_count = 0

    def redraw_window():
        window.blit(ressources.BG, (0, 0))
        
        level_label = main_font.render(f'Level: {level}', 1, (255, 255, 255))
        window.blit(level_label, (window.get_width() - level_label.get_width() - 10, 10))

        for enemy in enemies:
            enemy.draw(window)

        player.draw(window)

        for powerup in powerups:
            powerup.draw(window)

        if lost:
            lost_label = lost_font.render('You Lost!!', 1, (255, 255, 255))
            window.blit(lost_label, (window.get_width()/2 - lost_label.get_width()/2, 350))

        pg.display.update()

    while run:
        pg.display.set_caption(title + str(" / FPS: {}".format(int(clock.get_fps()))))
        clock.tick(fps)
        redraw_window()

        if not(len(enemies)):
            level += 1
            wave_length += 5
            for _ in range(wave_length):
                enemy = Enemy(random.randrange(50, window.get_width()-100), random.randrange(-1500, -100), random.choice(['red', 'blue', 'green']))
                enemy.new_weapon(0, enemy.get_height(), 0, "blaster")
                enemies.append(enemy)

            for _ in range(level):
                powerups.append(PowerUp(random.randrange(50, window.get_width()-100), random.randrange(-1500, -100), random.choice(['size', 'speed', 'damage', 'heal', 'cooldown'])))
                
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
            try:
                player.weapon_switch(event.dict['key']-49)
            except:
                pass

def main_menu(window):
    pg.display.set_caption(title)
    run = True
    while run:
        window.blit(ressources.BG, (0, 0))
        title_label = title_font.render('START', 1, (255, 255, 255))
        window.blit(title_label, (window.get_width()/2 - title_label.get_width()/2, 350))
        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.KEYDOWN:
                main(window)
    pg.quit()

main_menu(screen)
