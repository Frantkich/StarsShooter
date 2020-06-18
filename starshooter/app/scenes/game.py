from app.ressources import *

from app.classes.explosion import Explosion
from app.classes.parallaxe import Parallaxe
from app.classes.powerup import PowerUp
from app.classes.weapon import Weapon
from app.classes.label import Label
from app.classes.enemy import Enemy
from app.classes.boss import Boss


def game(player):
    run = True
    DEBUG = False
    previousKey = None
    
    pg.mixer.Sound(sound_list['intro']).play()

    player.health = player.health_max

    enemies = []
    powerups = []
    explosions = []
    parallaxes = []

    wave_length = 0
    level = 0
    lost = False
    lost_count = 0

    pause = False

    
    label_active = 0
    labels = []
    labels.append(Label(screen.get_width()/2, 200, "Continue", main_color, 50))
    labels.append(Label(screen.get_width()/2, 400, "Headquarter", main_color, 50))

    def redraw_window():
        if player.screen_shake:
            player.screen_shake -= 1
            intensity = 10
            screen.blit(pg.transform.scale(pg.image.load(background), screen.get_size()), (random.randint(-intensity, intensity), random.randint(-intensity, intensity)))
        else:
            screen.blit(pg.transform.scale(pg.image.load(background), screen.get_size()), (0, 0))        

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
            Label(screen.get_width()/2, screen.get_height()*0.25, 'YOU DIED', (255, 240, 200), 100).draw() ###############################
            Label(screen.get_width()/2, screen.get_height()*0.6, 'score : {}'.format(player.score), (255, 240, 200), 50).draw()
            Label(screen.get_width()/2, screen.get_height()*0.7, 'max score : {}'.format(player.max_score), (255, 240, 200), 50).draw()

        if pause:
            for n in range(len(labels)):
                if n == label_active:
                    labels[n].draw(1)
                else:
                    labels[n].draw()

        Label(screen.get_width()*0.85, 30, 'Level: {}'.format(level), (255, 240, 200), 30).draw() #########################""
        Label(screen.get_width()*0.2, 30, 'Enemies remain : {}'.format(len(enemies)), (255, 240, 200), 30).draw()

    def update():
        for parallaxe in parallaxes:
            parallaxe.update()

        for enemy in enemies[:]:
            enemy_temp = enemy.update([player]) 
            if enemy_temp:
                explosions.append(Explosion((int(enemy.x + enemy.get_width()/2), int(enemy.y + enemy.get_height()/2)), enemy.boom ))
                enemies.remove(enemy_temp)

        for powerup in powerups[:]:
            powerup_temp = powerup.update([player])
            if powerup_temp:
                powerups.remove(powerup_temp)

        if not(random.randint(0, fps*40)):
            parallaxes.append(Parallaxe(random.choice(list(parallaxe_list))))

    while run:
        end()

        if not(len(enemies)) and not(DEBUG):
            level += 1
            wave_length += 5

            if not(level%5):
                pg.mixer.Sound(sound_list['boss']).play()
                change_music("boss")

            if level%5 == 1:
                change_music("level")

            if level%5 == 4:
                change_music("pre_boss")

            if not(level%10):
                boss = Boss(0, -500, 'boss_1')
                boss.weapons[0].change_weapon('gatling')
                boss.weapons[1].change_weapon('gatling')
                boss.weapons[2].change_weapon('BFG')
                boss.weapons[3].change_weapon('gatling')
                boss.weapons[4].change_weapon('gatling')
                enemies.append(boss)

            elif not(level%5):
                boss = Boss(0, -500, 'boss_2')
                boss.weapons[0].change_weapon('sniper')
                boss.weapons[1].change_weapon('sniper')
                enemies.append(boss)

            else:
                for _ in range(wave_length):
                    enemy = Enemy(random.randrange(25, screen.get_width()-50), random.randrange(-500*level, -100), random.choice(list(enemy_list)))
                    enemy.weapons[0].change_weapon('gatling')
                    enemies.append(enemy)

            for _ in range(random.randint(0, int(level/2))):
                powerups.append(PowerUp(random.randrange(25, screen.get_width()-50), random.randrange(-1000*level, -100), random.choice(bonus_list)))

        redraw_window()

        if not(pause):
            lost = player.update(enemies)
            if lost:
                if not(lost_count):
                    pg.mixer.Sound(sound_list['end']).play()
                lost_count += 1
                if lost_count > fps * 3:
                    save(player)
                    run = False
                else:
                    continue
            
            update()


        for e in pg.event.get():
            if e.type == pg.QUIT:
                quit()
            if keyPressed("esc"):
                pause = True
            try :
                player.weapon_switch(e.dict['key']-49)
            except KeyError:
                pass
            
            if pause:
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
                                pause = False
                            if label_active == 1:
                                pause = False
                                player.health = 0
                                break
                except KeyError:
                    pass

            # if e.type == pg.MOUSEBUTTONUP:
                # pass
                # x, y = pg.mouse.get_pos()

                # boss = Boss(0, -500, 'boss_1')
                # boss.weapons[0].change_weapon('gatling')
                # boss.weapons[1].change_weapon('gatling')
                # boss.weapons[2].change_weapon('BFG')
                # boss.weapons[3].change_weapon('gatling')
                # boss.weapons[4].change_weapon('gatling')
                # enemies.append(boss)
                
                # powerups.append(PowerUp(x, y, random.choice(powerup_list)))
                
                # enemy = Enemy(x, y, random.choice(list(enemy_list)))
                # enemy.weapons[0].change_weapon('gatling')
                # enemies.append(enemy)

                # parallaxes.append(Parallaxe(random.choice(list(parallaxe_list))))
                
                # for enemy in enemies:
                #     enemy.health = 0

                # save(player)

                # player.health = 0
    change_music("transition")
                
  