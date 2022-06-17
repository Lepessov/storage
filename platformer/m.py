import pygame as pg

from sys import exit

from setup import *
from tile import Tile 
from level import Level 
from player import Player 

# Initializing
pg.init()
screen = pg.display.set_mode((screen_width, screen_height))
clock = pg.time.Clock()

# Level setup
level = Level(level_map, screen)

while True:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit

    screen.fill('black')
    level.run()
    pg.display.update()
    clock.tick(60)


