import pygame
from math import *
from random import randint
from os import chdir

chdir("D:\JoyClashV4\Files")

class Bullet :
    def __init__(self, brawleur, block, speed):
        self.image=pygame.image.load(f"Images/a_{brawleur}.png").convert_alpha()
        self.block=block
        scaling=(block/2)/(self.image.get_height())
        self.image=pygame.transform.scale_by(self.image, scaling)
        
        self.rect=self.image.get_rect(x=-1000, y=-1000)
        self.speed=speed
        

    def settings(self, x, y, angle, acc) :
        if not acc :
            angle+=randint(-30, 30)
        self.image=pygame.transform.rotate(self.image, angle)
        self.rect.x, self.rect.y=x+self.block/2-self.image.get_width()/2, y+self.block/2-self.image.get_height()/2
        self.x=cos(radians(angle))*self.block/(3*self.speed)
        self.y=-sin(radians(angle))*self.block/(3*self.speed)

    def event(self) :
        pass

    def update(self) :
        
        self.rect.x+=self.x
        self.rect.y+=self.y
        

    def draw(self, screen):
        screen.blit(self.image, self.rect)

