import pygame as pg
import random

pg.init()
pg.font.init()
random.seed()

pg.mixer.init(frequency=44100, size=-16, channels=2, buffer=512, devicename="mixer", allowedchanges=0)
pg.mixer.music.set_volume(0.5)


screen = pg.display.set_mode((650, 1000))
title = 'Space Shooter'
clock = pg.time.Clock()
screen_shake = 0
gif_speed = 5
fps = 60

