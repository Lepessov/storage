import pygame as pg 

from sys import exit
from random import *

class Player(pg.sprite.Sprite):

    def __init__(self):

        super().__init__()
        self.image = pg.image.load('graphics/Player/player_stand.png').convert_alpha()
        self.walk1 = pg.image.load('graphics/Player/player_walk_1.png').convert_alpha()
        self.walk2 = pg.image.load('graphics/Player/player_walk_2.png').convert_alpha()
        self.jump = pg.image.load('graphics/Player/jump.png').convert_alpha()
        self.index = 0
        self.walk_list = [self.walk1, self.walk2]

        self.surf = self.walk_list[self.index]
        self.gravity = 0
        self.rect = self.image.get_rect(midbottom = (100, 300))
        self.player_gravity = 0 
        self.jump_sound = pg.mixer.Sound('audio/jump.mp3')
        self.jump_sound.set_volume(0.5)

    def player_input(self):
        key = pg.key.get_pressed()
        if key[pg.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -20
            self.jump_sound.play()

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity 
        if self.rect.bottom >= 300:
            self.rect.bottom = 300
    
    def animation(self):

        if self.rect.bottom < 300:
            self.image = self.jump
        else:
            self.index += 0.1
            if self.index >= len(self.walk_list):
                self.index = 0
            self.image = self.walk_list[int(self.index)]

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation()


class Obstacles(pg.sprite.Sprite):

    def __init__(self,type):
        super().__init__()

        if type == 'snail':
            self.walk1 = pg.image.load('graphics/snail/snail1.png').convert_alpha()
            self.walk2 = pg.image.load('graphics/snail/snail2.png').convert_alpha()
            self.walk_list = [self.walk1, self.walk2]
            y_pos = 300 
        else:
            self.walk1 = pg.image.load('graphics/Fly/Fly1.png').convert_alpha()
            self.walk2 = pg.image.load('graphics/Fly/Fly2.png').convert_alpha()
            self.walk_list = [self.walk1, self.walk2]
            y_pos = randint(180, 210)
            

        self.index = 0
        self.image = self.walk_list[self.index]
        self.rect = self.image.get_rect(midbottom = (randint(900, 1100), y_pos))

    def animation(self):
        self.index += 0.1
        if self.index >= len(self.walk_list):
            self.index = 0
        self.image = self.walk_list[int(self.index)]

    def destroy(self):
        if self.rect.x < -100:
            self.kill()

    def update(self):
        self.animation()
        self.rect.x -= 6
        self.destroy()





def display_score():
    current_time = int(pg.time.get_ticks() / 1000 - start_time )
    score_surf = test_font.render(f'Score: {current_time}', False, (64, 64, 64))
    screen.blit(score_surf, score_rect)
    
    return current_time

def display(s):
    surf = test_font.render(f'Your score: {s}', False, (64, 64, 64,))
    rect = over_surf.get_rect(center=(500, 50))
    screen.blit(surf, rect)

# def obstacle_movement(obstacle_rect_list):
#     if obstacle_rect_list:
#         for obstacle_rect in obstacle_rect_list:
#             obstacle_rect.x -= 5

#             if obstacle_rect.bottom == 300:
#                 screen.blit(snail_surf, obstacle_rect)
#             else:
#                 screen.blit(fly_surf, obstacle_rect)

#         obstacle_rect_list = [obstacle for obstacle in obstacle_rect_list if obstacle.x > -100]

#         return obstacle_rect_list

#     else:

#         return []

def check_collisions(player, obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect):
                return False
    return True

def collision_sprite():

    if pg.sprite.spritecollide(player.sprite, obstacles, False):
        obstacles.empty()
        return False
    else:
        return True

# def player_animation():

#     global player_surf, player_index

#     if player_rect.bottom < 300:
#         player_surf = player_jump
#     else:
#         player_index += 0.1
#         if player_index >= len(player_walk_list):
#             player_index = 0
#         player_surf = player_walk_list[int(player_index)]

# Initializing 
pg.init()
screen = pg.display.set_mode((800, 400))
pg.display.set_caption('Runner')
clock = pg.time.Clock()
test_font = pg.font.Font(None, 50)
over_font = pg.font.Font(None, 100)
game_active = True
back_music = pg.mixer.Sound('audio/background_music.mp3')
back_music.set_volume(0.5)
back_music.play(loops = -1) 
start_time = 0
# obstacle_rect_list = []

over_surf = over_font.render('Game Over', False, (64, 64, 64,))
over_rect = over_surf.get_rect(center=(400, 190))

instructions_surf = test_font.render('Press "SPACE" to restart the game.', False, (64, 64, 64,))
instructions_rect = instructions_surf.get_rect(center=(400, 350))

score_surf = test_font.render('My game', False, (64, 64, 64))
score_rect = score_surf.get_rect(center=(400, 50))

sky_surf = pg.image.load('graphics/Sky.png').convert()
ground_surf = pg.image.load('graphics/ground.png').convert()

# snail_walk1 = pg.image.load('graphics/snail/snail1.png').convert_alpha()
# snail_walk2 = pg.image.load('graphics/snail/snail2.png').convert_alpha()
# snail_walk_list = [snail_walk1, snail_walk2]
# snail_index = 0
# snail_surf = snail_walk_list[snail_index]
# snail_surf = snail_walk_list[snail_index]
# snail_rect = snail_surf.get_rect(midbottom = (600, 300))
# fly_walk1 = pg.image.load('graphics/Fly/Fly1.png').convert_alpha()
# fly_walk2 = pg.image.load('graphics/Fly/Fly2.png').convert_alpha()
# fly_walk_list = [fly_walk1, fly_walk2]
# fly_index = 0
# fly_surf = fly_walk_list[fly_index]
# fly_rect = fly_surf.get_rect(midbottom = (600, 300))

obstacles = pg.sprite.Group()

player = pg.sprite.GroupSingle()
player.add(Player())

# player_stand = pg.image.load('graphics/Player/player_stand.png').convert_alpha()
# player_walk1 = pg.image.load('graphics/Player/player_walk_1.png').convert_alpha()
# player_walk2 = pg.image.load('graphics/Player/player_walk_2.png').convert_alpha()
# player_jump = pg.image.load('graphics/Player/jump.png').convert_alpha()
# player_index = 0
# player_walk_list = [player_walk1, player_walk2]

# player_surf = player_walk_list[0]
# player_rect = player_surf.get_rect(midbottom = (80, 300))
# player_gravity = 0 

# Timer
obstacle_timer = pg.USEREVENT + 1
pg.time.set_timer(obstacle_timer, 1500)

# Obstacle animation timer
snail_timer = pg.USEREVENT + 2
pg.time.set_timer(snail_timer, 200)
fly_timer = pg.USEREVENT + 2
pg.time.set_timer(fly_timer, 200)

while True:

    for event in pg.event.get():

        if event.type == pg.QUIT:
            pg.quit()
            exit()

        if game_active:
            # if event.type == pg.MOUSEBUTTONDOWN:
            #     if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
            #         player_gravity = -20

            # if event.type == pg.KEYDOWN:
            #     if event.key == pg.K_SPACE and player_rect.bottom >= 300:
            #         player_gravity = -20
            pass 

        else:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    # snail_rect.x = 600
                    start_time = pg.time.get_ticks() / 1000
                    game_active = True
                    obstacle_rect_list.clear()
        if game_active:
            if event.type == obstacle_timer:
                obstacles.add(Obstacles(choice(['snail', 'snail', 'fly'])))
                # if randint(0, 2):
                #     obstacle_rect_list.append(snail_surf.get_rect(bottomright = (randint(900, 1100), 300)))
                # else:
                #     obstacle_rect_list.append(fly_surf.get_rect(bottomright = (randint(900, 1100), randint( 180, 210))))

            # if event.type == snail_timer:
            #     if snail_index == 1:
            #         snail_index = 0
            #     else:
            #         snail_index = 1

            #     snail_surf = snail_walk_list[snail_index]

            # if event.type == fly_timer:
            #     if fly_index == 0:
            #         fly_index = 1
            #     else:
            #         fly_index = 0

            #     fly_surf = fly_walk_list[fly_index]
        
    if game_active:

        # Environment
        screen.blit(ground_surf,(0, 300))
        screen.blit(sky_surf,(0,0))

        # Score
        s = display_score()

        # Player
        # player_gravity += 1
        # player_rect.y += player_gravity

        # if player_rect.bottom >= 300:
        #     player_rect.bottom = 300
        # player_animation()
        # screen.blit(player_surf,player_rect)
        player.draw(screen)
        player.update()
        obstacles.draw(screen)
        obstacles.update()

        # Obstacle movement
        # obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        # Collision
        game_active = collision_sprite()
    else:
        screen.fill((94, 129, 162))
        screen.blit(over_surf, over_rect)
        screen.blit(instructions_surf, instructions_rect)
        display(s)



    pg.display.update()
    clock.tick(60)


