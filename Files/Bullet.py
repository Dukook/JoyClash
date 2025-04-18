import pygame
from math import cos, sin, radians
from random import randint

class Bullet :
    def __init__(self, brawleur, block, speed):
        self.block=block
        self.speed=speed
        self.image=pygame.image.load(f"Images/a_{brawleur}.png").convert_alpha()
        self.rect=self.image.get_rect(x=-100, y=-100)

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

