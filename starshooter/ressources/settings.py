import pygame as pg

title = 'Space Shooter'
screen = pg.display.set_mode((650, 1000))
gameClock = pg.time.Clock()
fps = 60

main_font = pg.font.SysFont('comicsans', 50)
lost_font = pg.font.SysFont('comicsans', 60)
title_font = pg.font.SysFont('comicsans', 70)