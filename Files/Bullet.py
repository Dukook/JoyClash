import pygame
from math import *
from random import randint
from os import chdir

chdir("D:\JoyClashV3\Files")

class Bullet :
    def __init__(self, x, y, angle, brawleur, acc, block, speed):
        self.image=pygame.image.load(f"Images/a_{brawleur}.png").convert_alpha()
        if not acc :
            angle+=randint(-30, 30)
        scaling=(block/2)/(self.image.get_height())
        self.image=pygame.transform.scale_by(self.image, scaling)
        self.image=pygame.transform.rotate(self.image, angle)
        self.rect=self.image.get_rect(x=x+block/2-self.image.get_width()/2, y=y+block/2-self.image.get_height()/2)
        self.x=cos(radians(angle))*block/(3*speed)
        self.y=-sin(radians(angle))*block/(3*speed)

    def event(self) :
        pass

    def update(self) :
        
        self.rect.x+=self.x
        self.rect.y+=self.y
        

    def draw(self, screen):
        screen.blit(self.image, self.rect)

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