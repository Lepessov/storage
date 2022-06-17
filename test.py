import pygame as pg
from sys import exit

level_map = [
'                                       ',
'                                       ',
'                                       ',
' XX P    XXX                   XX      ',
' XXXX              XX              XX  ',
' XXXX            XX                    ',
'  XX       X   XXXX       XX   XX      ',
'                                       ',
'          X   XXXX       XX   XXX      ',
'      XXXX    XXXXXXX    XX   XXXX     ',
' XXXXXXXXX     XXXXXX    XX  XXXX      ',
]

tile_size = 64
screen_width = 1200
screen_height = len(level_map) * tile_size

class Tile(pg.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pg.Surface((size, size))
        self.image.fill('grey')
        self.rect = self.image.get_rect(topleft = pos)

    def update(self, x_shift):
        self.rect.x += x_shift

class Player(pg.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pg.image.load('graphics/Player/player_stand.png')
        self.rect = self.image.get_rect(midbottom = pos)
        self.direction = pg.math.Vector2(0,0)
        self.speed = 8
        self.gravity = 0.8
        self.jump_speed = -16

    def get_input(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_RIGHT]:
            self.direction.x = 1
        elif keys[pg.K_LEFT]:
            self.direction.x = -1
        elif keys[pg.K_UP]:
            self.gravity = -20
        else:
            self.direction.x = 0

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def update(self):
        self.get_input()
        self.rect.x += self.direction.x * self.speed
        # self.apply_gravity()
        

class Level:
    def __init__(self, level_data, surface):
        self.setup_level(level_data)
        self.display_surface = surface

        self.world_shift = 0

    def setup_level(self, layout):
        self.tiles = pg.sprite.Group()
        self.player = pg.sprite.GroupSingle()
        for i in range(0, len(layout)):
            for j in range(0, len(layout[i])):
                if layout[i][j] == 'X':
                    self.tiles.add(Tile((j*64, i*64), 64))
                elif layout[i][j] == 'P':
                    self.player.add(Player((i*64, j*64)))

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < screen_width/4 and player.direction.x < 0:
            self.world_shift = 8
            player.speed = 0

        elif player_x > screen_width - screen_width/4 and player.direction.x > 0:
            self.world_shift = -8
            player.speed = 0

        else:
            self.world_shift = 0
            player.speed = 8

    def run(self):
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.player.draw(self.display_surface)
        self.player.update()
        self.scroll_x()

# Init
pg.init()
screen = pg.display.set_mode((screen_width, screen_height))
clock = pg.time.Clock()

level = Level(level_map, screen)
while True:
    for event in pg.event.get():

        if event.type == pg.QUIT:
            pg.quit()
            exit()

    screen.fill('black')
    level.run()

    pg.display.update()
    clock.tick(60)


