import pygame
from pygame.math import Vector2
from os import chdir

chdir("D:\JoyClashV3\Files")
pygame.font.init()
font = pygame.font.Font("Others/arial.ttf", 20)

capa={"Hank" : (1320, 210, 0.9, 1.2),
      "Berry": (1000, 230, 1.1, 1.2),
      "Surge": (1260, 225, 0.9, 1.3),
      "Carroje": (1080, 280, 0.8, 1.7),
      "Popofox": (1150, 155, 1.2, 0.6),
      "Spookie": (1220, 150, 1.0, 1.0),
      "Mushy": (1050, 130, 1.05, 1.5),
      "Bubule": (1400, 200, 0.85, 0.9),
      "UIIA": (1800, 310, 1.5, 0.65)
}

class Player :
    def __init__(self, x, y, perso, zone_morte, WIDTH, HEIGH, j, block, autre_j_manque_dinspi):
        self.block=block
        self.pers=perso
        self.capa=capa[perso]
        self.base_speed=self.capa[2]
        try :
            self.image=pygame.image.load(f"Images/u_{perso}.png").convert_alpha()
        except :
            self.image=pygame.image.load(f"Images/goat_Surge.png").convert_alpha()
        self.image=pygame.transform.scale(self.image, (self.block,self.block))
        self.rect=self.image.get_rect(x=x,y=y)

        self.vise=pygame.image.load("Images/vise3.png").convert_alpha()
        self.vise=pygame.transform.scale(self.vise, (20*self.block,10*self.block))

        

        self.joy=pygame.joystick.Joystick(autre_j_manque_dinspi)
        self.joy.init()
        
        self.PV=self.capa[0]
        self.speed=2
        self.stamina=2500
        self.can=True
        self.stamina_speed=1
        self.reloading=False
        self.sprinting=False
        self.x1=x
        self.y1=y
        self.zone_morte=zone_morte
        self.WIDTH=WIDTH
        self.HEIGH=HEIGH
        self.ticks=0 
        self.shot_acc=[not not not not False, not True]#lol
        self.canshoot=True
        self.lock=False
        self.death=pygame.transform.scale(pygame.image.load("Images/death.png").convert_alpha(), (18*self.block, 18*self.block))
        self.i_death=0
        self.modif=1
        self.modif2=1
        if j==0 :
            self.stam_pos = (30,20, 100)
            self.right,self.left=True, False
            self.axe_x1, self.axe_y1=1, 0
            self.death=pygame.transform.rotate(self.death, -90)
        else :
            self.stam_pos = (WIDTH-80, 20, WIDTH-150)
            self.right,self.left=False, True
            self.axe_x1, self.axe_y1=-1, 0
            self.death=pygame.transform.rotate(self.death, 90)
        self.j=j


        self.up, self.down=False, False


    def event(self) :
        lock=self.joy.get_button(5)
        shoot=self.joy.get_button(1)
        sprint=self.joy.get_button(0)
        vibr=self.joy.get_button(2)
        self.axe_x1=self.joy.get_axis(0)*self.modif*self.modif2
        self.axe_y1=self.joy.get_axis(1)*self.modif*self.modif2
        self.vec = Vector2(self.axe_x1,self.axe_y1)
        self.rad, self.angle = self.vec.as_polar() # le rad est inutile mais je veux pas ça crash
        self.ajusted_angle = (360-self.angle) % 360
        

        
        

        
        if vibr :
            self.joy.rumble(1,1,1)

        #direction joueur
        if self.axe_x1>self.zone_morte :
            self.right=True
        else :
            self.right=False
        if self.axe_x1<-self.zone_morte :
            self.left=True
        else :
            self.left=False
        if self.axe_y1>self.zone_morte :
            self.down=True
        else :
            self.down=False
        if self.axe_y1<-self.zone_morte :
            self.up=True
        else :
            self.up=False

        
        #recharge stamina plus élevé si le joueur ne bouge pas
        if (not self.up and not self.down and not self.right and not self.left):
            self.ajusted_angle=None
            self.stamina_speed=4
        if lock :
            self.stamina_speed=4

        #variation de l'endurance
        if sprint and not lock and self.stamina>=20 and self.can and (self.left or self.up or self.right or self.down):
            self.stamina-=20
            self.sprinting=True
        else :
            self.sprinting=False
            if self.stamina<5000 :
                self.stamina+=self.stamina_speed
                if self.stamina>5000 :
                    self.stamina=5000
        if self.stamina<20 :
            self.can=False
        elif self.stamina>=1000 :
            self.can=True
        

        #variation de vitesse
        if self.sprinting :
            self.speed=0.15
        elif not self.can or self.reloading :
            self.speed=0.075
        else :
            self.speed=0.115

        #déplacements
        if self.right and self.x1<self.WIDTH-self.block and not lock:
            self.x1+=self.speed*round(self.axe_x1,1)*self.block*self.base_speed
            self.stamina_speed=2
        elif self.left and self.x1>0 and not lock :
            self.x1+=self.speed*round(self.axe_x1,1)*self.block*self.base_speed
            self.stamina_speed=2

        if self.down and self.y1<self.HEIGH-self.block and not lock :
            self.y1+=self.speed*round(self.axe_y1,1)*self.block*self.base_speed
            self.stamina_speed=2
        elif self.up and self.y1>0 and not lock :
            self.y1+=self.speed*round(self.axe_y1,1)*self.block*self.base_speed
            self.stamina_speed=2

        #shoot
        if shoot and self.canshoot and self.ajusted_angle!=None:
            if lock :
                self.shot_acc=[True, True]
            else :
                self.shot_acc=[True, False]

        if lock and self.ajusted_angle!=None :
            self.lock=True#pas envie de changer la variable un peu partout
            self.vise2=pygame.transform.rotozoom(self.vise, self.ajusted_angle, 1)
        else :
            self.lock=False
            
        #les print qui carry
        '''if self.j==0 :
            print(self.ajusted_angle)'''
        '''print(self.player.stamina)'''

    def update(self) :
        self.radius=int(self.stamina//200)
        self.color=(max(255-self.stamina//15,0), max(min(self.stamina//4-300,255),0), 0)
        if self.pers!="UIIA" :
            if self.up and abs(self.axe_y1)>abs(self.axe_x1) :
                self.new_image=self.image
            elif self.left and abs(self.axe_x1)>abs(self.axe_y1) :
                self.new_image=pygame.transform.rotate(self.image, 90)
            elif self.down and abs(self.axe_y1)>abs(self.axe_x1) :
                self.new_image=pygame.transform.rotate(self.image, 180)
            elif self.right and abs(self.axe_x1)>abs(self.axe_y1) :
                self.new_image=pygame.transform.rotate(self.image, -90)
        else :
            if self.right :
                self.new_image=pygame.transform.flip(self.image, True, False)
            elif self.left :
                self.new_image=self.image
        if self.i_death>0.2*self.block :
            self.i_death-=0.2*self.block
        
        if self.j==0 :
            self.pos_death=((-6*self.block-self.PV/self.capa[0]*12*self.block)+self.i_death,0)
        else :
            self.pos_death=((20*self.block+self.PV/self.capa[0]*12*self.block)-self.i_death, 0)


    def move_x(self, x1):
        self.tx1=self.rect.x
        self.rect.x=x1
    def unmove_x(self, tx1):
        self.x1=tx1
        self.rect.x=self.x1

    def move_y(self, y1):
        self.ty1=self.rect.y
        self.rect.y=y1
    def unmove_y(self, ty1):
        self.y1=ty1
        self.rect.y=self.y1

    def draw(self, screen):
        #pers 1ligne btw
        screen.blit(self.new_image, self.rect)

    def drawstuff(self, screen):
        #la visée
        if self.lock :
            len_de_la_rotation_qui_clc_dans_pygame=[self.vise2.get_width(), self.vise2.get_height()]
            screen.blit(self.vise2, (self.rect.x-len_de_la_rotation_qui_clc_dans_pygame[0]/2+self.block/2,self.rect.y-len_de_la_rotation_qui_clc_dans_pygame[1]/2+self.block/2))

        #mort
        screen.blit(self.death, self.pos_death)

        

        #la stamina, bcp trop  long a mon gout
        self.contours = pygame.Surface((50, 50), pygame.SRCALPHA)
        if self.can :
            pygame.draw.circle(self.contours, (150, 150, 150, 60), (25, 25), 25)
        else :
            pygame.draw.circle(self.contours, (255, 150, 150, 60), (25, 25), 25)
        screen.blit(self.contours, (self.stam_pos[0], self.stam_pos[1]))
        pygame.draw.circle(screen, self.color, (self.stam_pos[0]+25, self.stam_pos[1]+25), self.radius)
        if not self.sprinting and self.stamina<5000 :
            self.rad_blue=(self.ticks%200)//8
            if self.stamina_speed==4 :
                self.ticks+=3
            else :
                self.ticks+=1
            pygame.draw.circle(screen, "blue", (self.stam_pos[0]+25, self.stam_pos[1]+25), self.rad_blue, 3)
        else :
            self.ticks=0

        #les PV
        text_PV = font.render(str(int(self.PV)), True, "orange")
        screen.blit(text_PV, (self.stam_pos[2], self.stam_pos[1]*1.8))

        


