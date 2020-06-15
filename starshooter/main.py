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
from ressources.classes.explosion import Explosion
from ressources.classes.soundbarre import Soundbarre
from ressources.classes.shop_section import Shop_section
from ressources.classes.shop_item import Shop_item
from ressources.classes.parallaxe import Parallaxe

def main():
    screen
    run = True

    player = Player(0, screen.get_height()-screen.get_height()/4)
    player.weapons[0].change_weapon('missile')
    # player.weapons[1].change_weapon('sniper')
    player.weapons[1].change_weapon('blaster')

    enemies = []
    powerups = []

    explosions = []
    parallaxes = []

    wave_length = 0
    level = 0
    lost = False
    lost_count = 0
    background_offset = (0, 0)

    DEBUG = True

    def redraw_window():
        screen.blit(pg.transform.scale(pg.image.load(background), screen.get_size()), background_offset)

        for parallaxe in parallaxes:
            parallaxe.draw()

        for enemy in enemies:
            enemy.draw(screen)

        for powerup in powerups:
            powerup.draw(screen)

        for explosion in explosions:
            explosion.draw()

        player.draw(screen)

        if lost:
            pass
            Label(screen.get_width()/2, screen.get_height()/2, 'YOU DIED', (255, 240, 200), 100).draw(screen)
        
        Label(screen.get_width()*0.85, 30, 'Level: {}'.format(level), (255, 240, 200), 30).draw(screen)
        Label(screen.get_width()*0.2, 30, 'Enemies remain : {}'.format(len(enemies)), (255, 240, 200), 30).draw(screen)
        pg.display.update()

    while run:
                
        pg.display.set_caption(title + str(" / FPS: {}".format(int(clock.get_fps()))))
        clock.tick(fps)
        redraw_window()

        if not(len(enemies)) and not(DEBUG):
            level += 1
            wave_length += 5

            for _ in range(wave_length):
                enemy = Enemy(random.randrange(50, screen.get_width()-100), random.randrange(-500*level, -100), random.choice(list(enemy_list)))
                enemy.weapons[0].change_weapon('blaster')
                enemies.append(enemy)

            if level == 5:
                boss = Boss(0, -500, 'boss_2')
                boss.weapons[0].change_weapon('sniper')
                boss.weapons[1].change_weapon('sniper')
                enemies.append(boss)

            if level == 10:
                boss = Boss(0, -500, 'boss_1')
                boss.weapons[0].change_weapon('blaster')
                boss.weapons[1].change_weapon('blaster')
                boss.weapons[2].change_weapon('BFG')
                boss.weapons[3].change_weapon('blaster')
                boss.weapons[4].change_weapon('blaster')
                enemies.append(boss)

            # for _ in range(level):
            #     powerups.append(PowerUp(random.randrange(50, screen.get_width()-100), random.randrange(-1500, -100), random.choice(['size', 'speed', 'damage', 'heal', 'cooldown'])))

        
        if not(random.randint(0, fps*40)):
            parallaxes.append(Parallaxe(random.choice(list(parallaxe_list))))

        for parallaxe in parallaxes:
            parallaxe.move()

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
                explosions.append(Explosion((int(enemy.x + enemy.get_width()/2), int(enemy.y + enemy.get_height()/2)), 70))
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
            if event.type == pygame.MOUSEBUTTONUP and DEBUG:
                x, y = pygame.mouse.get_pos()
                enemy = Enemy(x, y, random.choice(list(enemy_list)))
                enemy.weapons[0].change_weapon('blaster')
                enemies.append(enemy)
        
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

    soundbarre = Soundbarre(screen.get_width()/4, screen.get_height()* 3/10 , (4, 195, 225), screen)

    stars = []
    for n in range(1000):
        stars.append(Star((screen.get_width()/2, screen.get_height()/2), random.randint(0, 100)))
        for _ in range(500):
            stars[n].move()

    pg.time.delay(2500)
    change_music("Space_Invaders_3.mp3")
    
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
                            main()
                        elif label_active == 1:
                            pass
                            # Récuperation de sauvegarde
                            print("sauvegarde")
                        elif label_active == 2:
                            settings(soundbarre)
                        else:
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

