import pygame
from math import cos, sin, radians
from random import randint

class Bullet :
    def __init__(self, brawleur, block, speed):
        self.block=block
        self.speed=speed
        self.image=pygame.image.load(f"Images/a_{brawleur}.png").convert_alpha()
        
        scaling=(block/2)/(self.image.get_height())
        self.image=pygame.transform.scale_by(self.image, scaling)
        
    def settings(self, x, y, angle, acc) :
        if not acc :
            angle+=randint(-30, 30)
        self.image2=pygame.transform.rotate(self.image, angle)
        self.rect=self.image2.get_rect(x=x+self.block/2-self.image2.get_width()/2, y=y+self.block/2-self.image2.get_height()/2)
        self.x=cos(radians(angle))*self.block/(3*self.speed)
        self.y=-sin(radians(angle))*self.block/(3*self.speed)


    def event(self) :
        pass

    def update(self) :
        
        self.rect.x+=self.x
        self.rect.y+=self.y
        

    def draw(self, screen):
        screen.blit(self.image2, self.rect)

class Surge :

    def __init__(self, x, y, block):
        self.rect=pygame.rect.Rect(x-block, y-block, 3*block, 3*block)
        self.image=pygame.transform.scale(pygame.image.load("Images/boom.png").convert_alpha(), (3*block, 3*block))

    def draw(self, screen) :
        screen.blit(self.image, self.rect)

class Berry :

    def __init__(self, x, y, block):
        self.rect=pygame.rect.Rect(x-0.75*block, y-0.75*block, 2.5*block, 2.5*block)
        self.image=pygame.transform.scale(pygame.image.load("Images/ice_cream.png").convert_alpha(), (2.5*block, 2.5*block))

    def draw(self, screen) :
        screen.blit(self.image, self.rect)

class Spookie :

    def __init__(self, x, y, block):
        self.rect=pygame.rect.Rect(x-2*block, y-2*block, 5*block, 5*block)
        self.image=pygame.transform.scale(pygame.image.load("Images/Cookie.png").convert_alpha(), (5*block, 5*block))

    def draw(self, screen) :
        screen.blit(self.image, self.rect)