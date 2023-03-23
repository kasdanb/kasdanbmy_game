# Created By Kasdan blattman
# Agenda:
# gIT GITHUB    
# Build file and folder structures
# Create libraries
# testing github changes
# I changed something - I changed something else tooooo!

# import libs
import pygame as pg
import random
import os
# import settings 
from settings import *
from sprites import *
# from pg.sprite import Sprite

#set up asset folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder)


#create game class in order to pass properties to the sprites file
class Game:
    def __init__(self):
        #init game window etc.
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("my game")
        self.clock = pg.time.Clock()
        self.running = True

    def new(self):
        #starting a new game
        self.score = 0
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        self.player = Player()
        self.all_sprites.add(Player)
        for i in range(0,10):
            m = Mob(20,20,(0,255,))
            self.all_sprites.add(m)
            self.enemies.add(m)
        self.run()
    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type ==pg.KEYDOWN:
                if event.key ==pg.K_SPACE:
                    self.player.jump()
    def update(self):
    def draw(self):
    def draw_text(text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        screen.blit(text_surface, text_rect)
    def get_mouse_now():
        x,y = pg.mouse.get_pos()
        return (x,y)
    

g = Game()

While g.running:
    g.new()

pg.quit()
    



 
# set up assets folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")
# 


def get_mouse_now():
    x,y = pg.mouse.get_pos()
    return (x,y)

# init pg and create window
pg.init()
# init sound mixer
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("My first game...")
clock = pg.time.Clock() 

# i have a group of sprites, allows you to update all sprites at the same time
all_sprites = pg.sprite.Group()
enemies = pg.sprite.Group()

player = Player()

all_sprites.add(player)
player.pos = (0,0)

# creates a for loop that creates 20 mobs
# 
for i in range(0,20):
    # instantiate mobs
    m = Mob(randint(30,90), randint(30, 90), (255,0,0))
    # add enemies to enemies and all_sprites...
    enemies.add(m)
    all_sprites.add(m)

print(enemies)
# game loop



while RUNNING:
    #  keep loop running at the right speed
    clock.tick(FPS)
    ### process input events section of game loop
    for event in pg.event.get():
        # check for window closing
        if event.type == pg.QUIT:
            RUNNING = False
            # break
    # print(get_mouse_now())
    ### update section of game loop (if updates take longer the 1/30th of a second, you will get laaaaag...)
    def input(self):
        keystate = pg.key.get_pressed()
        if keystate[pg.K_ESCAPE]:
            print ('this is working')
            if event.key
            PAUSED == True
    if PAUSED != True:
        all_sprites.update()
        enemies.update()

    # if player hits enemies
    blocks_hit_list = pg.sprite.spritecollide(player, enemies, True)
    if blocks_hit_list:
        SCORE += 1

    for block in blocks_hit_list:
        print(block)
        pass
    
    ### draw and render section of game loop
    screen.fill(BLUE)
    all_sprites.draw(screen)
    draw_text("Score: " + str(SCORE), 22, WHITE, WIDTH/2, HEIGHT/10)

    # double buffering draws frames for entire screen
    pg.display.flip()
    # pg.display.update() -> only updates a portion of the screen
# ends program when loops evaluates to false
pg.quit()