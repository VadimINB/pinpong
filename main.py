from pygame import *
from random import randint
SCREENSIZE = (700, 700)
BACKCOLOR = (189, 255, 0)

window = display.set_mode(SCREENSIZE)
display.set_caption('ping pong')

timer = time.Clock()

run = True

class GameSprite(sprite.Sprite):
    def __init__ (self, img, x, y, speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(img), (width, height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_left(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys [K_s] and self.rect.y + self.rect.height < SCREENSIZE[1]:
            self.rect.y += self.speed

    def update_right(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys [K_DOWN] and self.rect.y + self.rect.height < SCREENSIZE[1]:
            self.rect.y += self.speed

class Ball(sprite.Sprite):
    def __init__ (self, img, x, y, speed_x,speed_y, width, height):
        self.image = transform.scale(image.load(img), (width, height))
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def update_ball(self):
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x

        if sprite.collide_rect(self, platform_left) or sprite.collide_rect(self, platform_right):
            self.speed_x *= -1

        if self.rect.y < 0 or self.rect.y > SCREENSIZE[1] - self.rect.height:
            self.speed_y *= -1
    def who_Loze(self):
        if self.rect.x > SCREENSIZE[0] - self.rect.width:
            return "right"
        elif self.rect.x < 0:
            return "left"
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    
class Wall():
    def __init__(self,x,y,width,height,color):
        self.rect = Rect(x,y,width,height)
        self.color = color
    def draw(self):
        draw.rect(window,self.color,self.rect)

x = randint(3,6)
y = randint(2,6)
wall_1 = Wall(345,0,10,700,(0,178,0))
bal = Ball("ball.png",330,330,x,y,50,50)
finish = False

platform_left = Player("platform.png",20,350, 7,25,99)
platform_right = Player("platform.png",660,350,7,25,99)

font.init()
font = font.Font(None,50)


while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    if finish != True:
        window.fill(BACKCOLOR)
        draw.circle(window, (0, 175,0), (345, 345), 150, 10)
        wall_1.draw()
        platform_left.reset()
        platform_right.reset()
        platform_left.update_left()
        platform_right.update_right() 
        bal.reset()
        bal.update_ball()
        if bal.who_Loze() == "right":
            loze = font.render("Правый проиграл!!!!",True,(213,32,192))
            window.blit(loze,(350,20))
            finish = True
        if bal.who_Loze() == "left":
            loze = font.render("Левый проиграл!!!!",True,(213,32,192))
            window.blit(loze,(350,20))
            finish = True
    display.update()
    timer.tick(60)