from pygame import *
from random import randint
window = display.set_mode((700,500))
display.set_caption('Catch')
background = transform.scale(image.load('table.png'),(700,500))
window.blit(background,(0,0))
mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
clock = time.Clock()
FPS = 60
mixer.music.set_volume(0.2)
class Ball(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed,size_x,size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(size_x,size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x,self.rect.y))
    def update(self):
        if self.rect.x <= 700 :
            self.rect.x -= self.speed
        if self.rect.y <= 500 :
            self.rect.y += self.speed
        if self.rect.x >= 700 :
            self.rect.x += self.speed
        if self.rect.y >= 500 :
            self.rect.y -= self.speed
class P1(sprite.Sprite):
    def __init__ (self,x,y,speed):
        super().__init__()
        self.image = Surface((40,230))
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def draw_wall(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 300:
            self.rect.y += self.speed
class P2(sprite.Sprite):
    def __init__ (self,x,y,speed):
        super().__init__()
        self.image = Surface((40,230))
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def draw_wall(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 300:
            self.rect.y += self.speed
player1 = P1(50,160,10)
player2 = P2(600,160,10)
ball1 = Ball('ball.png',330,250,1,50,40)
game = True
while game :
    for e in event.get():
        if e.type == QUIT:
            game = False
    clock.tick(FPS)
    window.blit(background,(0,0))
    player1.draw_wall()
    player1.update()
    player2.draw_wall()
    player2.update()
    ball1.reset()
    ball1.update()
    display.update()