def settings(soundbarre):
    run = True
    previousKey = None
    
    labels = []
    controls = []
    labels.append(Label(screen.get_width()/2, screen.get_height()* 1.5/10, "Sound", (255, 240, 200), 60)) #Sound Label
    labels.append(Label(screen.get_width()/2, screen.get_height()* 5/10 , "Controls", (255, 240, 200), 60))  #Controls
    controls.append(Label(screen.get_width()/2, screen.get_height()* 6/10 , "Z, Q, S, D : Movement", (255, 240, 200), 40))
    controls.append(Label(screen.get_width()/2, screen.get_height()* 7/10 , "1, 2, 3 ... : Switch weapons", (255, 240, 200), 40))
    controls.append(Label(screen.get_width()/2, screen.get_height()* 8/10 , "Space : shoot", (255, 240, 200), 40))
    labels.append(Label(screen.get_width()/2, screen.get_height()* 9/10, "Escape : Done", (255, 240, 200), 40))  #Esc 
    
    while run:
        for label in labels:
            label.draw(screen)

        for control in controls:
            control.draw(screen)

        soundbarre.draw(screen)
        for e in pg.event.get():
            try:
                if previousKey != e.dict['unicode']:
                    previousKey = e
                    if keyPressed("d") and soundbarre.volumeLevel < 10:
                        soundbarre.up_volumeLevel()
                        pg.mixer.music.set_volume(soundbarre.volumeLevel/10)
                    if keyPressed("q") and 0 < soundbarre.volumeLevel:
                        soundbarre.down_volumeLevel()
                        pg.mixer.music.set_volume(soundbarre.volumeLevel/10)
                    if keyPressed("f"):  #Test son
                        pg.mixer.Sound(sound_list['test1']).play()
                        change_music("Space_Invaders_1.mp3")
                    if keyPressed("g"): #test son
                        pg.mixer.Sound(sound_list['test2']).play()
                    if keyPressed('esc'):
                            run = False

            except KeyError:
                pass        

        pg.display.update()
        clock.tick(60)
        pg.display.set_caption("FPS: {}".format(int(clock.get_fps())))
        pg.draw.rect(screen, (0,0,0), ((0,0), (screen.get_width(), screen.get_height()) ))

def shop():
    
    label_active = 0
    run = True
    previousKey = None
    
    shop_section = []  #Shop_section(self, label_y, label_text, x, y, width, height)

    shop_section.append(Shop_section(screen.get_height()* 1/10, "Power-ups", screen.get_width()*1/3, screen.get_height()* 1.4/10))
    shop_section.append(Shop_section(screen.get_height()* 4/10 , "Weapons", screen.get_width()*1/3, screen.get_height()* 4.4/10))
    shop_section.append(Shop_section(screen.get_height()* 7/10 , "Ships", screen.get_width()*1/3, screen.get_height()* 7.4/10))

    shop_section[0].add_shop_item(Shop_item("item lo", "999", "ship_blue.png"))
    shop_section[0].add_shop_item(Shop_item("item lo", "999","ship_red.png"))
    shop_section[0].add_shop_item(Shop_item("item lo", "999","ship_green.png"))
    shop_section[1].add_shop_item(Shop_item("item2", "999","ship_blue.png"))
    shop_section[1].add_shop_item(Shop_item("item2", "999", "ship_red.png"))
    shop_section[1].add_shop_item(Shop_item("item2", "999","ship_green.png"))
    shop_section[2].add_shop_item(Shop_item("item2", "999","ship_blue.png"))
    shop_section[2].add_shop_item(Shop_item("item2", "999","ship_red.png"))
    shop_section[2].add_shop_item(Shop_item("item2", "999","ship_green.png"))

    while run:
        for n in range(len(shop_section)):
            if n == label_active:
                shop_section[n].label.draw(screen, 1)  #Display label
                shop_section[n].draw(screen, 1)
            else:
                shop_section[n].label.draw(screen, 0)
                shop_section[n].draw(screen, 0)

        for e in pg.event.get():
            try:
                if previousKey != e.dict['unicode']:
                    previousKey = e
                    if keyPressed("s"):
                        label_active += 1

                    if keyPressed("z"):
                        label_active -= 1

                    if label_active < 0:
                        label_active = len(shop_section)-1

                    elif len(shop_section)-1 < label_active:
                        label_active = 0

                    if keyPressed("d"):
                        shop_section[label_active].item_count += 1

                    if keyPressed("q"):
                        shop_section[label_active].item_count -= 1


            except KeyError:
                pass

        pg.display.update()
        clock.tick(60)
        pg.display.set_caption("FPS: {}".format(int(clock.get_fps())))
        pg.draw.rect(screen, (0,0,0), ((0,0), (screen.get_width(), screen.get_height()) ))


# menu()
main()
# settings(Soundbarre(screen.get_width()/4, screen.get_height()* 3/10 , (4, 195, 225), screen))
# shop()