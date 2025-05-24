import pygame
from pygame.math import Vector2

pygame.font.init()
font = pygame.font.Font("Others/arial.ttf", 20)


# "nom" : [PV, Damage, speed, bulletspeed, range, spam, nb_bullet]
capa={"Hank" : (1320, 210, 0.9, 1.2,700, 1300, 6),
      "Berry": (1000, 230, 1.1, 1.2, 600, 1200, 5),
      "Surge": (1260, 225, 0.9, 1.3, 650, 1300, 4),
      "Carroje": (1080, 280, 0.8, 1.7, 1200, 1300, 4),
      "Popofox": (1150, 155, 1.2, 0.6, 450, 700, 30),
      "Spookie": (1220, 150, 1.0, 1.0, 650, 1400, 5),
      "Mushy": (1050, 130, 1.05, 1.1, 500, 1450, 8),
      "Bubule": (1400, 200, 0.85, 0.9, 600, 1000, 10),
      "Chick'n bob": (950, 37, 1.25, 0.9, 500, 1100, 7),
      "Owleaf": (1300, 170, 1.0, 1.1, 650, 1450, 3),
      "Squeak": (1350, 180, 0.9, 1.0, 800, 1300, 5),
      "Furbok": (1500, 310, 0.75, 0.7, 700, 2200, 2),
      "Zipit": (1220, 280, 1.0, 0.8, 650, 1500, 3),
      "Semibot": (1280, 260, 1.2, 0.85, 750, 1250, 5),
      "Chauss-être": (1450, 8, 1.1, 1.0, 250, 450, 6),
      "Paper Dukook": (1200, 180, 1.1, 1.1, 720, 1200, 8),
      "UIIA": (1800, 310, 1.5, 0.65, 1300, 1300, 69)
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
        self.vise=pygame.transform.scale(self.vise, ((self.capa[4]*self.block)*0.032/self.capa[3],10*self.block))

        

        self.joy=pygame.joystick.Joystick(autre_j_manque_dinspi)
        self.joy.init()
        
        self.PV=self.capa[0]
        self.speed=2
        self.slow=1
        self.stamina=2500
        self.can=True
        self.canvibr=True
        self.stamina_speed=1
        self.reloading=False#jamais utilisé yet
        self.ammo=self.capa[6]
        self.sprinting=False
        self.x1=x
        self.y1=y
        self.zone_morte=zone_morte
        self.WIDTH=WIDTH
        self.HEIGH=HEIGH
        self.ticks=0 
        self.shot_acc=[not not not not False, not True]#lol
        self.canshoot=True
        self.shooting=False
        self.canhit=True
        self.hitwall=False
        self.explosion=True
        self.range=0
        self.duration_bullet=-1000
        self.time_effect=-1000
        self.furb=0
        self.furb2=1
        self.furb22=1
        self.lock=False
        self.death=pygame.transform.scale(pygame.image.load("Images/death.png").convert_alpha(), (18*self.block, 18*self.block))
        self.i_death=0
        self.modif=1
        self.modif2=1
        self.damage_boost=1
        self.powerlift=1.0
        if j==0 :
            #            (xstam,ystam,xPV,xammo,xnammo,ynammo)
            self.stam_pos = (30,20, 100, 160, 20, HEIGH-40)
            self.right,self.left=True, False
            self.axe_x1, self.axe_y1=1, 0
            self.death=pygame.transform.rotate(self.death, -90)
        else :
            self.stam_pos = (WIDTH-80, 20, WIDTH-150, WIDTH-190, WIDTH-420, HEIGH-40)
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
        self.axe_x1=self.joy.get_axis(0)*self.modif*self.modif2*self.furb2*self.slow
        self.axe_y1=self.joy.get_axis(1)*self.modif*self.modif2*self.furb22*self.slow
        self.vec = Vector2(self.axe_x1,self.axe_y1)
        self.rad, self.angle = self.vec.as_polar() # le rad est inutile mais je veux pas ça crash
        self.ajusted_angle = (360-self.angle+self.furb) % 360
        

        
        

        
        if vibr and self.canvibr and self.ammo!=self.capa[6] and self.can:
            
            self.reloading=True
            self.time_reloading=pygame.time.get_ticks()


        #direction joueur
        self.right=bool(self.axe_x1>self.zone_morte)

        self.left=bool(self.axe_x1<-self.zone_morte)

        self.down=bool(self.axe_y1>self.zone_morte)

        self.up=bool(self.axe_y1<-self.zone_morte)

        
        #recharge stamina plus élevé si le joueur ne bouge pas
        if (not self.up and not self.down and not self.right and not self.left):
            self.ajusted_angle=None
            self.stamina_speed=4
        if lock :
            self.stamina_speed=4

        #variation de l'endurance
        if sprint and not lock and self.stamina>=20 and self.can and (self.left or self.up or self.right or self.down) and not self.reloading:
            self.stamina-=20
            self.sprinting=True
        else :
            self.sprinting=False
            if self.stamina<5000 :
                self.stamina+=self.stamina_speed
                if self.stamina>5000 :
                    self.stamina=5000
        
        if self.stamina<100 :
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
        if shoot and self.canshoot and self.ajusted_angle!=None and not self.reloading:
            if self.ammo>0 :
                self.shot_acc=[True, lock]
                self.ammo-=1
            else :
                self.joy.rumble(0.5,0.5,500)

        self.lock=bool(self.ajusted_angle!=None and lock)

            
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

        if self.reloading :
            self.joy.rumble(0.5,0.5,1)
            if pygame.time.get_ticks()-self.time_reloading>3000 :
                self.reloading=False
                self.canvibr=True
                self.ammo=self.capa[6]


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
            self.vise2=pygame.transform.rotate(self.vise, self.ajusted_angle)
            l_v=[self.vise2.get_width(), self.vise2.get_height()]
            screen.blit(self.vise2, (self.rect.x-l_v[0]/2+self.block/2,self.rect.y-l_v[1]/2+self.block/2))

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
        text_PV = font.render(str(int(self.PV)), True, "red")
        screen.blit(text_PV, (self.stam_pos[2], self.stam_pos[1]*1.8))

        #les munitions
        text_ammo = font.render(str(int(self.ammo)), True, "orange")
        screen.blit(text_ammo, (self.stam_pos[3], self.stam_pos[1]*1.8))

        #new ammo
        if self.ammo>1 :
            pygame.draw.rect(screen, "gold", (self.stam_pos[4], self.stam_pos[5], self.ammo/self.capa[6]*400, 20))
        else :
            pygame.draw.rect(screen, "orangered", (self.stam_pos[4], self.stam_pos[5], self.ammo/self.capa[6]*400, 20))
        pygame.draw.rect(screen, "ghostwhite", (self.stam_pos[4], self.stam_pos[5], 400, 20), 2)

        


