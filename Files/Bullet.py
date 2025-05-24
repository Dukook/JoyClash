import pygame
from math import cos, sin, radians
from random import randint

angle_diff=12

class Bullet :
    def __init__(self, brawleur, block, speed):
        self.block=block
        self.speed=speed
        if brawleur=="Owleaf" :
            self.image=[]
            scaling=(block/2)/(pygame.image.load(f"Images/a_{brawleur}_0.png").convert_alpha().get_height())
            for x in range(3) :
                self.image.append(pygame.transform.scale_by(pygame.image.load(f"Images/a_{brawleur}_{x}.png").convert_alpha(), scaling))
            
        elif brawleur=="Paper Dukook" :
            self.image=[]
            for x in range(8) :
                self.image.append(pygame.transform.scale(pygame.image.load(f"Images/a_{brawleur}_{x}.png").convert_alpha(), (1.2*self.block, 1.2*self.block)))
        else :
            try : 
                self.image=pygame.image.load(f"Images/a_{brawleur}.png").convert_alpha()
            except :
                self.image=pygame.transform.rotate(pygame.image.load(f"Images/goat_Surge.png").convert_alpha(),90)
            scaling=(block/2)/(self.image.get_height())
            self.image=pygame.transform.scale_by(self.image, scaling)
            self.rect=self.image.get_rect(x=-1000, y=-1000)

    def settings(self, x, y, angle, acc) :
        if not acc :
            angle+=randint(-30, 30)
        self.image2=pygame.transform.rotate(self.image, angle)
        self.rect=self.image2.get_rect(x=x+self.block/2-self.image2.get_width()/2, y=y+self.block/2-self.image2.get_height()/2)
        self.x=cos(radians(angle))*self.block/(3*self.speed)
        self.y=-sin(radians(angle))*self.block/(3*self.speed)

    def settings_paper(self, x, y, angle, acc, n) :
        if not acc :
            angle+=randint(-30, 30)
        self.image2=pygame.transform.rotate(self.image[n], angle)
        self.rect=self.image2.get_rect(x=x+self.block/2-self.image2.get_width()/2, y=y+self.block/2-self.image2.get_height()/2)
        self.x=cos(radians(angle))*self.block/(3*self.speed)
        self.y=-sin(radians(angle))*self.block/(3*self.speed)

    def settings_owl(self, x, y, angle, acc) :
        self.power=[]
        if not acc :
            angle+=randint(-30, 30)
        for z in range(3):
            self.power.append(randint(0,2))
        self.image2=(pygame.transform.rotate(self.image[self.power[0]], angle-angle_diff), pygame.transform.rotate(self.image[self.power[1]], angle), pygame.transform.rotate(self.image[self.power[2]], angle+angle_diff))
        self.rect=[]
        for dague in self.image2 :
            self.rect.append(dague.get_rect(x=x+self.block/2-dague.get_width()/2, y=y+self.block/2-dague.get_height()/2))  
        blt_spd=self.block/(3*self.speed)
        self.x=[(cos(radians(angle-angle_diff))*blt_spd), (cos(radians(angle))*blt_spd), (cos(radians(angle+angle_diff))*blt_spd)]
        self.y=[-(sin(radians(angle-angle_diff))*blt_spd), -(sin(radians(angle))*blt_spd), -(sin(radians(angle+angle_diff))*blt_spd)]
        self.dagues=[True, True, True]

    def event(self) :
        pass

    def update(self) :
        
        self.rect.x+=self.x
        self.rect.y+=self.y

    def updateowl(self) :
        for x in range(len(self.rect)):
            if self.dagues[x] :
                temprect=self.rect[x]
                temprect.x+=self.x[x]
                temprect.y+=self.y[x]
                self.rect[x]=temprect

    def updatex(self) :
        self.rect.x+=self.x

    def updatey(self) :
        self.rect.y+=self.y
        

    def draw(self, screen):
        screen.blit(self.image2, self.rect)

    def drawowl(self, screen):
        for x in range(len(self.rect)):
            if self.dagues[x] :
                screen.blit(self.image2[x], self.rect[x])

