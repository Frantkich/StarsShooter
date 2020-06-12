import pygame as pg

title = 'Space Shooter'
screen = pg.display.set_mode((650, 1000))
clock = pg.time.Clock()
fps = 60
gif_speed = 5

main_font = pg.font.SysFont('comicsans', 50)
lost_font = pg.font.SysFont('comicsans', 60)
title_font = pg.font.SysFont('comicsans', 70)