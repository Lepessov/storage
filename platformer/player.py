import pygame as pg

walk_surf_1 = pg.image.load('graphics/Player/player_walk_1.png')
walk_surf_2 = pg.image.load('graphics/Player/player_walk_2.png')


class Player(pg.sprite.Sprite):

    def __init__(self, pos):
        super().__init__()
        self.walk_list = [walk_surf_1, walk_surf_2]
        self.index = 0

        self.image = pg.image.load('graphics/Player/player_stand.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.direction = pg.math.Vector2(0, 0)
        self.speed = 8
        self.jump_speed = -16
        self.gravity = 0.8

    def get_input(self):

        keys = pg.key.get_pressed()

        if keys[pg.K_RIGHT]:
            self.direction.x = 1

            if self.index >= len(self.walk_list):
                self.index = 0

        elif keys[pg.K_LEFT]:
            self.direction.x = -1

            if self.index >= len(self.walk_list):
                self.index = 0

        else:
            self.direction.x = 0

        if keys[pg.K_SPACE]:
            self.jump()
            self.image = pg.image.load('graphics/Player/jump.png')

    def animation(self):
        if self.index >= len(self.walk_list):
            self.index = 0
        self.image = self.walk_list[int(self.index)]


    def jump(self):
        self.direction.y = self.jump_speed

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def update(self):
        self.get_input()
        self.animation()
