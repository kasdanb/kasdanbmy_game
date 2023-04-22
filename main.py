#file created by kasdan Blattman
# import libs
import pygame as pg
import os
# import settings 
from settings import *
from sprites import *
from math import *
from math import ceil
from os import path

pg.init()
# from pg.sprite import Sprite

# set up assets folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "images")



class Game:
    def __init__(self):
        # init game window 
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("my game")
        self.clock = pg.time.Clock()
        self.running = True
        self.score = 0
        self.win = False
        self.lose = False
    
    # gets the image from folder 
    def load_data(self):
        self.player_img = pg.image.load(path.join(img_folder, "icespice.jpeg")).convert()

    def new(self):
        # starting a new game
        self.score = 0

        # added to load data, sets all of the plats, sprites, and player onto pygame window
        self.load_data()
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.plat_list = []
        self.enemies = pg.sprite.Group()
        self.attached_items = pg.sprite.Group()
        self.player = Player(self)
        self.plat1 = Platform(WIDTH, 50, 0, HEIGHT-50, (150,150,150), "normal")
        self.all_sprites.add(self.player)
        self.all_sprites.add(self.plat1)
        self.platforms.add(self.plat1)
        
        
        for plat in PLATFORM_LIST:
            p = Platform(*plat)
            self.all_sprites.add(p)
            self.platforms.add(p)
        for i in range(0,15):
            # puts plats on random places on window, making a new random "map" every time
            p = Platform(randint(0,WIDTH-50), randint(0,HEIGHT-50), 100, 25, BLACK, "normal")
            self.all_sprites.add(p)
            self.platforms.add(p)
            self.plat_list.append(p)
            if i != 0:
                print(abs(self.plat_list[i-1].rect.x - self.plat_list[i].rect.x) > 25 and
                      abs(self.plat_list[i-1].rect.y - self.plat_list[i].rect.y) > 25)  
                if (abs(self.plat_list[i-1].rect.x - self.plat_list[i].rect.x) > 100 and
                      abs(self.plat_list[i-1].rect.y - self.plat_list[i].rect.y) > 100):
                    print("i need to adjust this platform...") 
                    p.image.fill(RED)
                    p.rect.x -= 50
                    p.rect.y -= 50
                self.all_sprites.add(p)
                self.platforms.add(p)
                self.plat_list.append(p)
            
        for i in range(0,10):
            # if player gets close enough to get coins, the coin will get collected
            #also creates mobs and puts them in random places on map
            m = Mob(self, 20,20,(0,255,0))
            self.all_sprites.add(m)
            self.enemies.add(m)
        self.start_score = len(self.platforms)
        self.run()
    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
    
    def events(self):
        # jump command for player
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

        # check to see if we collide with enemyd
        mhits = pg.sprite.spritecollide(self.player, self.enemies, False)
        if mhits:
            # adds score to scoreboard when player collects coins
            mhits[0].attached_now = True
            self.enemies.remove(mhits[0])
            self.attached_items.add(mhits[0])
            self.score += 1
            
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                if abs(self.player.vel.x) > abs(self.player.vel.y):
                    if self.player.vel.x > 0:
                        pass
                        # print("Im going faster on the x and coming from the left...")
                if hits[0].variant == "disappearing":
                    hits[0].kill()
                elif hits[0].variant == "bouncey":
                    self.player.pos.y = hits[0].rect.top
                    self.player.vel.y = -PLAYER_JUMP
                elif hits[0].variant == "winner" and len(self.enemies) == 0:
                    self.win = True
                else:
                    self.player.pos.y = hits[0].rect.top
                    self.player.vel.y = 0
    
    def draw(self):
        self.screen.fill(BLUE)
        self.all_sprites.draw(self.screen)


        if not self.win:
            # self.draw_text(str(self.player.rot), 24, WHITE, WIDTH/2, HEIGHT/2)
            self.draw_text(str(self.score), 24, WHITE, WIDTH/2, HEIGHT/2)
        else:
            self.draw_text("You win!", 24, WHITE, WIDTH/2, HEIGHT/2)

        #displays score in the middle of the screen
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
    
 # Define the screen width and height
screen_width = 800
screen_height = 600

# lines 163-174 I was trying to display the objective of the game on the screen
# Copied chunk from RPS code, but was not working
screen = pg.display.set_mode((screen_width, screen_height))   
screen_rect = screen.get_rect() 

def render_message(text): 
    m = font.render(text, True, RED)
    m_rect = m.get_rect()
    m_rect.top = screen_rect.bottom - (m_rect.bottom - m_rect.top)
    return (m, m_rect)

font = pg.font.SysFont(None,48)
(message, message_rect) = render_message("Collect the Coins to Win")


pg.display.flip()



# instantiate the game class
g = Game()

# kick off the game loop
while g.running:
    g.new()

pg.quit()








