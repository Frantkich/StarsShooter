
import pygame as pg
import os
import random

from ressources.ressources import *
from ressources.settings import *
from ressources.functions import *

from ressources.classes.enemy import Enemy
from ressources.classes.boss import Boss
from ressources.classes.weapon import Weapon
from ressources.classes.powerup import PowerUp
from ressources.classes.explosion import Explosion
from ressources.classes.parallaxe import Parallaxe
from ressources.classes.label import Label

def game(player):
    run = True
    enemies = []
    powerups = []

    explosions = []
    parallaxes = []

    wave_length = 0
    level = 0
    lost = False
    lost_count = 0
    background_offset = (0, 0)
    pg.mixer.Sound(sound_list['intro']).play()
    change_music("level.mp3")

    DEBUG = True

    def redraw_window():
        screen.blit(pg.transform.scale(pg.image.load(background), screen.get_size()), background_offset)

        for parallaxe in parallaxes:
            parallaxe.draw()

        for enemy in enemies:
            enemy.draw()

        for powerup in powerups:
            powerup.draw()

        for explosion in explosions:
            explosion.draw()

        player.draw()

        if lost:
            pass
            Label(screen.get_width()/2, screen.get_height()/2, 'YOU DIED', (255, 240, 200), 100).draw()
        
        Label(screen.get_width()*0.85, 30, 'Level: {}'.format(level), (255, 240, 200), 30).draw()
        Label(screen.get_width()*0.2, 30, 'Enemies remain : {}'.format(len(enemies)), (255, 240, 200), 30).draw()
        pg.display.update()

    while run:  
        pg.display.set_caption(title + str(" / FPS: {}".format(int(clock.get_fps()))))
        clock.tick(fps)
        redraw_window()

        if not(len(enemies)) and not(DEBUG):
            level += 1
            wave_length += 5

            if not(level%5):
                pg.mixer.Sound(sound_list['boss']).play()
                change_music("boss.mp3")

            if level%5 == 1 and level != 1:
                change_music("level.mp3")

            if not(level%10):
                boss = Boss(0, -500, 'boss_1')
                boss.weapons[0].change_weapon('blaster')
                boss.weapons[1].change_weapon('blaster')
                boss.weapons[2].change_weapon('BFG')
                boss.weapons[3].change_weapon('blaster')
                boss.weapons[4].change_weapon('blaster')
                enemies.append(boss)

            elif not(level%5):
                boss = Boss(0, -500, 'boss_2')
                boss.weapons[0].change_weapon('sniper')
                boss.weapons[1].change_weapon('sniper')
                enemies.append(boss)

            else:
                for _ in range(wave_length):
                    enemy = Enemy(random.randrange(50, screen.get_width()-100), random.randrange(-500*level, -100), random.choice(list(enemy_list)))
                    enemy.weapons[0].change_weapon('blaster')
                    enemies.append(enemy)

            for _ in range(random.randint(0, int(level/2))):
                powerups.append(PowerUp(random.randrange(50, screen.get_width()-100), random.randrange(-1500, -100), random.choice(list(powerup_list))))
        
        if not(random.randint(0, fps*40)):
            parallaxes.append(Parallaxe(random.choice(list(parallaxe_list))))

        for parallaxe in parallaxes:
            parallaxe.update()

        #update Player
        lost = player.update(enemies)
        if lost:
            lost_count += 1
            if lost_count > fps * 3:
                save(player)
                run = False
            else:
                continue
        
        #update Enemy 
        for enemy in enemies[:]:
            enemy_temp = enemy.update([player]) 
            if enemy_temp:
                explosions.append(Explosion((int(enemy.x + enemy.get_width()/2), int(enemy.y + enemy.get_height()/2)), enemy.boom ))
                enemies.remove(enemy_temp)
        
        #update Power-Up
        for powerup in powerups[:]:
            powerup_temp = powerup.update(player)
            if powerup_temp:
                powerups.remove(powerup_temp)
                
        if player.screen_shake:
            player.screen_shake -= 1
            intensity = 10
            background_offset = (random.randint(-intensity, intensity), random.randint(-intensity, intensity))
        else:
            background_offset = (0, 0)
        

        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit()
            try :
                player.weapon_switch(event.dict['key']-49)
            except KeyError:
                pass
            if event.type == pygame.MOUSEBUTTONUP:
                x, y = pygame.mouse.get_pos()
                powerups.append(PowerUp(x, y, 'cooldown'))
                # enemy = Enemy(x, y, random.choice(list(enemy_list)))
                # enemy.weapons[0].change_weapon('blaster')
                # enemies.append(enemy)

                # parallaxes.append(Parallaxe(random.choice(list(parallaxe_list))))
                
                # for enemy in enemies:
                #     enemy.health = 0

                # load(player)

                # player.health = 0
                
  