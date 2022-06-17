import pygame as pg

from tile import Tile
from setup import * 
from player import Player


class Level:

    def __init__(self,level_data, screen):
        self.level_data = level_data
        self.screen = screen
        self.setup(self.level_data)

        self.world_speed = 8

    def setup(self, layout):
        self.tile = pg.sprite.Group()
        self.player = pg.sprite.GroupSingle()

        for i in range(0, len(layout)):
            for j in range(0, len(layout[i])):
                if layout[i][j] == 'X':
                    self.tile.add(Tile((j*tile_size, i*tile_size), tile_size))
                elif layout[i][j] == 'P':
                    self.player.add(Player((j, i)))
    def horizontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for tile in self.tile.sprites():
            if tile.rect.colliderect(player):
                if player.direction.x > 0:
                    player.rect.right = tile.rect.left
                elif player.direction.x < 0:
                    player.rect.left = tile.rect.right

    def vertical_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()

        for tile in self.tile.sprites():
            if tile.rect.colliderect(player):
                if player.direction.y > 0:
                    player.rect.bottom = tile.rect.top
                    player.direction.y = 0
                elif player.direction.y < 0:
                    player.rect.top = tile.rect.bottom
                    player.direction.y = 0

    def scroll_x(self):

        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < screen_width/4 and direction_x < 0:
            self.world_speed = 8
            player.speed = 0

        elif player_x > (screen_width - screen_width/4) and direction_x > 0:
            self.world_speed = -8
            player.speed = 0

        else:
            self.world_speed = 0
            player.speed = 8
        
        self.tile.update(self.world_speed) 

    def run(self):
        self.player.draw(self.screen)
        self.player.sprite.update()
        self.tile.draw(self.screen)
        self.scroll_x()
        self.horizontal_movement_collision()
        self.vertical_movement_collision()

