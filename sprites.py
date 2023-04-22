import pygame as pg
from pygame.sprite import Sprite
from settings import *
from random import randint
from random import randrange

vec = pg.math.Vector2

# player class

class Player(Sprite):
    def __init__(self, game):
        Sprite.__init__(self)
        # these are the properties
        self.game = game
        #Along with self_load, this changes the main sprite to an image
        self.image = pg.image.load('icespice.jpeg').convert_alpha()
        self.image = pg.transform.scale(self.image, (70, 70))
        # self.image_orig = pg.transform.scale(game.player_img, (64, 64))
        self.image.set_colorkey(WHITE)
# All the movement rules for the main sprite + size and appearance
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .85 / 2)
        self.pos = vec(0, 0)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.cofric = 0.1
        self.canjump = False
        self.rot = 0
        self.rot_speed = 0
        self.last_update = pg.time.get_ticks()
        self.left_key = pg.K_a
        self.health = 100

    def input(self):
        #more movement rules for the player, allows player to go side to side at certain speed
        keystate = pg.key.get_pressed()
        if keystate[self.left_key]:
            self.acc.x = -PLAYER_ACC
            self.rot_speed = 8
        if keystate[pg.K_d]:
            self.acc.x = PLAYER_ACC
            self.rot_speed = -8
    
    def jump(self):
        #Allows player to jump with space bar
        self.rect.x += 1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 1
        if hits and self.canjump:
            self.vel.y = -PLAYER_JUMP
    
    def inbounds(self):
        # Allows player to go to the other side of the screen when they fall off the other side, like pacman
        # All print lines are shown in terminal but not in window
        if self.rect.x > WIDTH - 50:
            self.pos.x = WIDTH - 25
            self.vel.x = 0
            print("i am off the right side of the screen...")
        if self.rect.x < 0:
            self.pos.x = 25
            self.vel.x = 0
            print("i am off the left side of the screen...")
        if self.rect.y > HEIGHT:
            print("i am off the bottom of the screen")
        if self.rect.y < 0:
            print("i am off the top of the screen...")

    def mob_collide(self):
            #adds point to score when main sprite collects coins
            hits = pg.sprite.spritecollide(self, self.game.enemies, True)
            if hits:
                print("you collided with an enemy...")
                self.game.score += 1

    def update(self):
        # This chunk allows player movement and the speed that the main sprite is able to move at 
        self.rot_speed = 0
        if self.rot > 312 or self.rot < 56:
            self.canjump = True
        else:
            self.canjump = False
        self.acc = vec(0, PLAYER_GRAV)
        self.acc.x = self.vel.x * PLAYER_FRICTION
        self.input()
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        # self.rotate()
        if self.pos.x < 0:
            self.pos.x = WIDTH
        if self.pos.x > WIDTH:
            self.pos.x = 0
        self.rect.midbottom = self.pos
        

class Mob(Sprite):
    def __init__(self, game, width,height, color):
        Sprite.__init__(self)
        #creating dimensions of mob sprites
        self.game = game
        self.width = width
        self.height = height
        #changing "mob" sprites to image of coins
        self.image = pg.image.load('coin.jpeg').convert_alpha()
        self.image = pg.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
        #positions the coins at random points around the window, also more movement rules for the coins
        self.pos = vec(randint(0,WIDTH), randint(0,HEIGHT))
        self.vel = vec(0,0)
        self.acc = vec(1,1)
        self.cofric = 0.01
        self.attached_now = False

    # Jumping rules for main sprite
    def jump(self):
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        if hits:
            if self.vel.y > 1:
                self.vel = vec(5,-10)
            else:
                self.pos.y = hits[0].rect.top
                self.vel.y = 0
        else:
            self.vel.x = 0
    #attaches the coins to the player after the player collects them from 126-138
    def attached(self, obj):
        if self.attached_now:
            self.pos = obj.pos - vec(0,16) + vec(randint(-64,64), randint(-64,64))
    def update(self):
        if not self.attached_now:
            self.acc = vec(0, PLAYER_GRAV)
            self.jump()
            self.acc.x = self.vel.x * PLAYER_FRICTION
            self.vel += self.acc
            self.pos += self.vel + 0.5 * self.acc
        else:
            self.attached(self.game.player)
        self.rect.midbottom = self.pos

# create a new platform class...
# Displays them on the screen and gives them color and size
class Platform(Sprite):
    def __init__(self, x, y, width, height, color, variant):
        Sprite.__init__(self)
        self.width = width
        self.height = height
        self.image = pg.Surface((self.width,self.height))
        self.color = color
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.variant = variant


