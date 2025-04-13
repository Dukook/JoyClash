import pygame
from random import randint
from Player import Player
from Bullet import Bullet, Surge, Berry, Spookie
from Account import Choice, Write



info_P1, pseudo_P1=Choice(1)
info_P2, pseudo_P2=Choice(2)
"""info_P1, pseudo_P1=["1740", "46546133468451", "True", "True", "True", "True", "True", "True", "True", "True", "True"], "Dukook"
info_P2, pseudo_P2=["1740", "46546133468451", "True", "True", "True", "True", "True", "True", "True", "True", "True"], 'DuCook'"""




pygame.init()



pers=["Hank", "Berry", "Surge", "Carroje", "Popofox", "Spookie", "Mushy", "Bubule", "UIIA"]
# "nom" : [PV, Damage, speed, bullettime&speed]
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
nb_pers=8

FPS=45
sett=[]

class Menu :
    def __init__(self, screen, change):
        #setup de base
        self.screen=screen
        self.clock=pygame.time.Clock()

        #image background + ajustement taille écran
        self.background=pygame.image.load("Images/main_menu.jpg").convert()
        self.background=pygame.transform.scale(self.background, (800,600))

        #indications menu
        self.dpad_button=pygame.image.load("Images/d-pad_button.png").convert_alpha()
        self.dpad_button=pygame.transform.scale(self.dpad_button, (50,50))
        self.dpad_button_down=pygame.transform.rotate(self.dpad_button, 180)
        self.ready=pygame.image.load("Images/ready.png").convert_alpha()
        self.ready=pygame.transform.scale(self.ready, (250,125))

        #images joy-con SL et SR
        self.bSL=pygame.image.load("Images/bSL2.png").convert_alpha()
        self.bSR=pygame.image.load("Images/bSR2.png").convert_alpha()
        self.gSL=pygame.image.load("Images/gSL2.png").convert_alpha()
        self.gSR=pygame.image.load("Images/gSR2.png").convert_alpha()

        #images perso
        self.hank=pygame.transform.scale(pygame.image.load("Images/f_Hank.png").convert_alpha(), (240,285))
        self.berry=pygame.transform.scale(pygame.image.load("Images/f_Berry.png").convert_alpha(), (240,285))
        self.surge=pygame.transform.scale(pygame.image.load("Images/f_Surge.png").convert_alpha(), (240,285))
        self.carroje=pygame.transform.scale(pygame.image.load("Images/f_Carroje.png").convert_alpha(), (240,285))
        self.popofox=pygame.transform.scale(pygame.image.load("Images/f_Popofox.png").convert_alpha(), (240,285))
        self.spookie=pygame.transform.scale(pygame.image.load("Images/f_Spookie.png").convert_alpha(), (240,285))
        self.mushy=pygame.transform.scale(pygame.image.load("Images/f_Mushy.png").convert_alpha(), (240,285))
        self.bubule=pygame.transform.scale(pygame.image.load("Images/f_bubule.png").convert_alpha(), (240,285))
        self.UIIA=pygame.transform.scale(pygame.image.load("Images/f_UIIA.png").convert_alpha(), (240,285))

        #autres images
        self.cross=pygame.transform.scale_by(pygame.image.load("Images/cross.png").convert_alpha(), 0.48)
        self.coin=pygame.transform.scale_by(pygame.image.load("Images/coin.png").convert_alpha(), 0.5)
        self.logo=pygame.transform.scale(pygame.image.load("Images/logo.png").convert_alpha(), (100, 100))
        self.SS=pygame.transform.scale_by(pygame.image.load("Images/SS.png").convert(), 3)
        self.OO=pygame.transform.scale_by(pygame.image.load("Images/OO.png").convert(), 3)
        self.CG=pygame.transform.scale_by(pygame.image.load("Images/CG.png").convert(), 3)
        self.RD=pygame.transform.scale_by(pygame.image.load("Images/RD.png").convert(), 3)

        #compte des manettes connectés
        global sett
        count = pygame.joystick.get_count()
        self.running=False
        if count >= 2 :
            self.joy1=pygame.joystick.Joystick(0)
            self.joy2=pygame.joystick.Joystick(1)
            

                
            self.running=True
            self.joy1.init()
            self.joy2.init()
            if not change :
                if sett[5] :
                    self.joy1,self.joy2=self.joy2,self.joy1
            print(f"There is {count} controllers connected")
        else :
            print(f"Need more controllers. {count} controllers connected instead of 2")
            
        #setup menu
            
        self.plan="main_menu"

        #settings de base
        if change :
            self.zone_morte, self.zone_morte2  = 30, 30
            self.son=50
            self.WIDTH, self.HEIGHT=1280, 720
            self.pick1=0
            self.pick2=1
            self.plan = "main_menu"
            self.color_ss=["white","white","yellow",]
            self.srumb=True
            self.map="RD"
            self.swap=False
        else :
            #[self.zone_morte/100, self.zone_morte2/100, self.son, self.WIDTH, self.HEIGHT, self.swap, self.pick1, self.pick2, self.map, self.srumb, self.color_ss]
            self.zone_morte, self.zone_morte2  = sett[0]*100, sett[1]*100
            self.son=sett[2]
            self.WIDTH, self.HEIGHT = sett[3], sett[4]
            self.pick1=sett[6]
            self.pick2=sett[7]
            self.color_ss=sett[10]
            self.srumb=sett[9]
            self.swap=sett[5]
            self.map=sett[8]

        
        
        self.canback1, self.canback2, self.cannext1, self.cannext2, self.canchange_map, self.cansettings, self.canrumb, self.canplay1, self.canplay2=False, False, False, False, False, False, False, False, False#bcp de can
        

        #sons
        
        pygame.mixer.music.load("Songs/loby.mp3")
        pygame.mixer.music.set_volume(self.son/100)
        pygame.mixer.music.play()



        

    def event(self) :

        
        settings=self.joy1.get_button(6)

        if self.plan=="settings" :

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE :
                        self.joy1,self.joy2=self.joy2,self.joy1
                        self.swap= not self.swap


            low=self.joy1.get_button(0)
            mid=self.joy1.get_button(1)
            high=self.joy1.get_button(3)
            rumb=self.joy1.get_button(2)
            axe1=self.joy1.get_axis(0)
            axe2=self.joy2.get_axis(0)
            axe3=-self.joy1.get_axis(1)

            if abs(axe1)>self.zone_morte/100 :
                self.zone_morte+=axe1
                if self.zone_morte<1 :
                    self.zone_morte=1
                elif self.zone_morte>80 :
                    self.zone_morte=80

            if abs(axe2)>self.zone_morte2/100 :
                self.zone_morte2+=axe2
                if self.zone_morte2<1 :
                    self.zone_morte2=1
                elif self.zone_morte2>80 :
                    self.zone_morte2=80

            if abs(axe3)>0.2 :
                self.son+=axe3*3
                if self.son<0 :
                    self.son=0
                elif self.son>100 :
                    self.son=100
                pygame.mixer.music.set_volume(self.son/100)

            if low :
                self.WIDTH,self.HEIGHT = 1280, 720
                self.color_ss=["white","white","yellow"]
            
            if mid :
                self.WIDTH,self.HEIGHT = 1920, 1080
                self.color_ss=["white","yellow","white",]

            if high :
                self.WIDTH,self.HEIGHT = 2550, 1440
                self.color_ss=["yellow","white","white",]

            if rumb and self.canrumb:
                self.srumb=not self.srumb
                self.canrumb=False
                if self.srumb :
                    self.joy1.rumble(10,10,300)
                    self.joy2.rumble(10,10,300)
            elif not rumb :
                self.canrumb=True

            if settings and self.cansettings :
                self.plan="main_menu"
                self.cansettings=False
            elif not settings :
                self.cansettings=True

            

        elif self.plan == "main_menu" :

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False


            self.play1 = self.joy1.get_button(3)
            self.play2 = self.joy2.get_button(3)
            next1=self.joy1.get_button(5)
            next2=self.joy2.get_button(5)
            back1=self.joy1.get_button(4)
            back2=self.joy2.get_button(4)
            self.purchase1=self.joy1.get_button(1)
            self.purchase2=self.joy2.get_button(1)
            change_map=self.joy1.get_button(0)
            UIIA=pygame.key.get_pressed()
            if UIIA[pygame.K_u] and UIIA[pygame.K_i] and UIIA[pygame.K_a] and UIIA[pygame.K_SPACE] :
                global nb_pers
                nb_pers=9

            if self.srumb :
                vibr=self.joy1.get_button(2)
                vibr2=self.joy2.get_button(2)

                if vibr :
                    self.joy1.rumble(1,1,1)

                if vibr2 :
                    self.joy2.rumble(1,1,1)

            if self.purchase1 or self.play1 :
                pass
            else :

                if next1 and self.cannext1 :
                    self.pick1+=1
                    self.cannext1=False
                    
                    if self.pick1==self.pick2 :
                        self.pick1+=1
                    if self.pick1>=nb_pers :
                        self.pick1=0
                        if self.pick1==self.pick2 :
                            self.pick1+=1
                    
                elif not next1 :
                    self.cannext1=True
                
                if back1 and self.canback1:
                    self.pick1-=1
                    self.canback1=False
                    if self.pick1<0 :
                        self.pick1=nb_pers-1
                    if self.pick1==self.pick2 :
                        self.pick1-=1
                        if self.pick1<0 :
                            self.pick1=nb_pers-1
                elif not back1 :
                    self.canback1=True

                if settings and self.cansettings:
                    self.plan="settings"
                    self.cansettings=False
                elif not settings :
                    self.cansettings=True

                if change_map and self.canchange_map:
                    self.canchange_map=False
                    if self.map=="SS" :
                        self.map="OO"
                    elif self.map=="OO" :
                        self.map="CG"
                    elif self.map=="CG" :
                        self.map="RD"
                    else :
                        self.map="SS"
                elif not change_map :
                    self.canchange_map=True

            if self.purchase2 or self.play2 :
                pass
            else :

                if next2 and self.cannext2 :
                    self.pick2+=1
                    self.cannext2=False
                    if self.pick2>=nb_pers :
                        self.pick2=0
                    if self.pick1==self.pick2 :
                        self.pick2+=1
                        if self.pick2>=nb_pers :
                            self.pick2=0
                    
                elif not next2 :
                    self.cannext2=True

                if back2 and self.canback2:
                    self.pick2-=1
                    self.canback2=False
                    if self.pick2<0 :
                        self.pick2=nb_pers-1
                    if self.pick1==self.pick2 :
                        self.pick2-=1
                        if self.pick2<0 :
                            self.pick2=nb_pers-1
                    
                elif not back2 :
                    self.canback2=True

            if self.play1 and self.play2 and self.canplay1 and self.canplay2:
                self.running=False
                global play, sett
                play=True
                self.joy1.quit()
                self.joy2.quit()
                sett=[self.zone_morte/100, self.zone_morte2/100, self.son, self.WIDTH, self.HEIGHT, self.swap, self.pick1, self.pick2, self.map, self.srumb, self.color_ss]
                return

            


    def update(self):
        if not pygame.mixer.music.get_busy() :
            pygame.mixer.music.play()
        if self.plan=="main_menu" :
            if self.canback1 :    
                self.len_bSL=(46,46)
            else :
                self.len_bSL=(38,38)
            if self.canback2 :    
                self.len_gSL=(46,46)
            else :
                self.len_gSL=(38,38)
            if self.cannext1 :    
                self.len_bSR=(46,46)
            else :
                self.len_bSR=(38,38)
            if self.cannext2 :    
                self.len_gSR=(46,46)
            else :
                self.len_gSR=(38,38)

            
            actual_pick=(self.pick1+2)%nb_pers
            global info_P1, pseudo_P1
            #print(info_P1, self.canplay1)
            if info_P1==None :
                if actual_pick==2 or actual_pick==3 or actual_pick==4 :
                    self.canplay1=True
                else :
                    self.canplay1=False
            elif info_P1[actual_pick]=="False" :
                self.canplay1=False
                if self.purchase1 and int(info_P1[1])>=10:
                    info_P1, pseudo_P1=Write(pseudo_P1, actual_pick, -10)
            else :
                self.canplay1=True

            actual_pick2=(self.pick2+2)%nb_pers
            global info_P2, pseudo_P2
            #print(info_P2, self.canplay2)
            if info_P2==None :
                if actual_pick2==2 or actual_pick2==3 or actual_pick2==4 :
                    self.canplay2=True
                else :
                    self.canplay2=False
            elif info_P2[actual_pick2]=="False" :
                self.canplay2=False
                if self.purchase2 and int(info_P2[1])>=10:
                    info_P2, pseudo_P2=Write(pseudo_P2, actual_pick2, -10)
            else :
                self.canplay2=True

            #map
            if self.map=="SS" :
                self.map_color=["yellow", "white", "white", "white"]
                self.map_pos=(715, 80)

            elif self.map=="OO" :
                self.map_color=["white", "yellow", "white", "white"]
                self.map_pos=(40, 410)
            elif self.map=="CG" :
                self.map_color=["white", "white", "yellow", "white"]
                self.map_pos=(715, 410)
            else :
                self.map_color=["white", "white", "white", "yellow"]
                self.map_pos=(40, 80)
            

            


    def display(self) :
        self.screen.fill("black")
        if self.plan=="settings" :
            text = font.render("Settings", True, "gray")
            self.screen.blit(text, (360, 20))
            #P1
            pygame.draw.circle(self.screen, (0,0,40), (200, 300), 100)
            pygame.draw.circle(self.screen, (10, 185, 239), (200, 300), 100, 5)
            pygame.draw.circle(self.screen, (252, 23, 35), (200, 300), self.zone_morte)
            pygame.draw.rect(self.screen, (252, 23, 35), (78, 135, self.zone_morte*3,20))
            textP1 = font.render("Dead zone P1", True, (10, 185, 239))
            self.screen.blit(textP1, (130, 80))
            #P2
            pygame.draw.circle(self.screen, (0,0,40), (600, 300), 100)
            pygame.draw.circle(self.screen, (30, 220, 0), (600, 300), 100, 5)
            pygame.draw.circle(self.screen, (252, 23, 35), (600, 300), self.zone_morte2)
            pygame.draw.rect(self.screen, (252, 23, 35), (480, 135, self.zone_morte2*3,20))
            textP2 = font.render("Dead zone P2", True, (30, 220, 0))
            self.screen.blit(textP2, (540, 80))
            #son
            pygame.draw.rect(self.screen, "purple", (390, 405-self.son*2.8, 20, self.son*2.8))
            text_son = font.render("Volume", True, "purple")
            self.screen.blit(text_son, (368, 80))
            #écritures et résolutions
            text_size = font.render("Screen size :", True, "yellow")
            self.screen.blit(text_size, (70, 440))
            self.screen.blit(self.dpad_button, (225, 435))
            self.screen.blit(pygame.transform.rotate(self.dpad_button, -90), (270, 480))
            
            self.screen.blit(pygame.transform.rotate(self.dpad_button, 180), (225, 525))
            text_high = font.render("2560/1440", True, self.color_ss[0])
            self.screen.blit(text_high, (300, 445))
            text_mid = font.render("1920/1080", True, self.color_ss[1])
            self.screen.blit(text_mid, (335, 495))
            text_low = font.render("1280/720", True, self.color_ss[2])
            self.screen.blit(text_low, (300, 545))
            #vibrations
            if self.srumb :
                text_vibr=font.render("Rumble", True, "yellow")
            else :
                text_vibr=font.render("Rumble", True, "white")
            self.screen.blit(text_vibr, (575, 490))
            self.screen.blit(pygame.transform.rotate(self.dpad_button, 90), (500, 480))


        elif self.plan=="main_menu" :
            self.screen.blit(self.background, (0,0))
            self.screen.blit(self.dpad_button, (375,510))
            #blue gachette SL
            self.bSL2=pygame.transform.scale(self.bSL, self.len_bSL)
            self.screen.blit(self.bSL2, (150-self.len_bSL[0]//2,96-self.len_bSL[1]//2))
            #green gachette SL
            self.gSL2=pygame.transform.scale(self.gSL, self.len_gSL)
            self.screen.blit(self.gSL2, (440-self.len_gSL[0]//2,96-self.len_gSL[1]//2))
            #blue gachette SR
            self.bSR2=pygame.transform.scale(self.bSR, self.len_bSR)
            self.screen.blit(self.bSR2, (360-self.len_bSR[0]//2,96-self.len_bSR[1]//2))
            #green gachette SR
            self.gSR2=pygame.transform.scale(self.gSR, self.len_gSR)
            self.screen.blit(self.gSR2, (650-self.len_gSR[0]//2,96-self.len_gSR[1]//2))

            #perso P1
            if pers[self.pick1]=="Hank":
                self.screen.blit(self.hank, (136, 133))
            elif pers[self.pick1]=="Berry":
                self.screen.blit(self.berry, (136, 133))
            elif pers[self.pick1]=="Surge":
                self.screen.blit(self.surge, (136, 133))
            elif pers[self.pick1]=="Carroje":
                self.screen.blit(self.carroje, (136, 133))
            elif pers[self.pick1]=="Popofox":
                self.screen.blit(self.popofox, (136, 133))
            elif pers[self.pick1]=="Spookie":
                self.screen.blit(self.spookie, (136, 133))
            elif pers[self.pick1]=="Mushy":
                self.screen.blit(self.mushy, (136, 133))
            elif pers[self.pick1]=="Bubule":
                self.screen.blit(self.bubule, (136, 133))
            elif pers[self.pick1]=="UIIA":
                self.screen.blit(self.UIIA, (136, 133))

            #perso 2 (x+290)    
            if pers[self.pick2]=="Hank":
                self.screen.blit(self.hank, (426, 133))
            elif pers[self.pick2]=="Berry":
                self.screen.blit(self.berry, (426, 133))
            elif pers[self.pick2]=="Surge":
                self.screen.blit(self.surge, (426, 133))
            elif pers[self.pick2]=="Carroje":
                self.screen.blit(self.carroje, (426, 133))
            elif pers[self.pick2]=="Popofox":
                self.screen.blit(self.popofox, (426, 133))
            elif pers[self.pick2]=="Spookie":
                self.screen.blit(self.spookie, (426, 133))
            elif pers[self.pick2]=="Mushy":
                self.screen.blit(self.mushy, (426, 133))
            elif pers[self.pick2]=="Bubule":
                self.screen.blit(self.bubule, (426, 133))
            elif pers[self.pick2]=="UIIA":
                self.screen.blit(self.UIIA, (426, 133))

            #perso non débloqués
            if not self.canplay1 :
                self.screen.blit(self.cross, (111,140))

            if not self.canplay2 :
                self.screen.blit(self.cross, (401,140))

            #coin
            self.screen.blit(self.coin, (10,480))
            if info_P1!=None :
                if int(info_P1[1])>10000 :
                    self.screen.blit(font.render("∞", True, "yellow"), (140, 540))
                else :
                    self.screen.blit(font.render(info_P1[1], True, "yellow"), (140, 540))

            self.screen.blit(self.coin, (690,480))
            if info_P2!=None :
                if int(info_P1[1])>10000 :
                    self.screen.blit(font.render("∞", True, "yellow"), (660, 540))
                else :
                    decal_coin=font.render(info_P2[1], True, "yellow")
                    self.screen.blit(decal_coin, (670-decal_coin.get_width(), 540))

            #perso actif
            decal_p1=font.render(pers[self.pick1], True, (10, 185, 239))
            self.screen.blit(decal_p1, (255-decal_p1.get_width()/2, 80))
            decal_p2=font.render(pers[self.pick2], True, (30, 220, 0))
            self.screen.blit(decal_p2, (545-decal_p2.get_width()/2, 80))

            #player name
            if info_P1!=None :
                self.screen.blit(font.render(pseudo_P1, True, (10, 185, 239)), (10, 10))
            else :
                self.screen.blit(font.render("Guest", True, (10, 185, 239)), (10, 10))
            if info_P2!=None :
                decal_namep2=font.render(pseudo_P2, True, (30, 220, 0))
                self.screen.blit(decal_namep2, (790-decal_namep2.get_width(), 10))
            else :
                self.screen.blit(font.render("Guest", True, (30, 220, 0)), (730, 10))

            #indic ready
            if self.play1 and self.canplay1:
                self.screen.blit(self.ready, (60, 370))
            if self.play2 and self.canplay2:
                self.screen.blit(self.ready, (490, 370))

            #logo
            self.screen.blit(self.logo, (350, -10))

            #map
            self.screen.blit(self.dpad_button_down, self.map_pos)
            self.screen.blit(self.SS, (12, 200))
            self.screen.blit(self.OO, (686, 200))
            self.screen.blit(self.CG, (12, 280))
            self.screen.blit(self.RD, (686, 280))
            self.screen.blit(font.render("Shooting", True, self.map_color[0]), (24, 140))
            self.screen.blit(font.render("Stars", True, self.map_color[0]), (38, 170))
            self.screen.blit(font.render("Out in", True, self.map_color[1]), (710, 140))
            self.screen.blit(font.render("the Open", True, self.map_color[1]), (698, 170))
            self.screen.blit(font.render("Canal", True, self.map_color[2]), (35, 350))
            self.screen.blit(font.render("Grande", True, self.map_color[2]), (30, 380))
            self.screen.blit(font.render("Random", True, self.map_color[3]), (704, 350))
            self.screen.blit(font.render("map", True, self.map_color[3]), (718, 380))
            

        pygame.display.flip()
        

    def run(self) :
        while self.running :
            self.event()
            self.update()
            self.display()
            self.clock.tick(FPS)







class Game :
    
    def __init__(self, screen):
        global sett
        self.rumb=sett[9]
        self.pers=pers[sett[6]]
        self.capa=capa[self.pers]
        self.pers2=pers[sett[7]]
        self.capa2=capa[self.pers2]
        self.map=sett[8]
        if self.map=="RD" :
            rand=randint(0,2)
            if rand==0:
                self.map="SS"
            elif rand==1 :
                self.map="OO"
            else :
                self.map="CG"
        #def d'un block
        self.block=WIDTH/32
        # écran + rafraichissement
        self.screen = screen
        self.clock=pygame.time.Clock()
        #importation joueur et manettes
        
        if sett[5] :
            j=[1,0]
        else :
            j=[0,1]
        self.player=Player(1*self.block, 9*self.block, self.pers, sett[0], WIDTH, HEIGHT, 0, self.block, j[0])
        self.player2=Player(30*self.block, 9*self.block, self.pers2, sett[1], WIDTH, HEIGHT, 1, self.block, j[1])
        self.plan="start"

        #potions
        self.p_pos=[(16*self.block-self.block/2, 9*self.block-self.block/2), (20*self.block, 1*self.block), (11*self.block, 16*self.block), (20*self.block, 16*self.block), (11*self.block, 1*self.block), (19*self.block, 10*self.block), (12*self.block, 7*self.block)]
        self.p_speed=pygame.transform.scale(pygame.image.load("Images/p_speed.png").convert_alpha(), (self.block, self.block))
        self.p_damage=pygame.transform.scale(pygame.image.load("Images/p_damage.png").convert_alpha(), (self.block, self.block))
        self.p_heal=pygame.transform.scale(pygame.image.load("Images/p_heal.png").convert_alpha(), (self.block, self.block))
        self.spawn=pygame.transform.scale(pygame.image.load("Images/spawn.png").convert_alpha(), (2*self.block, 2*self.block))
        self.p_all=[(self.p_speed, "speed"), (self.p_damage, "damage"), (self.p_heal, "heal")]
        self.p_on_stage=[False,pygame.time.get_ticks()+randint(6000, 8000)]
        self.p_how_long=-5000

        #création mur
        self.murs=[]
        self.waters=[]
        self.bushs=[]

        if self.map=="SS" :
            self.murs.append(pygame.Rect(4*self.block,2*self.block, 1*self.block, 4*self.block))
            self.murs.append(pygame.Rect(8*self.block, 0*self.block, 2*self.block, 4*self.block))
            self.murs.append(pygame.Rect(3*self.block,15*self.block, 2*self.block, 3*self.block))
            self.murs.append(pygame.Rect(6*self.block, 12*self.block, 2*self.block, 2*self.block))
            self.murs.append(pygame.Rect(13*self.block, 9*self.block, 1*self.block, 3*self.block))
            self.murs.append(pygame.Rect(18*self.block,6*self.block, 1*self.block, 3*self.block))
            self.murs.append(pygame.Rect(22*self.block, 14*self.block, 2*self.block, 4*self.block))
            self.murs.append(pygame.Rect(24*self.block,4*self.block, 2*self.block, 2*self.block))
            self.murs.append(pygame.Rect(27*self.block, 12*self.block, 1*self.block, 4*self.block))
            self.murs.append(pygame.Rect(27*self.block, 0*self.block, 2*self.block, 3*self.block))

            self.waters.append(pygame.Rect(11*self.block,11*self.block, 2*self.block, 2*self.block))
            self.waters.append(pygame.Rect(19*self.block,5*self.block, 2*self.block, 2*self.block))

            """self.bushs.append(pygame.Rect(2*self.block,4*self.block, 2*self.block, 2*self.block))
            self.bushs.append(pygame.Rect(6*self.block,10*self.block, 2*self.block, 2*self.block))
            self.bushs.append(pygame.Rect(8*self.block,4*self.block, 2*self.block, 2*self.block))
            self.bushs.append(pygame.Rect(24*self.block,6*self.block, 2*self.block, 2*self.block))
            self.bushs.append(pygame.Rect(22*self.block,12*self.block, 2*self.block, 2*self.block))
            self.bushs.append(pygame.Rect(28*self.block,14*self.block, 2*self.block, 2*self.block))
            self.bushs.append(pygame.Rect(11*self.block,10*self.block, 2*self.block, 1*self.block))
            self.bushs.append(pygame.Rect(11*self.block,13*self.block, 2*self.block, 1*self.block))
            self.bushs.append(pygame.Rect(19*self.block,4*self.block, 2*self.block, 1*self.block))
            self.bushs.append(pygame.Rect(19*self.block,7*self.block, 2*self.block, 1*self.block))"""

            self.p_pos.append((6*self.block, 5*self.block))
            self.p_pos.append((25*self.block, 12*self.block))

        elif self.map=="OO" :
            #beacoup de mur lol
            self.murs.append(pygame.Rect(2*self.block,3*self.block, 2*self.block, 1*self.block))
            self.murs.append(pygame.Rect(3*self.block,7*self.block, 2*self.block, 4*self.block))
            self.murs.append(pygame.Rect(3*self.block,14*self.block, 1*self.block, 2*self.block))
            self.murs.append(pygame.Rect(7*self.block,0*self.block, 2*self.block, 2*self.block))
            self.murs.append(pygame.Rect(7*self.block,6*self.block, 2*self.block, 5*self.block))
            self.murs.append(pygame.Rect(7*self.block,13*self.block, 1*self.block, 2*self.block))
            self.murs.append(pygame.Rect(11*self.block,10*self.block, 1*self.block, 1*self.block))
            self.murs.append(pygame.Rect(13*self.block,5*self.block, 2*self.block, 1*self.block))
            self.murs.append(pygame.Rect(17*self.block,12*self.block, 2*self.block, 1*self.block))
            self.murs.append(pygame.Rect(20*self.block,7*self.block, 1*self.block, 1*self.block))
            self.murs.append(pygame.Rect(24*self.block,3*self.block, 1*self.block, 2*self.block))
            self.murs.append(pygame.Rect(23*self.block,7*self.block, 2*self.block, 5*self.block))
            self.murs.append(pygame.Rect(23*self.block,16*self.block, 2*self.block, 2*self.block))
            self.murs.append(pygame.Rect(28*self.block,2*self.block, 1*self.block, 2*self.block))
            self.murs.append(pygame.Rect(27*self.block,7*self.block, 2*self.block, 4*self.block))
            self.murs.append(pygame.Rect(28*self.block,14*self.block, 2*self.block, 1*self.block))

            self.waters.append(pygame.Rect(7*self.block,2*self.block, 2*self.block, 4*self.block))
            self.waters.append(pygame.Rect(23*self.block,12*self.block, 2*self.block, 4*self.block))

            """self.bushs.append(pygame.Rect(9*self.block,5*self.block, 2*self.block, 7*self.block))
            self.bushs.append(pygame.Rect(21*self.block,6*self.block, 2*self.block, 7*self.block))
            self.bushs.append(pygame.Rect(7*self.block,11*self.block, 2*self.block, 1*self.block))
            self.bushs.append(pygame.Rect(23*self.block,6*self.block, 2*self.block, 1*self.block))
            self.bushs.append(pygame.Rect(2*self.block,16*self.block, 7*self.block, 2*self.block))
            self.bushs.append(pygame.Rect(17*self.block,13*self.block, 2*self.block, 2*self.block))
            self.bushs.append(pygame.Rect(23*self.block,0*self.block, 7*self.block, 2*self.block))
            self.bushs.append(pygame.Rect(13*self.block,3*self.block, 2*self.block, 2*self.block))"""

            self.p_pos.append((5*self.block, 4*self.block))
            self.p_pos.append((26*self.block, 13*self.block))

        else :
            #encore plus de murs
            self.murs.append(pygame.Rect(3*self.block,5*self.block, 3*self.block, 1*self.block))
            self.murs.append(pygame.Rect(5*self.block,6*self.block, 1*self.block, 2*self.block))
            self.murs.append(pygame.Rect(5*self.block,10*self.block, 1*self.block, 2*self.block))
            self.murs.append(pygame.Rect(2*self.block,14*self.block, 1*self.block, 1*self.block))
            self.murs.append(pygame.Rect(5*self.block,14*self.block, 1*self.block, 1*self.block))
            self.murs.append(pygame.Rect(8*self.block,12*self.block, 1*self.block, 2*self.block))
            self.murs.append(pygame.Rect(9*self.block,5*self.block, 3*self.block, 1*self.block))
            self.murs.append(pygame.Rect(10*self.block,4*self.block, 1*self.block, 1*self.block))
            self.murs.append(pygame.Rect(13*self.block,0*self.block, 1*self.block, 2*self.block))
            self.murs.append(pygame.Rect(13*self.block,12*self.block, 1*self.block, 2*self.block))
            self.murs.append(pygame.Rect(13*self.block,16*self.block, 1*self.block, 2*self.block))
            self.murs.append(pygame.Rect(15*self.block,2*self.block, 1*self.block, 1*self.block))
            self.murs.append(pygame.Rect(16*self.block,3*self.block, 1*self.block, 2*self.block))
            self.murs.append(pygame.Rect(15*self.block,13*self.block, 1*self.block, 2*self.block))
            self.murs.append(pygame.Rect(16*self.block,15*self.block, 1*self.block, 1*self.block))
            self.murs.append(pygame.Rect(18*self.block,0*self.block, 1*self.block, 2*self.block))
            self.murs.append(pygame.Rect(18*self.block,4*self.block, 1*self.block, 2*self.block))
            self.murs.append(pygame.Rect(18*self.block,16*self.block, 1*self.block, 2*self.block))
            self.murs.append(pygame.Rect(23*self.block,4*self.block, 1*self.block, 2*self.block))
            self.murs.append(pygame.Rect(20*self.block,12*self.block, 3*self.block, 1*self.block))
            self.murs.append(pygame.Rect(21*self.block,13*self.block, 1*self.block, 1*self.block))
            self.murs.append(pygame.Rect(26*self.block,3*self.block, 1*self.block, 1*self.block))
            self.murs.append(pygame.Rect(29*self.block,3*self.block, 1*self.block, 1*self.block))
            self.murs.append(pygame.Rect(26*self.block,6*self.block, 1*self.block, 2*self.block))
            self.murs.append(pygame.Rect(26*self.block,10*self.block, 1*self.block, 3*self.block))
            self.murs.append(pygame.Rect(27*self.block,12*self.block, 2*self.block, 1*self.block))

            self.waters.append(pygame.Rect(3*self.block,6*self.block, 2*self.block, 6*self.block))
            self.waters.append(pygame.Rect(5*self.block,8*self.block, 10*self.block, 2*self.block))
            self.waters.append(pygame.Rect(3*self.block,14*self.block, 2*self.block, 1*self.block))
            self.waters.append(pygame.Rect(3*self.block,15*self.block, 3*self.block, 3*self.block))
            self.waters.append(pygame.Rect(17*self.block,8*self.block, 10*self.block, 2*self.block))
            self.waters.append(pygame.Rect(27*self.block,6*self.block, 2*self.block, 6*self.block))
            self.waters.append(pygame.Rect(26*self.block,0*self.block, 3*self.block, 3*self.block))
            self.waters.append(pygame.Rect(27*self.block,3*self.block, 2*self.block, 1*self.block))

            """self.bushs.append(pygame.Rect(8*self.block,2*self.block, 2*self.block, 3*self.block))
            self.bushs.append(pygame.Rect(6*self.block,6*self.block, 1*self.block, 1*self.block))
            self.bushs.append(pygame.Rect(5*self.block, 7*self.block, 3*self.block, 1*self.block))
            self.bushs.append(pygame.Rect(8*self.block,12*self.block, 2*self.block, 3*self.block))
            self.bushs.append(pygame.Rect(14*self.block,0*self.block, 4*self.block, 6*self.block))
            self.bushs.append(pygame.Rect(15*self.block,6*self.block, 2*self.block, 1*self.block))
            self.bushs.append(pygame.Rect(14*self.block,7*self.block, 4*self.block, 1*self.block))
            self.bushs.append(pygame.Rect(14*self.block,10*self.block, 4*self.block, 1*self.block))
            self.bushs.append(pygame.Rect(15*self.block,11*self.block, 2*self.block, 1*self.block))
            self.bushs.append(pygame.Rect(14*self.block, 12*self.block, 4*self.block, 6*self.block))
            self.bushs.append(pygame.Rect(22*self.block,3*self.block, 2*self.block, 3*self.block))
            self.bushs.append(pygame.Rect(23*self.block,10*self.block, 3*self.block, 2*self.block))
            self.bushs.append(pygame.Rect(25*self.block,11*self.block, 1*self.block, 1*self.block))
            self.bushs.append(pygame.Rect(22*self.block,13*self.block, 2*self.block, 3*self.block))"""

            self.p_pos.append((20*self.block, 6*self.block))
            self.p_pos.append((11*self.block, 11*self.block))

        self.SS=pygame.transform.scale(pygame.image.load("Images/t_SS.png").convert_alpha(), (WIDTH, HEIGHT))
        self.OO=pygame.transform.scale(pygame.image.load("Images/t_OO.png").convert_alpha(), (WIDTH, HEIGHT))
        self.CG=pygame.transform.scale(pygame.image.load("Images/t_CG.png").convert_alpha(), (WIDTH, HEIGHT))
        self.background=pygame.transform.scale(pygame.image.load("Images/background.png").convert_alpha(), (WIDTH, HEIGHT))

        #autres
        self.running=True
        self.shooting=[False, None, True]
        self.shooting2=[False, None, True]
        self.diff_ticks=750
        self.damage_boost=1.0
        self.p_duration=-10000
        self.time_surge=-200
        self.time_poison=-5000
        self.time_spookie=-5000
        self.time_UIIA=-5000
        self.mort=0
        self.mort_exp=0.000001
        self.canshot=True
        self.canshot2=True
        self.emt=False
        self.emt2=False
        

        #importation du song
        self.son=sett[2]/100
        pygame.mixer.music.stop()
        pygame.mixer.music.load("Songs/321.mp3")
        pygame.mixer.music.set_volume(self.son)
        pygame.mixer.music.play()

        #pers
        self.hank=pygame.transform.scale(pygame.image.load("Images/f_Hank.png").convert_alpha(), (240,285))
        self.berry=pygame.transform.scale(pygame.image.load("Images/f_Berry.png").convert_alpha(), (240,285))
        self.surge=pygame.transform.scale(pygame.image.load("Images/f_Surge.png").convert_alpha(), (240,285))
        self.carroje=pygame.transform.scale(pygame.image.load("Images/f_Carroje.png").convert_alpha(), (240,285))
        self.popofox=pygame.transform.scale(pygame.image.load("Images/f_Popofox.png").convert_alpha(), (240,285))
        self.spookie=pygame.transform.scale(pygame.image.load("Images/f_Spookie.png").convert_alpha(), (240,285))
        self.mushy=pygame.transform.scale(pygame.image.load("Images/f_Mushy.png").convert_alpha(), (240,285))
        self.bubule=pygame.transform.scale(pygame.image.load("Images/f_Bubule.png").convert_alpha(), (240,285))
        self.UIIA=pygame.transform.scale(pygame.image.load("Images/f_UIIA.png").convert_alpha(), (240,285))

        self.down=pygame.transform.scale(pygame.image.load("Images/down.png").convert_alpha(), (self.block/2,self.block/2))



        if self.pers=="Hank" :
            self.draw=self.hank
        elif self.pers=="Berry" :
            self.draw=self.berry
        elif self.pers=="Surge" :
            self.draw=self.surge
        elif self.pers=="Carroje" :
            self.draw=self.carroje
        elif self.pers=="Popofox" :
            self.draw=self.popofox
        elif self.pers=="Spookie" :
            self.draw=self.spookie
        elif self.pers=="Mushy" :
            self.draw=self.mushy
        elif self.pers=="Bubule" :
            self.draw=self.bubule
        elif self.pers=="UIIA" :
            self.draw=self.UIIA


        if self.pers2=="Hank" :
            self.draw2=self.hank
        elif self.pers2=="Berry" :
            self.draw2=self.berry
        elif self.pers2=="Surge" :
            self.draw2=self.surge
        elif self.pers2=="Carroje" :
            self.draw2=self.carroje
        elif self.pers2=="Popofox" :
            self.draw2=self.popofox
        elif self.pers2=="Spookie" :
            self.draw2=self.spookie
        elif self.pers2=="Mushy" :
            self.draw2=self.mushy
        elif self.pers2=="Bubule" :
            self.draw2=self.bubule
        elif self.pers2=="UIIA" :
            self.draw2=self.UIIA
        

        self.light=pygame.transform.rotozoom(pygame.image.load("Images/light.png").convert_alpha(), 5, 2)
        self.light2=pygame.transform.rotozoom(pygame.image.load("Images/light.png").convert_alpha(), -5, 2)
        self.c_1=pygame.transform.scale(pygame.image.load("Images/1.png").convert_alpha(), (6*self.block, 4*self.block))
        self.c_2=pygame.transform.scale(pygame.image.load("Images/2.png").convert_alpha(), (6*self.block, 4*self.block))
        self.c_3=pygame.transform.scale(pygame.image.load("Images/3.png").convert_alpha(), (6*self.block, 4*self.block))

        #init bullet
        self.bullet=Bullet(self.pers, self.block, self.capa[3])
        self.bullet2=Bullet(self.pers2, self.block, self.capa2[3])
        
    
    def event(self) :

        self.ticks=pygame.time.get_ticks()
        global running
        
        pause=bool(self.player.joy.get_button(6) and self.player2.joy.get_button(6))

        if self.plan == "start" :
            for x in range(3) :
                self.screen.fill('black')
                if x==0 :
                    self.screen.blit(self.c_3, (WIDTH/2-3*self.block, HEIGHT/2-2*self.block))
                elif x==1 :
                    self.screen.blit(self.c_2, (WIDTH/2-3*self.block, HEIGHT/2-2*self.block))
                else :
                    self.screen.blit(self.c_1, (WIDTH/2-3*self.block, HEIGHT/2-2*self.block))
                pygame.display.flip()
                self.clock.tick(1)
                
            self.plan="play"
            pygame.mixer.music.load("Songs/Trophy.mp3")
            pygame.mixer.music.play()

        elif self.plan == "play" :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    running=False

            self.player.event()
            self.player2.event()

            self.emt=self.player.joy.get_button(3)
            self.emt2=self.player2.joy.get_button(3)
            if self.player.shot_acc[0] :
                self.player.canshoot = False
                self.canshot=False
                self.canhit=True
                self.bullet.settings(self.player.rect.x, self.player.rect.y, self.player.ajusted_angle, self.player.shot_acc[1])
                self.player.shot_acc=[False, False]
                self.shooting=[True, self.ticks, True]
                if self.pers=="Spookie" :
                    self.a_spookie=Spookie(self.player.rect.x, self.player.rect.y, self.block)
                    self.time_spookie=self.ticks
                    if self.player2.rect.colliderect(self.a_spookie):
                        self.player2.PV-=self.capa[1]*self.damage_boost*1.2
                        self.player2.i_death=3*self.block
                        if self.rumb :
                            self.player2.joy.rumble(1,1,1000)

            if self.player2.shot_acc[0] :
                self.player2.canshoot = False
                self.canshot2=False
                self.canhit2=True
                self.bullet2.settings(self.player2.rect.x, self.player2.rect.y, self.player2.ajusted_angle, self.player2.shot_acc[1])
                self.player2.shot_acc=[False, False]
                self.shooting2=[True, self.ticks, True]
                if self.pers2=="Spookie" :
                    self.a_spookie=Spookie(self.player2.rect.x, self.player2.rect.y, self.block)
                    self.time_spookie=self.ticks
                    if self.player.rect.colliderect(self.a_spookie):
                        self.player.PV-=self.capa2[1]*self.damage_boost2*1.2
                        self.player.i_death=3*self.block
                        if self.rumb :
                            self.player.joy.rumble(1,1,1000)

            if pause and self.canpause:
                self.plan="pause"
                self.plan_return=False
                self.plan_pause=True
                self.canpause=False
            elif not pause :
                self.canpause=True

        elif self.plan=="pause" :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    running=False

            if pause and self.canpause:
                self.plan_return=True
                self.canpause=False
            elif not pause :
                self.canpause=True

        elif self.plan=="end" :
            stop=False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    running=False
                elif event.type == pygame.KEYDOWN :
                    if event.key==pygame.K_SPACE :
                        stop=True

            stop2=bool(self.player.joy.get_button(6) or self.player2.joy.get_button(6))
            if self.running ==True :
                self.running=not bool(stop or stop2)
                


            
        
    def update(self) :
        
        
        
        if self.plan == "play" :

            

            #over time
            self.mort+=1

            if self.mort>1800 :
                self.mort_exp+=0.0000005
                self.player.PV-=self.mort_exp*self.capa[0]
                self.player2.PV-=self.mort_exp*self.capa2[0]

            #potion
            if self.p_on_stage[1]<self.ticks and not self.p_on_stage[0]:
                self.p_on_stage[0]=True
                self.p_how_long=self.ticks
                self.p_pos_on_stage=self.p_pos[randint(0,len(self.p_pos)-1)]
                self.p_which=self.p_all[randint(0,2)]
                self.p_rect=self.p_which[0]
                self.p_rect=self.p_rect.get_rect(x=self.p_pos_on_stage[0], y=self.p_pos_on_stage[1])
            if self.p_on_stage[0] and self.p_how_long+4000<self.ticks :
                if self.player.rect.colliderect(self.p_rect) :
                    if self.p_which[1]=="heal" :
                        self.player.PV+=300
                    elif self.p_which[1]=="speed" :
                        self.player.base_speed*=1.5
                        self.p_duration=self.ticks
                    elif self.p_which[1]=="damage" :
                        self.damage_boost=1.25
                        self.p_duration=self.ticks
                    self.p_on_stage=[False,self.ticks+randint(6000, 8000)]
                if self.player2.rect.colliderect(self.p_rect) :
                    if self.p_which[1]=="heal" :
                        self.player2.PV+=300
                    elif self.p_which[1]=="speed" :
                        self.player2.base_speed*=1.3
                        self.p_duration=self.ticks
                    elif self.p_which[1]=="damage" :
                        self.damage_boost2=1.25
                        self.p_duration=self.ticks
                    self.p_on_stage=[False,self.ticks+randint(6000, 8000)]


            if self.p_duration+5000<self.ticks :
                self.damage_boost=1.0
                self.player.base_speed=self.capa[2]
                self.damage_boost2=1.0
                self.player2.base_speed=self.capa2[2]


            #movements
            self.player.update()
            self.player2.update()
            
            if self.pers!="Bubule" and self.pers!="UIIA":
                self.player.move_x(self.player.x1)
                for mur in self.murs + self.waters :
                    if self.player.rect.colliderect(mur) :
                        self.player.unmove_x(self.player.tx1)
                self.player.move_y(self.player.y1)
                for mur in self.murs + self.waters :
                    if self.player.rect.colliderect(mur) :
                        self.player.unmove_y(self.player.ty1)
            elif self.pers=="Bubule":
                self.player.move_x(self.player.x1)
                for mur in self.murs :
                    if self.player.rect.colliderect(mur) :
                        self.player.unmove_x(self.player.tx1)
                self.player.move_y(self.player.y1)
                for mur in self.murs :
                    if self.player.rect.colliderect(mur) :
                        self.player.unmove_y(self.player.ty1)
            else :
                self.player.move_x(self.player.x1)
                self.player.move_y(self.player.y1)

            if self.pers2!="Bubule" and self.pers2!="UIIA":
                self.player2.move_x(self.player2.x1)
                for mur in self.murs + self.waters :
                    if self.player2.rect.colliderect(mur) :
                        self.player2.unmove_x(self.player2.tx1)
                self.player2.move_y(self.player2.y1)
                for mur in self.murs + self.waters :
                    if self.player2.rect.colliderect(mur) :
                        self.player2.unmove_y(self.player2.ty1)
            elif self.pers2=="Bubule" :
                self.player2.move_x(self.player2.x1)
                for mur in self.murs :
                    if self.player2.rect.colliderect(mur) :
                        self.player2.unmove_x(self.player2.tx1)
                self.player2.move_y(self.player2.y1)
                for mur in self.murs :
                    if self.player2.rect.colliderect(mur) :
                        self.player2.unmove_y(self.player2.ty1)
            else :
                self.player2.move_x(self.player2.x1)
                self.player2.move_y(self.player2.y1)

            #bush
            """self.hide_p1=False
            for bush in self.bushs :
                if self.player.rect.colliderect(bush) :
                    self.hide_p1=True

            self.hide_p2=False
            for bush in self.bushs :
                if self.player2.rect.colliderect(bush) :
                    self.hide_p2=True"""
                    

            #bullet
            
            
            if self.shooting[0] :
                for mur in self.murs :
                    if mur.colliderect(self.bullet) and not self.pers=="Carroje" and not self.pers=="UIIA" :
                        self.shooting[2]=False
                        self.shooting[1]=self.ticks-self.diff_ticks*self.capa[3]
                        if self.pers!="Surge" :
                            self.player.canshoot=True
                        
                if self.ticks - self.shooting[1] <self.diff_ticks*self.capa[3] :
                    if self.shooting[2] :
                        self.bullet.update()
                        if self.player2.rect.colliderect(self.bullet) and self.canhit:
                            self.canhit=False
                            self.player2.PV-=self.capa[1]*self.damage_boost
                            self.player2.i_death=3*self.block
                            if self.rumb :
                                self.player2.joy.rumble(1,1,1000)
                            if self.pers=="Hank" :
                                self.player.PV+=50
                                if self.player.PV>self.capa[0] :
                                    self.player.PV=self.capa[0]
                            elif self.pers=="Mushy" :
                                self.time_poison=self.ticks
                                self.poison_ticks=int(self.time_poison/1000)
                            elif self.pers=="UIIA" :
                                self.time_UIIA=self.ticks
                else :
                    self.player.canshoot=True
                    if self.pers=="Surge" :
                        self.player.canshoot=False
                        self.canshot=True
                        self.a_surge=Surge(self.bullet.rect.x, self.bullet.rect.y, self.block)
                        self.time_surge=self.ticks
                    elif self.pers=="Berry" :
                        self.a_berry=Berry(self.bullet.rect.x, self.bullet.rect.y, self.block)

            
            
            if self.shooting2[0] :
                for mur in self.murs :
                    if mur.colliderect(self.bullet2) and not self.pers2=="Carroje" and not self.pers2=="UIIA" :
                        self.shooting2[2]=False
                        self.shooting2[1]=self.ticks-self.diff_ticks*self.capa2[3]
                        if self.pers2!="Surge" :
                            self.player2.canshoot=True
                        
                if self.ticks - self.shooting2[1] <self.diff_ticks*self.capa2[3] :
                    if self.shooting2[2] :
                        self.bullet2.update()
                        if self.player.rect.colliderect(self.bullet2) and self.canhit2:
                            self.canhit2=False
                            self.player.PV-=self.capa2[1]*self.damage_boost2
                            self.player.i_death=3*self.block
                            if self.rumb :
                                self.player.joy.rumble(1,1,1000)
                            if self.pers2=="Hank" :
                                self.player2.PV+=50
                                if self.player2.PV>self.capa2[0] :
                                    self.player2.PV=self.capa2[0]
                            elif self.pers2=="Mushy" :
                                self.time_poison=self.ticks
                                self.poison_ticks=int(self.time_poison/1000)
                            elif self.pers2=="UIIA" :
                                self.time_UIIA=self.ticks
                        
                        
                else :
                    self.player2.canshoot=True
                    if self.pers2=="Surge" : #pas besoin de mettre surge2 car in n'y as pas de doublons
                        self.player2.canshoot=False
                        self.canshot2=True
                        self.a_surge=Surge(self.bullet2.rect.x, self.bullet2.rect.y, self.block)
                        self.time_surge=self.ticks
                    elif self.pers2=="Berry" :
                        self.a_berry=Berry(self.bullet2.rect.x, self.bullet2.rect.y, self.block)

            #explosion de surge

            if self.ticks-self.time_surge<100 :
                if self.pers=="Surge" :
                    if self.player2.rect.colliderect(self.a_surge) and self.canhit:
                        self.player2.PV-=self.capa[1]*self.damage_boost*1.2
                        self.canhit=False
                        self.player2.i_death=3*self.block
                        if self.rumb :
                            self.player2.joy.rumble(1,1,1000)
                elif self.pers2=="Surge" :
                    if self.player.rect.colliderect(self.a_surge) and self.canhit2:
                        self.player.PV-=self.capa2[1]*self.damage_boost2*1.2
                        self.canhit2=False
                        self.player.i_death=3*self.block
                        if self.rumb :
                            self.player.joy.rumble(1,1,1000)
            else :
                if self.pers=="Surge" :
                    self.player.canshoot=self.canshot
                elif self.pers2=="Surge" :
                    self.player2.canshoot=self.canshot2

            if self.ticks-self.time_poison<4000 :
                self.new_ticks=int(self.ticks/1000)
                if self.pers=="Mushy" :
                    self.player2.modif=-1
                    self.player.modif=1
                    if self.new_ticks!=self.poison_ticks :
                        self.poison_ticks=self.new_ticks
                        self.player2.PV-=self.capa[1]/4*self.damage_boost
                        self.player2.i_death=1*self.block
                        if self.rumb :
                            self.player2.joy.rumble(1,1,1000)
                elif self.pers2=="Mushy" :
                    self.player.modif=-1
                    self.player2.modif=1
                    if self.new_ticks!=self.poison_ticks :
                        self.poison_ticks=self.new_ticks
                        self.player.PV-=self.capa2[1]/4*self.damage_boost2
                        self.player.i_death=1*self.block
                        if self.rumb :
                            self.player.joy.rumble(1,1,1000)
                else :
                    self.player.modif=1
                    self.player2.modif=1
            else :
                self.player.modif=1
                self.player2.modif=1

            if self.ticks-self.time_UIIA<2000 :
                if self.pers=="UIIA" :
                    self.player2.modif2=0
                elif self.pers2=="UIIA" :
                    self.player.modif2=0
            else :
                self.player.modif2=1
                self.player2.modif2=1

            

            #condition de fin

            if self.player.PV<=0 or self.player2.PV<=0 :
                if self.player.PV<=0 and self.player2.PV<=0 :
                    self.winner="draw"
                    reward=[2,2]
                elif self.player.PV<=0 :
                    self.winner="green"
                    reward=[1,3]
                else :
                    self.winner="blue"
                    reward=[3,1]
                self.plan="end"
                self.screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME)
                self.screen = pygame.display.set_mode((800, 600), pygame.NOFRAME)
                self.stop=False
                global info_P1, info_P2, pseudo_P1, pseudo_P2
                if pseudo_P1 !=None :
                    info_P1, pseudo_P1=Write(pseudo_P1, None, reward[0])
                if pseudo_P2 !=None :
                    info_P2, pseudo_P2=Write(pseudo_P2, None, reward[1])
                pygame.mixer.music.stop()
                pygame.mixer.music.load("Songs/vct.mp3")
                pygame.mixer.music.set_volume(self.son*2)
                pygame.mixer.music.play()

            #flaque de berry
            if self.pers=="Berry" :
                try :
                    if self.player2.rect.colliderect(self.a_berry) :
                        self.player2.PV-=4*self.damage_boost
                        if self.rumb :
                            self.player2.joy.rumble(1,1,1000)
                    if self.player.rect.colliderect(self.a_berry) and self.player.PV<self.capa[0] :
                        self.player.PV+=0.2*self.damage_boost
                except :
                    pass

            elif self.pers2=="Berry" :
                try :
                    if self.player.rect.colliderect(self.a_berry) :
                        self.player.PV-=4*self.damage_boost2
                        if self.rumb :
                            self.player.joy.rumble(1,1,1000)
                    if self.player2.rect.colliderect(self.a_berry) and self.player2.PV<self.capa2[0] :
                        self.player2.PV+=0.2*self.damage_boost
                except :
                    pass
        
        #menu de pause
        elif self.plan=="pause" :
            if self.plan_pause :
                self.screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME)
                self.screen = pygame.display.set_mode((800, 600), pygame.NOFRAME)
                self.plan_pause=False
                if self.shooting[0] :
                    self.tempo=self.ticks-self.shooting[1]
                if self.shooting2[0] :
                    self.tempo2=self.ticks-self.shooting2[1]
                self.tempo3=self.ticks-self.p_duration
            if self.plan_return :
                self.screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
                self.plan="play"
                if self.shooting[0] :
                    self.shooting[1]=self.ticks-self.tempo
                if self.shooting2[0] :
                    self.shooting2[1]=self.ticks-self.tempo2
                self.p_duration=self.ticks-self.tempo3


    def display(self) :
        #écran fond noire
        self.screen.fill("black")
        self.screen.blit(self.background, (0,0))



        
        if self.plan=="play" :
            if not pygame.mixer.music.get_busy() :
                pygame.mixer.music.play()
            
            #murs
            
            
            #berry
            if self.pers=="Berry" or self.pers2=="Berry":
                try :
                    self.a_berry.draw(self.screen)
                except :
                    pass

            if self.pers=="Spookie" or self.pers2=="Spookie" :
                if self.ticks-self.time_spookie<300 :
                    self.a_spookie.draw(self.screen)
            
            #potion
            if self.p_on_stage[0] :
                try :
                    if self.p_how_long+4000>=self.ticks :
                        self.screen.blit(self.spawn, (self.p_rect.x-self.block/2, self.p_rect.y-self.block/2))
                    else :
                        self.screen.blit(self.p_which[0], self.p_rect)
                except :
                    pass

            #player
            """if not self.hide_p1 :
                self.player.draw(self.screen)
            
            if not self.hide_p2 :
                self.player2.draw(self.screen)"""
            if self.pers!="UIIA" :
                self.player.draw(self.screen)
            if self.pers2!="UIIA" :
                self.player2.draw(self.screen)


            #map
            if self.map=="OO" :
                self.screen.blit(self.OO, (0,0))
            elif self.map=="SS" :
                self.screen.blit(self.SS, (0,0))
            else :
                self.screen.blit(self.CG, (0,0))
            
            """for mur in self.murs :
                pygame.draw.rect(self.screen, (255,10,200), mur, int(self.block/8))            
            for water in self.waters :
                pygame.draw.rect(self.screen, "blue", water, int(self.block/8))
            for bush in self.bushs :
                pygame.draw.rect(self.screen, "green", bush, int(self.block/8))"""

            if self.pers=="UIIA" :
                self.player.draw(self.screen)
            elif self.pers2=="UIIA" :
                self.player2.draw(self.screen)
            #info player
            self.player.drawstuff(self.screen)
            self.player2.drawstuff(self.screen)

            if self.emt :
                self.screen.blit(self.down, (self.player.x1-self.block/2, self.player.y1-self.block/2))
            if self.emt2 :
                self.screen.blit(self.down, (self.player2.x1-self.block/2, self.player2.y1-self.block/2))
            

            #bullet
            if self.shooting[0] :
                if self.ticks - self.shooting[1] <self.diff_ticks*self.capa[3] :
                    if self.shooting[2] :
                        self.bullet.draw(self.screen)
                else :
                    self.player.canshoot=True
                    self.shooting[0]=False

            

            if self.shooting2[0] :
                if self.ticks - self.shooting2[1] <self.diff_ticks*self.capa2[3] :
                    if self.shooting2[2] :
                        self.bullet2.draw(self.screen)
                else :
                    self.player2.canshoot=True
                    self.shooting2[0]=False

            if self.ticks-self.time_surge<100 :
                self.a_surge.draw(self.screen)
            

        elif self.plan=="end" :
            

            

             #print(self.draw, self.draw2)

            if self.winner=="draw" :
                screen.blit(font.render(f"Draw", True, "white"), (350, 450))
                screen.blit(self.draw, (100,100))
                screen.blit(self.draw2, (460,100))
                screen.blit(self.light, (0, -10))
                screen.blit(self.light2, (800-self.light2.get_width(), -10))
            elif self.winner=="blue" :
                screen.blit(font.render(f"Blue win", True, (10, 185, 239)), (350, 450))
                screen.blit(self.draw, (100,100))
                screen.blit(self.light, (0, -10))
            elif self.winner=="green" :
                screen.blit(font.render(f"Green win", True, (30, 220, 0)), (350, 450))
                screen.blit(self.draw2, (460,100))
                screen.blit(self.light2, (800-self.light2.get_width(), -10))

        elif self.plan=="pause" :
            if not pygame.mixer.music.get_busy() :
                pygame.mixer.music.play()
            
            screen.blit(self.draw, (100,100))
            screen.blit(self.draw2, (460,100))
            text_PV = font.render(str(int(self.player.PV)), True, (10, 185, 239))
            screen.blit(text_PV, (10, 10))
            text_PV2 = font.render(str(int(self.player2.PV)), True, (30, 220, 0))
            screen.blit(text_PV2, (790-text_PV2.get_width(), 10))
            txtn_123243=font.render(f"Pause", True, "red")
            screen.blit(txtn_123243, (400-txtn_123243.get_width()/2, 450))
            screen.blit(self.light, (0, -10))
            screen.blit(self.light2, (800-self.light2.get_width(), -10))
        


        pygame.display.flip()


    def run(self) :
        while self.running :
            self.event()
            self.update()
            self.display()
            self.clock.tick(FPS)

#setup


pygame.joystick.init()
pygame.font.init()
pygame.mixer.init()
font = pygame.font.Font("Others/arial.ttf", 20)
running=True
change=True

while running :
    play=False
    screen = pygame.display.set_mode((800, 600), pygame.NOFRAME)
    menu=Menu(screen, change)
    menu.run()
    change=False

    if play :
        WIDTH, HEIGHT = sett[3], sett[4]
        screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
        game=Game(screen)
        game.run()
    else :
        running=False

pygame.quit()