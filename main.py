# File created by: Chris Cozort
# Agenda:
# gIT GITHUB    
# Build file and folder structures
# Create libraries
# testing github changes
# I changed something - I changed something else tooooo!

# This file was created by: Chris Cozort
# Sources: http://kidscancode.org/blog/2016/08/pygame_1-1_getting-started/
# Sources: 

# import libs
import pygame as pg
import os
# import settings 
from settings import *
from sprites import *
from os import path
# from pg.sprite import Sprite



# set up assets folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")

def load_data(self):
    self.player_img = pg.image.load(path.join(img_folder, "yb.jpeg"))
# create game class in order to pass properties to the sprites file

class Game:
    def __init__(self):
        # init game window etc.
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("my game")
        self.clock = pg.time.Clock()
        self.running = True
        print(self.screen)
    def new(self):
        # starting a new game
        self.load_data()
        self.score = 0
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        self.player = Player(self)
        self.plat1 = Platform(WIDTH, 50, 0, HEIGHT-50, (255,255,0), "normal")
        self.plat2 = Platform(50, 25, 200, 400, (255,255,0), "normal")
        self.plat3 = Platform(50, 25, 350, 200, (255,255,0), "normal")
        self.plat4 = Platform(50, 25, 100, 300, (255,255,0), "normal")
        self.plat5 = Platform(50, 25, 500, 350, (255,255,0), "normal")
        self.plat6 = Platform(50, 25, 600, 425, (255,255,0), "normal")
        self.plat7 = Platform(50, 25, 650, 285, (255,255,0), "normal")
        self.plat8 = Platform(50, 25, 650, 100, (255,255,0), "normal")
        self.plat9 = Platform(50, 25, 50, 150, (255,255,0), "normal")
        self.plat10 = Platform(50, 25, 400, 650, (255,255,0), "normal")
        # self.plat1 = Platform(WIDTH, 50, 0, HEIGHT-50, (150,150,150), "normal")
        self.all_sprites.add(self.plat1)
        self.all_sprites.add(self.plat2)
        self.all_sprites.add(self.plat3)
        self.all_sprites.add(self.plat4)
        self.all_sprites.add(self.plat5)
        self.all_sprites.add(self.plat6)
        self.all_sprites.add(self.plat7)
        self.all_sprites.add(self.plat8)
        self.all_sprites.add(self.plat9)
        self.all_sprites.add(self.plat10)


        self.platforms.add(self.plat1)
        self.platforms.add(self.plat2)
        self.platforms.add(self.plat3)
        self.platforms.add(self.plat4)
        self.platforms.add(self.plat5)
        self.platforms.add(self.plat6)
        self.platforms.add(self.plat7)
        self.platforms.add(self.plat8)
        self.platforms.add(self.plat9)
        self.platforms.add(self.plat10)

        
        self.all_sprites.add(self.player)
        for i in range(0,10):
            m = Mob(20,20,(0,255,0))
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
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()
    def update(self):
        self.all_sprites.update()
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                if hits[0].variant == "dissapearing":
                    hits[0].kill()
                elif hits[0].variant == "icey":
                    self.player.pos.y = hits[0].rect.top
                    self.player.vel.y = 0
                    PLAYER_FRICTION = 0
                elif hits[0].variant == "bouncey":
                    self.player.pos.y = hits[0].rect.top
                    self.player.vel.y = -PLAYER_JUMP
                else:
                    self.player.pos.y = hits[0].rect.top
                    self.player.vel.y = 0

    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        # is this a method or a function?
        pg.display.flip()
    def draw_text(self, text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text_surface, text_rect)
    def get_mouse_now(self):
        x,y = pg.mouse.get_pos()
        return (x,y)

# instantiate the game class...
g = Game()

# kick off the game loop
while g.running:
    g.new()

pg.quit()