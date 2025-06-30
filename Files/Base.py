import pygame
from random import randint
from Player import Player
from Bullet import *
from Account import Choice, Write, Tour

pygame.init()


"""info_P1, pseudo_P1=["1740", "46546133468451", "True", "True", "True", "False", "True", "True", "True", "True", "True", "True", "True", "True", "True", "True", "True", "True", "True", "True", "True", "True"], "Dukook"
info_P2, pseudo_P2=["1740", "46546133468451", "True", "True", "True", "True", "True", "True", "True", "True", "True", "True", "True", "True", "True", "True", "True", "True", "True", "True", "True", "True"], 'DuCook'"""
tab=Tour()

if tab[0] :
    players=tab[2]
    stages=[players]
    stage_pos=1
    nb_fight=[0,(len(players)//2)-1]
    player_next=[]
    if len(players)%2!=0 :
        player_next.append(players[-1])
    info_P1=["0", "0", "True", "True", "True", "True", "True", "True", "True", "True", "True", "True", "True", "True", "True", "True", "True", "True", "True", "True", str(tab[3]), "False"]
    info_P2=["0", "0", "True", "True", "True", "True", "True", "True", "True", "True", "True", "True", "True", "True", "True", "True", "True", "True", "True", "True", str(tab[3]), "False"]

elif pygame.joystick.get_count() >= 2:
    info_P1, pseudo_P1=Choice(1)
    info_P2, pseudo_P2=Choice(2)


screen = pygame.display.set_mode((800, 600), pygame.NOFRAME)
screen.blit(pygame.transform.scale(pygame.image.load("Images/logo.png").convert_alpha(), (800, 600)), (0,0))
pygame.display.flip()

star=[1,2,2,2,3,4,5,6]
star_ammo=[0,0,3,4,5,6,7,7,7]
pers=["Hank", "Berry", "Surge", "Carroje", "Popofox", "Spookie", "Mushy", "Bubule", "Chick'n bob", "Owleaf", "Squeak", "Furbok", "Zipit", "Semibot", "Chauss-être", "Paper Dukook", "MiraDraco", "Pyroxis", "...", "UIIA"]
# "nom" : [PV, Damage, speed, bulletspeed(-:↑),skin,  range, spam, nb_bullet]
capa={"Hank" : (1320, 240, 0.9, 1.2, pygame.transform.scale(pygame.image.load("Images/f_Hank.png").convert_alpha(), (240,285)),700, 1300, 6),
      "Berry": (1000, 230, 1.1, 1.2, pygame.transform.scale(pygame.image.load("Images/f_Berry.png").convert_alpha(), (240,285)), 600, 1200, 5),
      "Surge": (1260, 225, 0.9, 1.3, pygame.transform.scale(pygame.image.load("Images/f_Surge.png").convert_alpha(), (240,285)), 650, 1300, 6),
      "Carroje": (1080, 280, 0.8, 1.7, pygame.transform.scale(pygame.image.load("Images/f_Carroje.png").convert_alpha(), (240,285)), 1200, 1300, 4),
      "Popofox": (1150, 155, 1.2, 0.6, pygame.transform.scale(pygame.image.load("Images/f_Popofox.png").convert_alpha(), (240,285)), 450, 700, 18),
      "Spookie": (1220, 150, 1.0, 1.0, pygame.transform.scale(pygame.image.load("Images/f_Spookie.png").convert_alpha(), (240,285)), 650, 1400, 5),
      "Mushy": (1050, 130, 1.05, 1.1, pygame.transform.scale(pygame.image.load("Images/f_Mushy.png").convert_alpha(), (240,285)), 500, 1450, 8),
      "Bubule": (1400, 200, 0.85, 0.9, pygame.transform.scale(pygame.image.load("Images/f_Bubule.png").convert_alpha(), (240,285)), 600, 1000, 10),
      "Chick'n bob": (950, 37, 1.25, 0.9, pygame.transform.scale(pygame.image.load("Images/f_Chick'n bob.png").convert_alpha(), (240,285)), 500, 1100, 7),
      "Owleaf": (1300, 170, 1.0, 1.0, pygame.transform.scale(pygame.image.load("Images/f_Owleaf.png").convert_alpha(), (240,285)), 650, 1450, 3),
      "Squeak": (1350, 180, 0.9, 1.1, pygame.transform.scale(pygame.image.load("Images/f_Squeak.png").convert_alpha(), (240,285)), 900, 1310, 5),
      "Furbok": (1500, 780, 0.75, 0.7, pygame.transform.scale(pygame.image.load("Images/f_Furbok.png").convert_alpha(), (240,285)), 700, 2200, 2),
      "Zipit": (1220, 305, 1.0, 0.8, pygame.transform.scale(pygame.image.load("Images/f_Zipit.png").convert_alpha(), (240,285)), 650, 1500, 3),
      "Semibot": (1330, 260, 1.2, 0.85, pygame.transform.scale(pygame.image.load("Images/f_Semibot.png").convert_alpha(), (240,285)), 750, 1250, 5),
      "Chauss-être": (1180, 8, 1.1, 1.0, pygame.transform.scale(pygame.image.load("Images/f_Chauss-être.png").convert_alpha(), (240,285)), 200, 450, 6),
      "Paper Dukook": (1200, 180, 1.1, 1.1, pygame.transform.scale(pygame.image.load("Images/f_Paper Dukook.png").convert_alpha(), (240,285)), 720, 1200, 8),
      "MiraDraco": (1340, 220, 0.9, 0.8, pygame.transform.scale(pygame.image.load("Images/f_MiraDraco.png").convert_alpha(), (240,285)), 700, 1450, 4),
      "Pyroxis": (1210, 160, 1.1, 0.9, pygame.transform.scale(pygame.image.load("Images/f_Pyroxis.png").convert_alpha(), (240,285)), 500, 1000, 4),
      "...": (500, 190, 0.9, 1.0, pygame.transform.scale(pygame.image.load("Images/f_....png").convert_alpha(), (240,285)), 680, 1100, 2),
      "UIIA": (1800, 310, 1.5, 0.65, pygame.transform.scale(pygame.image.load("Images/f_UIIA.png").convert_alpha(), (240,285)), 1000, 1000, 69)
}
berry_heal=50
hank_heal=80
semibot_damage=60
xbox={"-":6,
      "L":2,
      "U":3,
      "R":1,
      "D":0,
      "N":5,
      "B":4,
}

ps={"-":4,
      "L":2,
      "U":3,
      "R":1,
      "D":0,
      "N":10,
      "B":9,
}

act=xbox
act2=xbox




nb_pers=len(pers)-1
if tab[0] :
    nb_pers-=1
nb_pers_base=nb_pers

FPS=45
sett=[]

class Menu :
    def __init__(self, screen, change):
        if tab[0] :
            global stages, stage_pos, player_next, players, nb_fight
            gay=True
            if nb_fight[0]>nb_fight[1] :
                print(nb_fight)
                stages.append(player_next)
                players=stages[stage_pos]
                print(players)
                if len(players)>=2 :
                    stage_pos+=1
                    player_next=[]
                    if len(players)%2!=0 :
                        player_next.append(players[-1])
                    nb_fight=[0,(len(players)//2)-1]
                else :
                    print(f"{players[0]} win !")
                    gay=False
            if gay :
                global pseudo_P1, pseudo_P2
                pseudo_P1=players[nb_fight[0]*2]
                pseudo_P2=players[nb_fight[0]*2+1]
                nb_fight[0]+=1
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

        #autres images
        self.cross=pygame.transform.scale_by(pygame.image.load("Images/cross.png").convert_alpha(), 0.48)
        self.coin=pygame.transform.scale_by(pygame.image.load("Images/coin.png").convert_alpha(), 0.5)
        self.logo=pygame.transform.scale(pygame.image.load("Images/logo.png").convert_alpha(), (100, 100))
        self.SS=pygame.transform.scale_by(pygame.image.load("Images/SS.png").convert(), 3)
        self.OO=pygame.transform.scale_by(pygame.image.load("Images/OO.png").convert(), 3)
        self.CG=pygame.transform.scale_by(pygame.image.load("Images/CG.png").convert(), 3)
        self.RD=pygame.transform.scale_by(pygame.image.load("Images/RD.png").convert(), 3)
        self.ZG=pygame.transform.scale_by(pygame.image.load("Images/ZG.png").convert(), 3)
        self.xbox=pygame.transform.scale_by(pygame.image.load("Images/xbox.png").convert_alpha(), 0.12)
        self.ps= pygame.transform.scale_by(pygame.image.load("Images/ps.png").convert_alpha(), 0.16)

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
            pygame.time.delay(2000)

        
            
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

        
        
        self.canback1, self.canback2, self.cannext1, self.cannext2, self.canchange_map, self.cansettings, self.canrumb, self.canplay1, self.canplay2, self.can_swapp=False, False, False, False, False, False, False, False, False, False#bcp de can
        

        #sons
        
        pygame.mixer.music.load("Songs/loby.mp3")
        pygame.mixer.music.set_volume(self.son/100)
        pygame.mixer.music.play()

    def event(self) :

        global act, act2
        settings=self.joy1.get_button(act["-"])

        if self.plan=="settings" :

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE :
                        self.joy1,self.joy2=self.joy2,self.joy1
                        self.swap= not self.swap
                    


            low=self.joy1.get_button(act["D"])
            mid=self.joy1.get_button(act["R"])
            high=self.joy1.get_button(act["U"])
            rumb=self.joy1.get_button(act["L"])
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
                self.WIDTH,self.HEIGHT = 2560, 1440
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
                if event.type == pygame.KEYDOWN :
                    if (event.key == pygame.K_KP1 or event.key == pygame.K_LEFT or event.key == pygame.K_l) and act==ps :
                        act=xbox
                    elif (event.key == pygame.K_KP1 or event.key == pygame.K_LEFT or event.key == pygame.K_l) and act==xbox :
                        act=ps
                    if (event.key == pygame.K_KP2 or event.key == pygame.K_RIGHT or event.key == pygame.K_r) and act2==ps :
                        act2=xbox
                    elif (event.key == pygame.K_KP2 or event.key == pygame.K_RIGHT or event.key == pygame.K_r) and act2==xbox :
                        act2=ps


            self.play1 = self.joy1.get_button(act["U"])
            self.play2 = self.joy2.get_button(act2["U"])
            next1=self.joy1.get_button(act["N"])
            next2=self.joy2.get_button(act2["N"])
            back1=self.joy1.get_button(act["B"])
            back2=self.joy2.get_button(act2["B"])
            self.purchase1=self.joy1.get_button(act["R"])
            self.purchase2=self.joy2.get_button(act2["R"])
            change_map=self.joy1.get_button(act["D"])
            UIIA=pygame.key.get_pressed()
            vibr=self.joy1.get_button(act["L"])
            vibr2=self.joy2.get_button(act2["L"])
            if not tab[0] :
                if UIIA[pygame.K_u] and UIIA[pygame.K_i] and UIIA[pygame.K_a] and UIIA[pygame.K_SPACE] and self.can_swapp:
                    self.can_swapp=False
                    global nb_pers
                    if nb_pers==nb_pers_base :
                        nb_pers+=1
                    else :
                        nb_pers=nb_pers_base
                        if self.pick1==nb_pers_base : #car l'indice est moins 1 par rapport au nb mais plus 1par rapport au max sans UIIA
                            self.pick1=0
                            if self.pick1==self.pick2 :
                                self.pick1+=1
                        elif self.pick2==nb_pers_base :
                            self.pick2=0
                            if self.pick1==self.pick2 :
                                self.pick2+=1

                if not UIIA[pygame.K_SPACE]:
                    self.can_swapp=True

            if self.srumb :

                if vibr :
                    self.joy1.rumble(1,1,1)

                if vibr2 :
                    self.joy2.rumble(1,1,1)

            if vibr :
                self.pick1=randint(0, nb_pers-1)
                if self.pick1==self.pick2 :
                    self.pick1+=1
                if self.pick1>=nb_pers :
                    self.pick1=0
                    if self.pick1==self.pick2 :
                        self.pick1+=1
            if vibr2 :
                self.pick2=randint(0, nb_pers-1)
                if self.pick1==self.pick2 :
                    self.pick2-=1
                if self.pick2<0 :
                    self.pick2=nb_pers-1
                    if self.pick1==self.pick2 :
                        self.pick2-=1

            if self.purchase1 or self.play1 or vibr :
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
                        self.map="ZG"
                    elif self.map=="ZG" :
                        self.map="RD"
                    else :
                        self.map="SS"
                elif not change_map :
                    self.canchange_map=True

            if self.purchase2 or self.play2 or vibr2:
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

            
            actual_pick=self.pick1%nb_pers+2
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

            actual_pick2=self.pick2%nb_pers+2
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
            elif self.map=="ZG" :
                self.map_color=["white", "white", "white", "yellow"]
                self.map_pos=(-100, -100)
            elif self.map=="RD" :
                self.map_color=["yellow", "yellow", "yellow", "yellow"]
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

            #perso
            perspick=capa[pers[self.pick1]]
            self.screen.blit(perspick[4], (136, 133))

            perspick=capa[pers[self.pick2]]
            self.screen.blit(perspick[4], (426, 133))

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
                if int(info_P2[1])>10000 :
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

            #info prix
            self.screen.blit(font.render("Fighters cost 10 coins", True, (255,10,200)), (302, 428))

            #info controller
            if act==ps :
                self.screen.blit(self.ps, (260, 20))
            elif act==xbox :
                self.screen.blit(self.xbox, (260, 20))
            if act2==ps :
                self.screen.blit(self.ps, (475, 20))
            elif act2==xbox :
                self.screen.blit(self.xbox, (475, 20))

            #logo
            self.screen.blit(self.logo, (350, -10))

            #map
            self.screen.blit(self.dpad_button_down, self.map_pos)
            self.screen.blit(self.SS, (12, 200))
            self.screen.blit(self.OO, (686, 200))
            self.screen.blit(self.CG, (12, 280))
            self.screen.blit(self.ZG, (686, 280))
            self.screen.blit(font.render("Shooting", True, self.map_color[0]), (24, 140))
            self.screen.blit(font.render("Stars", True, self.map_color[0]), (38, 170))
            self.screen.blit(font.render("Out in", True, self.map_color[1]), (710, 140))
            self.screen.blit(font.render("the Open", True, self.map_color[1]), (698, 170))
            self.screen.blit(font.render("Canal", True, self.map_color[2]), (35, 350))
            self.screen.blit(font.render("Grande", True, self.map_color[2]), (30, 380))
            self.screen.blit(font.render("Zen", True, self.map_color[3]), (718, 350))
            self.screen.blit(font.render("Garden", True, self.map_color[3]), (704, 380))
            

        pygame.display.flip()
        
    def run(self) :
        while self.running :
            self.event()
            self.update()
            self.display()
            self.clock.tick(FPS)







class Game :
    
    def __init__(self, screen):
        global sett, act, act2
        self.rumb=sett[9]
        self.pers=pers[sett[6]]
        self.capa=capa[self.pers]
        self.pers2=pers[sett[7]]
        self.capa2=capa[self.pers2]
        self.map=sett[8]

        self.evnt=randint(1,10)

        self.b_potion=1
        self.ot=1
        self.fast=1
        if self.evnt<=5 :
            self.name_event="Normal"
        elif self.evnt<=7 :
            self.b_potion=2
            self.name_event="Potion unleash"
        elif self.evnt<=8 :
            self.ot=2.5
            self.name_event="Over time"
        elif self.evnt<=10 :
            self.fast=1.6
            self.name_event="Gotta go fast"

        if self.map=="RD" :
            rand=randint(0,3)
            if rand==0:
                self.map="SS"
            elif rand==1 :
                self.map="OO"
            elif rand==2 :
                self.map="CG"
            else :
                self.map="ZG"
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
        self.player=Player(1*self.block, 9*self.block, self.pers, sett[0], WIDTH, HEIGHT, 0, self.block, j[0], act, self.ot, self.fast)
        self.player2=Player(30*self.block, 9*self.block, self.pers2, sett[1], WIDTH, HEIGHT, 1, self.block, j[1], act2, self.ot, self.fast)
        self.plan="start"

        #potions
        self.p_pos=[(16*self.block-self.block/2, 9*self.block-self.block/2), (20*self.block, 1*self.block), (11*self.block, 16*self.block), (20*self.block, 16*self.block), (11*self.block, 1*self.block), (19*self.block, 10*self.block), (12*self.block, 7*self.block)]
        self.p_speed=pygame.transform.scale(pygame.image.load("Images/p_speed.png").convert_alpha(), (self.block, self.block))
        self.p_damage=pygame.transform.scale(pygame.image.load("Images/p_damage.png").convert_alpha(), (self.block, self.block))
        self.p_heal=pygame.transform.scale(pygame.image.load("Images/p_heal.png").convert_alpha(), (self.block, self.block))
        self.p_ammo=pygame.transform.scale(pygame.image.load("Images/p_ammo.png").convert_alpha(), (self.block, self.block))
        self.p_love=pygame.transform.scale(pygame.image.load("Images/p_love.png").convert_alpha(), (self.block, self.block))
        self.spawn=pygame.transform.scale(pygame.image.load("Images/spawn.png").convert_alpha(), (2*self.block, 2*self.block))
        self.p_all=[(self.p_speed, "speed"), (self.p_damage, "damage"), (self.p_ammo, "ammo"), (self.p_love, "love"), (self.p_heal, "heal"), (self.p_heal, "heal")]
        self.p_on_stage=[False,pygame.time.get_ticks()+randint(6000, 8000)]
        self.p_how_long=-5000

        #création mur
        self.murs=[]
        self.waters=[]
        self.bushs=[]

        self.murs.append(pygame.Rect(-1*self.block,-1*self.block, 34*self.block, 1*self.block))
        self.murs.append(pygame.Rect(-1*self.block,0*self.block, 1*self.block, 18*self.block))
        self.murs.append(pygame.Rect(-1*self.block,18*self.block, 34*self.block, 1*self.block))
        self.murs.append(pygame.Rect(32*self.block,0*self.block, 1*self.block, 18*self.block))

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

        elif self.map=="CG" :
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
        
        elif self.map=="ZG" :
            self.murs.append(pygame.Rect(0*self.block,0*self.block, 6*self.block, 2*self.block))
            self.murs.append(pygame.Rect(0*self.block,5*self.block, 2*self.block, 1*self.block))
            self.murs.append(pygame.Rect(0*self.block,12*self.block, 2*self.block, 1*self.block))
            self.murs.append(pygame.Rect(0*self.block,16*self.block, 5*self.block, 2*self.block))
            self.murs.append(pygame.Rect(9*self.block,0*self.block, 2*self.block, 2*self.block))
            self.murs.append(pygame.Rect(9*self.block,5*self.block, 2*self.block, 6*self.block))
            self.murs.append(pygame.Rect(11*self.block,8*self.block, 1*self.block, 3*self.block))
            self.murs.append(pygame.Rect(9*self.block,13*self.block, 2*self.block, 5*self.block))
            self.murs.append(pygame.Rect(11*self.block,17*self.block, 1*self.block, 1*self.block))
            self.murs.append(pygame.Rect(15*self.block,4*self.block, 1*self.block, 1*self.block))
            self.murs.append(pygame.Rect(14*self.block,5*self.block, 2*self.block, 1*self.block))
            self.murs.append(pygame.Rect(16*self.block,12*self.block, 2*self.block, 1*self.block))
            self.murs.append(pygame.Rect(16*self.block,13*self.block, 1*self.block, 1*self.block))
            self.murs.append(pygame.Rect(20*self.block,0*self.block, 1*self.block, 1*self.block))
            self.murs.append(pygame.Rect(21*self.block,0*self.block, 2*self.block, 5*self.block))
            self.murs.append(pygame.Rect(20*self.block,7*self.block, 1*self.block, 3*self.block))
            self.murs.append(pygame.Rect(21*self.block,7*self.block, 2*self.block, 6*self.block))
            self.murs.append(pygame.Rect(21*self.block,16*self.block, 2*self.block, 2*self.block))
            self.murs.append(pygame.Rect(27*self.block,0*self.block, 5*self.block, 2*self.block))
            self.murs.append(pygame.Rect(30*self.block,5*self.block, 2*self.block, 1*self.block))
            self.murs.append(pygame.Rect(30*self.block,12*self.block, 2*self.block, 1*self.block))
            self.murs.append(pygame.Rect(26*self.block,16*self.block, 6*self.block, 2*self.block))

            self.waters.append(pygame.Rect(0*self.block,2*self.block, 2*self.block, 3*self.block))
            self.waters.append(pygame.Rect(0*self.block,13*self.block, 2*self.block, 3*self.block))
            self.waters.append(pygame.Rect(14*self.block,10*self.block, 2*self.block, 4*self.block))
            self.waters.append(pygame.Rect(16*self.block,4*self.block, 2*self.block, 4*self.block))
            self.waters.append(pygame.Rect(30*self.block,2*self.block, 2*self.block, 3*self.block))
            self.waters.append(pygame.Rect(30*self.block,13*self.block, 2*self.block, 3*self.block))

            self.p_pos=[(16*self.block-self.block/2, 9*self.block-self.block/2), (5*self.block, 5*self.block), (26*self.block, 12*self.block), (5*self.block, 12*self.block), (26*self.block, 5*self.block), (12*self.block, 6*self.block), (19*self.block, 11*self.block), (12*self.block, 15*self.block), (19*self.block, 2*self.block)]

        self.SS=pygame.transform.scale(pygame.image.load("Images/t_SS.png").convert_alpha(), (WIDTH, HEIGHT))
        self.OO=pygame.transform.scale(pygame.image.load("Images/t_OO.png").convert_alpha(), (WIDTH, HEIGHT))
        self.CG=pygame.transform.scale(pygame.image.load("Images/t_CG.png").convert_alpha(), (WIDTH, HEIGHT))
        self.ZG=pygame.transform.scale(pygame.image.load("Images/t_ZG.png").convert_alpha(), (WIDTH, HEIGHT))
        self.background=pygame.transform.scale(pygame.image.load("Images/background.png").convert_alpha(), (WIDTH, HEIGHT))

        #autres
        self.explosion=bool(1+1==2)
        self.running=True
        self.p_duration=-10000
        self.mort=0
        self.mort_exp=0.000001
        self.emt=False
        self.emt2=False
        

        #importation du song
        self.son=sett[2]/100
        pygame.mixer.music.stop()
        pygame.mixer.music.load("Songs/321.mp3")
        pygame.mixer.music.set_volume(self.son)
        pygame.mixer.music.play()


        self.ice=pygame.transform.scale(pygame.image.load("Images/ice_cream.png").convert_alpha(), (self.block*2,self.block*2))
        self.ice_pos=self.ice.get_rect(x=-1000, y=-1000)

        self.boom=pygame.transform.scale(pygame.image.load("Images/boom.png").convert_alpha(), (self.block*3.5,self.block*3.5))
        self.boom_pos=self.boom.get_rect(x=-1000,y=-1000)

        self.cookie=pygame.transform.scale(pygame.image.load("Images/Cookie.png").convert_alpha(), (self.block*3.5,self.block*3.5))
        self.cookie_pos=self.cookie.get_rect(x=-1000,y=-1000)

        self.smelt=pygame.transform.scale(pygame.image.load("Images/smelt.png").convert_alpha(), (self.block*4,self.block*4))
        self.smelt_pos=self.smelt.get_rect(x=-1000,y=-1000)

        self.tp=pygame.transform.scale(pygame.image.load("Images/tp.png").convert_alpha(), (self.block, self.block))

        self.down=pygame.transform.scale(pygame.image.load("Images/down.png").convert_alpha(), (self.block/2,self.block/2))



        self.draw=self.capa[4]

        self.draw2=self.capa2[4]
        

        self.light=pygame.transform.rotozoom(pygame.image.load("Images/light.png").convert_alpha(), 5, 2)
        self.light2=pygame.transform.rotozoom(pygame.image.load("Images/light.png").convert_alpha(), -5, 2)
        self.c_1=pygame.transform.scale(pygame.image.load("Images/1.png").convert_alpha(), (6*self.block, 4*self.block))
        self.c_2=pygame.transform.scale(pygame.image.load("Images/2.png").convert_alpha(), (6*self.block, 4*self.block))
        self.c_3=pygame.transform.scale(pygame.image.load("Images/3.png").convert_alpha(), (6*self.block, 4*self.block))

        #def des bullet

        self.bullet_P1=Bullet(self.pers, self.block, self.capa[3])
        self.bullet_P2=Bullet(self.pers2, self.block, self.capa2[3])
  
    def event(self) :

        self.ticks=pygame.time.get_ticks()
        global running
        
        pause=bool(self.player.joy.get_button(act["-"]) and self.player2.joy.get_button(act2["-"]))

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
            if self.pers=="UIIA" or self.pers2=="UIIA" :
                pygame.mixer.music.load("Songs/UIIA.mp3")
            else :
                pygame.mixer.music.load("Songs/Battle.mp3")
            pygame.mixer.music.play()

        elif self.plan == "play" :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    running=False

            self.player.event()
            if self.player.tping :
                self.player.time_effect=self.ticks
                self.player.tping=False
            self.player2.event()
            if self.player2.tping :
                self.player2.time_effect=self.ticks
                self.player2.tping=False

            self.emt=self.player.joy.get_button(act["U"])
            self.emt2=self.player2.joy.get_button(act2["U"])
            """if self.player.shot_acc[0] :
                self.player.canshoot = False
                self.canshot=False
                self.canhit=True
                self.bullet=Bullet(self.player.rect.x, self.player.rect.y, self.player.ajusted_angle, self.pers, self.player.shot_acc[1], self.block, self.capa[3])
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
                self.bullet2=Bullet(self.player2.rect.x, self.player2.rect.y, self.player2.ajusted_angle, self.pers2, self.player2.shot_acc[1], self.block, self.capa2[3])
                self.player2.shot_acc=[False, False]
                self.shooting2=[True, self.ticks, True]
                if self.pers2=="Spookie" :
                    self.a_spookie=Spookie(self.player2.rect.x, self.player2.rect.y, self.block)
                    self.time_spookie=self.ticks
                    if self.player.rect.colliderect(self.a_spookie):
                        self.player.PV-=self.capa2[1]*self.damage_boost2*1.2
                        self.player.i_death=3*self.block
                        if self.rumb :
                            self.player.joy.rumble(1,1,1000)"""

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

            stop2=bool(self.player.joy.get_button(act["-"]) or self.player2.joy.get_button(act2["-"]))
            if self.running ==True :
                self.running=not bool(stop or stop2)
                           
    def stat0(self) :
        self.player.damage_boost=1.0
        self.player.base_speed=self.capa[2]
        self.player.ammo_boost=1
        self.player2.damage_boost=1.0
        self.player2.base_speed=self.capa2[2]
        self.player2.ammo_boost=1

    def update(self) :
        
        
        
        if self.plan == "play" :

            if not pygame.mixer.music.get_busy() :
                pygame.mixer.music.play()

            #over time
            self.mort+=1

            if self.mort>2200*self.ot :
                self.mort_exp+=0.0000005
                self.player.PV-=self.mort_exp*self.capa[0]
                self.player2.PV-=self.mort_exp*self.capa2[0]

            #potion
            if self.p_on_stage[1]<self.ticks and not self.p_on_stage[0]:
                self.p_on_stage[0]=True
                self.p_how_long=self.ticks
                self.p_pos_on_stage=self.p_pos[randint(0,len(self.p_pos)-1)]
                if self.ot==1 :
                    self.p_which=self.p_all[randint(0,len(self.p_all)-1)]
                else :
                    self.p_which=self.p_all[randint(0,len(self.p_all)-3)]#pas de heal
                self.p_rect=self.p_which[0]
                self.p_rect=self.p_rect.get_rect(x=self.p_pos_on_stage[0], y=self.p_pos_on_stage[1])
            if self.p_on_stage[0] and self.p_how_long+4000<self.ticks :
                if self.player.rect.colliderect(self.p_rect) :
                    self.stat0()
                    if self.p_which[1]=="heal" :
                        self.player.PV+=300*self.b_potion
                    elif self.p_which[1]=="speed" :
                        self.player.base_speed*=1.4
                        self.p_duration=self.ticks
                    elif self.p_which[1]=="damage" :
                        self.player.damage_boost=1.2
                        self.p_duration=self.ticks
                    elif self.p_which[1]=="ammo" :
                        self.player.ammo_boost=0
                        self.player.ammo=self.player.capa[6]
                        self.p_duration=self.ticks
                    else :
                        self.player.PV=1
                    self.p_on_stage=[False,self.ticks+randint(6000/self.b_potion, 8000/self.b_potion)]
                if self.player2.rect.colliderect(self.p_rect) :
                    self.stat0()
                    if self.p_which[1]=="heal" :
                        self.player2.PV+=300*self.b_potion
                    elif self.p_which[1]=="speed" :
                        self.player2.base_speed*=1.4
                        self.p_duration=self.ticks
                    elif self.p_which[1]=="damage" :
                        self.player2.damage_boost=1.2
                        self.p_duration=self.ticks
                    elif self.p_which[1]=="ammo" :
                        self.player2.ammo_boost=0
                        self.player2.ammo=self.player2.capa[6]
                        self.p_duration=self.ticks
                    else :
                        self.player2.PV=1
                    self.p_on_stage=[False,self.ticks+randint(6000/self.b_potion, 8000/self.b_potion)]

                if self.p_how_long+14000<self.ticks :
                    self.p_on_stage=[False,self.ticks+randint(6000/self.b_potion, 8000/self.b_potion)]


            if self.p_duration+(5000*self.b_potion)<self.ticks :
                self.stat0()
                


            #movements
            self.player.update()
            self.player2.update()
            
            hit=False
            if self.pers!="Bubule" and self.pers!="UIIA":
                self.player.move_x(self.player.x1)
                for mur in self.murs + self.waters :
                    if self.player.rect.colliderect(mur) :
                        self.player.unmove_x(self.player.tx1)
                        hit=True
                self.player.move_y(self.player.y1)
                for mur in self.murs + self.waters :
                    if self.player.rect.colliderect(mur) :
                        self.player.unmove_y(self.player.ty1)
                        hit=True
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

            

            hit2 = False
            if self.pers2!="Bubule" and self.pers2!="UIIA":
                self.player2.move_x(self.player2.x1)
                for mur in self.murs + self.waters :
                    if self.player2.rect.colliderect(mur) :
                        self.player2.unmove_x(self.player2.tx1)
                        hit2=True
                self.player2.move_y(self.player2.y1)
                for mur in self.murs + self.waters :
                    if self.player2.rect.colliderect(mur) :
                        self.player2.unmove_y(self.player2.ty1)
                        hit2=True
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

            if hit and self.pers=="..." and self.rumb :
                self.player.joy.rumble(0.2,0.2,int(1000/FPS))
            elif hit2 and self.pers2=="..." and self.rumb :
                self.player2.joy.rumble(0.2,0.2,int(1000/FPS))
            

            #condition de fin

            if self.player.PV<=0 or self.player2.PV<=0 :
                global player_next, pseudo_P1, pseudo_P2
                if self.player.PV<=0 and self.player2.PV<=0 :
                    self.winner="draw"
                    reward=[6,6]
                elif self.player.PV<=0 :
                    self.winner="green"
                    reward=[3,10]
                    if tab[0] :
                        player_next.append(pseudo_P2)
                else :
                    self.winner="blue"
                    reward=[10,3]
                    if tab[0] :
                        player_next.append(pseudo_P1)
                self.plan="end"
                self.screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME)
                self.screen = pygame.display.set_mode((800, 600), pygame.NOFRAME)
                self.stop=False
                if not tab[0] :
                    global info_P1, info_P2
                    if pseudo_P1 !=None :
                        info_P1, pseudo_P1=Write(pseudo_P1, None, reward[0])
                    if pseudo_P2 !=None :
                        info_P2, pseudo_P2=Write(pseudo_P2, None, reward[1])
                pygame.mixer.music.stop()
                pygame.mixer.music.load("Songs/vct.mp3")
                pygame.mixer.music.set_volume(self.son*2)
                pygame.mixer.music.play()

            #flaque de berry
            """if self.pers=="Berry" :
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
                    pass"""
        
        #menu de pause
        elif self.plan=="pause" :
            if self.plan_pause :
                self.screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME)
                self.screen = pygame.display.set_mode((800, 600), pygame.NOFRAME)
                self.plan_pause=False
            if self.plan_return :
                self.screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
                self.plan="play"

    def updraw_bullet(self, pers, player, player_adv, bullet, capa) :
        if self.plan=="play" :
            if player.shot_acc[0]==True :
                player.shot_acc[0]=False
                player.canshoot=False
                player.shooting=True
                player.range=0
                player.hitwall=False
                if pers=="Owleaf" :
                    bullet.settings_owl(player.rect.x, player.rect.y, player.ajusted_angle, player.shot_acc[1])
                    player.canhit=[True, True, True]
                elif pers=="Paper Dukook" :
                    player.ammo+=1*player.ammo_boost
                    self.n=randint(0,star_ammo[player.ammo]) 
                    player.ammo-=star[self.n]*player.ammo_boost
                    bullet.settings_paper(player.rect.x, player.rect.y, player.ajusted_angle, player.shot_acc[1], self.n)
                    player.canhit=True
                else :
                    bullet.settings(player.rect.x, player.rect.y, player.ajusted_angle, player.shot_acc[1])
                    player.canhit=True
                if pers=="Furbok" :
                    player.furb=randint(10,350)
                    player.furb2=(randint(0,1)-0.5)*2
                    player.furb22=(randint(0,1)-0.5)*2
                elif pers=="Semibot" :
                    if player.PV>semibot_damage :
                        player.PV-=semibot_damage
                player.duration_bullet=self.ticks
                player.explosion=False


            if self.ticks-player.duration_bullet>capa[6] :
                player.canshoot=True
            elif self.ticks-player.duration_bullet>(capa[5]+player.range) :
                player.shooting=False

            if pers=="Hank" :
                if player.shooting :
                    for mur in self.murs :
                        if mur.colliderect(bullet) :
                            player.shooting=False
                            player.hitwall=True
                            player.duration_bullet=self.ticks-capa[5]
                    if not player.hitwall :
                        bullet.update()
                        bullet.draw(self.screen)
                        if player_adv.rect.colliderect(bullet) :
                            player.canhit=False
                            player.hitwall=True
                            player_adv.PV-=capa[1]*player.damage_boost*player.powerlift
                            player_adv.i_death=3*self.block
                            if self.rumb :
                                player_adv.joy.rumble(1,1,1000)
                            player.PV+=hank_heal
                            player.duration_bullet=self.ticks-capa[5]
            
            elif pers=="Berry" :
                if self.ticks-player.duration_bullet>capa[5] :
                    self.ice_pos.center=bullet.rect.center
                #self.screen.blit(self.ice, self.ice_pos)

                if player_adv.rect.colliderect(self.ice_pos) :
                    player_adv.PV-=capa[1]/FPS*player.damage_boost*player.powerlift
                    player_adv.i_death=1*self.block
                    if self.rumb :
                        player_adv.joy.rumble(1,1,200)
                if player.rect.colliderect(self.ice_pos) and self.ot==1:
                    player.PV+=capa[1]/(berry_heal*FPS)*player.damage_boost*player.powerlift

                if player.shooting :
                    for mur in self.murs :
                        if mur.colliderect(bullet) :
                            player.shooting=False
                            player.hitwall=False
                            player.duration_bullet=self.ticks-capa[5]
                            self.ice_pos.center=bullet.rect.center
                    if not player.hitwall :
                        bullet.update()
                        bullet.draw(self.screen)
                        if player_adv.rect.colliderect(bullet) :
                            player.canhit=False
                            player.hitwall=True
                            player_adv.PV-=capa[1]*player.damage_boost*player.powerlift
                            player_adv.i_death=3*self.block
                            self.ice_pos.center=bullet.rect.center
                            if self.rumb :
                                player_adv.joy.rumble(1,1,1000)
                            player.duration_bullet=self.ticks-capa[5]
            
            elif pers=="Surge" :
                if self.ticks-player.duration_bullet>capa[5] and not player.explosion:
                    self.boom_pos.center=bullet.rect.center
                    player.time_effect=self.ticks
                    player.explosion=True
                if player.shooting :
                    for mur in self.murs :
                        if mur.colliderect(bullet) :
                            player.shooting=False
                            player.hitwall=True
                            player.duration_bullet=self.ticks-capa[5]
                            player.time_effect=self.ticks
                            self.boom_pos.center=bullet.rect.center
                            player.explosion=True
                    if not player.hitwall :
                        bullet.update()
                        bullet.draw(self.screen)
                        if player_adv.rect.colliderect(bullet) :
                            player.canhit=False
                            player.hitwall=True
                            player.time_effect=self.ticks
                            self.boom_pos.center=bullet.rect.center
                            player.explosion=True
                            player_adv.PV-=capa[1]*player.damage_boost*player.powerlift
                            player_adv.i_death=3*self.block
                            if self.rumb :
                                player_adv.joy.rumble(1,1,1000)
                            player.duration_bullet=self.ticks-capa[5]
                            
                if self.ticks-player.time_effect<300 :
                    self.screen.blit(self.boom, self.boom_pos)
                    if player.canhit :
                        if player_adv.rect.colliderect(self.boom_pos) :
                            player.canhit=False
                            player_adv.PV-=capa[1]*player.damage_boost*1.2*player.powerlift
                            player_adv.i_death=3*self.block
                            if self.rumb :
                                player_adv.joy.rumble(1,1,1000)

            elif pers=="Carroje" :
                if player.shooting :
                    if not player.hitwall :
                        bullet.update()
                        bullet.draw(self.screen)
                        if player_adv.rect.colliderect(bullet) :
                            player.canhit=False
                            player.hitwall=True
                            player_adv.PV-=capa[1]*player.damage_boost*player.powerlift
                            player_adv.i_death=3*self.block
                            if self.rumb :
                                player_adv.joy.rumble(1,1,1000)
                            player.duration_bullet=self.ticks-capa[5]


            elif pers=="Popofox" or pers=="Bubule" or pers=="Furbok" or pers=="Semibot" :
                if player.shooting :
                    for mur in self.murs :
                        if mur.colliderect(bullet) :
                            player.shooting=False
                            player.hitwall=True
                            player.duration_bullet=self.ticks-capa[5]
                    if not player.hitwall :
                        bullet.update()
                        bullet.draw(self.screen)
                        if player_adv.rect.colliderect(bullet) :
                            player.canhit=False
                            player.hitwall=True
                            player_adv.PV-=capa[1]*player.damage_boost*player.powerlift
                            player_adv.i_death=3*self.block
                            if self.rumb :
                                player_adv.joy.rumble(1,1,1000)
                            player.duration_bullet=self.ticks-capa[5]

            elif pers=="Spookie" :
                if not player.explosion :
                    player.explosion=True
                    player.time_effect=self.ticks
                    self.cookie_pos.center=player.rect.center
                if self.ticks-player.time_effect<300 :
                    #self.screen.blit(self.cookie, self.cookie_pos)
                    if player.canhit :
                        if player_adv.rect.colliderect(self.cookie_pos) :
                            player.canhit=False
                            player_adv.PV-=capa[1]*player.damage_boost*1.2*player.powerlift
                            player_adv.i_death=3*self.block
                            if self.rumb :
                                player_adv.joy.rumble(1,1,1000)
                if player.shooting :
                    
                    for mur in self.murs :
                        if mur.colliderect(bullet) :
                            player.shooting=False
                            player.hitwall=True
                            player.duration_bullet=self.ticks-capa[5]
                    if not player.hitwall :
                        bullet.update()
                        bullet.draw(self.screen)
                        if player_adv.rect.colliderect(bullet) :
                            player.hitwall=True
                            player_adv.PV-=capa[1]*player.damage_boost*player.powerlift
                            player_adv.i_death=3*self.block
                            if self.rumb :
                                player_adv.joy.rumble(1,1,1000)
                            player.duration_bullet=self.ticks-capa[5]

            elif pers=="Mushy" :
                if player.shooting :
                    for mur in self.murs :
                        if mur.colliderect(bullet) :
                            player.shooting=False
                            player.hitwall=True
                            player.duration_bullet=self.ticks-capa[5]
                    if not player.hitwall :
                        bullet.update()
                        bullet.draw(self.screen)
                        if player_adv.rect.colliderect(bullet) :
                            player.canhit=False
                            player.hitwall=True
                            player_adv.PV-=capa[1]*player.damage_boost*player.powerlift
                            player_adv.i_death=3*self.block
                            if self.rumb :
                                player_adv.joy.rumble(1,1,1000)
                            player.duration_bullet=self.ticks-capa[5]
                            player.time_effect=self.ticks
                            self.ticks_poison=[int(self.ticks/1000), self.ticks%1000]

                if self.ticks-player.time_effect<4000 :
                    player_adv.modif=-1
                    if self.ticks_poison[0]!=int((self.ticks-self.ticks_poison[1])/1000) :
                        self.ticks_poison[0]+=1
                        player_adv.PV-=capa[1]*player.damage_boost/4
                        player_adv.i_death=1*self.block
                        if self.rumb :
                            player_adv.joy.rumble(1,1,500)
                    player.one_time=False
                else :
                    if not player.one_time :
                        player.one_time=True
                        player_adv.modif=1

            
            elif pers=="Chick'n bob" :
                if player.shooting :
                    for mur in self.murs :
                        if mur.colliderect(bullet) :
                            player.shooting=False
                            player.hitwall=True
                            player.duration_bullet=self.ticks-capa[5]
                    if not player.hitwall :
                        bullet.update()
                        bullet.draw(self.screen)
                        if player_adv.rect.colliderect(bullet) :
                            player.canhit=False
                            player.hitwall=True
                            percent=min(max((self.ticks - player.duration_bullet)/(capa[5])+10/100, 25/100),1)*37/100
                            player_adv.PV-=percent*player_adv.capa[0]*player.damage_boost*player.powerlift
                            player_adv.i_death=8*percent*self.block #un peu moin de 3*3(8) car 3 de base et 3 pour 37*3=100%
                            if self.rumb :
                                player_adv.joy.rumble(1,1,1000)
                            player.duration_bullet=self.ticks-capa[5]

            elif pers=="Owleaf" :
                if player.shooting :
                    temp=0
                    for mur in self.murs :
                        for x in range(len(bullet.rect)) :
                            if mur.colliderect(bullet.rect[x]) :
                                bullet.dagues[x]=False
                                if not bullet.dagues[x]:
                                    temp+=1
                    if temp>=3 :
                        player.shooting=False
                        player.hitwall=True
                        player.duration_bullet=self.ticks-capa[5]
                
                    if not player.hitwall :
                        bullet.updateowl()
                        bullet.drawowl(self.screen)
                        for x in range(len(bullet.rect)) :
                            if bullet.dagues[x] :
                                if player_adv.rect.colliderect(bullet.rect[x]) and player.canhit[x]:
                                    player.canhit[x]=False
                                    player_adv.i_death=3*self.block
                                    if self.rumb :
                                        player_adv.joy.rumble(1,1,1000)     
                                    if bullet.power[x]==0 :
                                        player.PV+=capa[1]*player.damage_boost*0.2*player.powerlift
                                        player_adv.PV-=capa[1]*player.damage_boost*player.powerlift
                                    elif bullet.power[x]==2 :
                                        player_adv.PV-=capa[1]*player.damage_boost*1.2*player.powerlift
                                    else :
                                        player_adv.PV-=capa[1]*player.damage_boost*player.powerlift
                                        player.ammo+=1


            elif pers=="Squeak" :
                if player.shooting :
                    bullet.updatex()
                    collision=False
                    for mur in self.murs :
                        if mur.colliderect(bullet) :
                            collision=True
                    if collision :
                        bullet.x=-bullet.x
                        bullet.updatex()
                        if player.range<310 :
                            player.range+=100
                        

                    
                    bullet.updatey()
                    collision=False
                    for mur in self.murs :
                        if mur.colliderect(bullet) :
                            collision=True
                    if collision :
                        bullet.y=-bullet.y
                        bullet.updatey()
                        if player.range<310 :
                            player.range+=100
                    if not player.hitwall :
                        bullet.draw(self.screen)
                        if player_adv.rect.colliderect(bullet) :
                            player.canhit=False
                            player.hitwall=True
                            player_adv.PV-=capa[1]*player.damage_boost*player.powerlift
                            player_adv.i_death=3*self.block
                            if self.rumb :
                                player_adv.joy.rumble(1,1,1000)
                            player.duration_bullet=self.ticks-capa[5]


            elif pers=="Zipit" :
                if player.shooting :
                    for mur in self.murs :
                        if mur.colliderect(bullet) :
                            player.shooting=False
                            player.hitwall=True
                            player.duration_bullet=self.ticks-capa[5]
                            
                    if not player.hitwall :
                        bullet.update()
                        bullet.draw(self.screen)
                        if player_adv.rect.colliderect(bullet) :
                            percent=max((self.ticks - player.duration_bullet)/(capa[5]*2),10/100)*10
                            player_adv.PV-=capa[1]/percent*player.damage_boost*player.powerlift

                            player.canhit=False
                            player.hitwall=True
                            #player_adv.PV-=capa[1]*player.damage_boost*player.powerlift
                            player_adv.i_death=1/percent*3*self.block
                            if self.rumb :
                                player_adv.joy.rumble(1,1,1000)
                            player.duration_bullet=self.ticks-capa[5]
                            player.time_effect=self.ticks
                            """#pull
                            x=0
                            ok=True
                            while x<6 and ok :
                                x+=1
                                player_adv.move_x(player_adv.x1-bullet.x*1.5)
                                player_adv.move_y(player_adv.y1-bullet.y*1.5)

                                for mur in self.murs + self.waters :
                                    if player_adv.rect.colliderect(mur) :
                                        ok=False

                            player_adv.unmove_x(player_adv.tx1)
                            player_adv.unmove_y(player_adv.ty1)"""

                if self.ticks-player.time_effect<120 :
                    ok=True
                    player_adv.x1-=bullet.x*0.8
                    player_adv.y1-=bullet.y*0.8
                    player_adv.move_x(player_adv.x1)
                    player_adv.move_y(player_adv.y1)
                    for mur in self.murs + self.waters :
                        if player_adv.rect.colliderect(mur) :
                            ok=False
                    if not ok :
                        player_adv.unmove_x(player_adv.tx1)
                        player_adv.unmove_y(player_adv.ty1)
            
            elif pers=="Chauss-être" :
                self.smelt_pos.center=player.rect.center
                
                if player_adv.rect.colliderect(self.smelt_pos) :
                    player_adv.slow=0.8
                    player_adv.PV-=capa[1]*player.damage_boost*player.powerlift
                    player_adv.i_death=1.5*self.block
                    if self.rumb :
                        player_adv.joy.rumble(0.5,0.5,1000)
                else :
                    player_adv.slow=1
                if player.shooting :
                    if not player.hitwall :
                        player.x1+=bullet.x
                        player.y1+=bullet.y
                        player.move_x(player.x1)
                        player.move_y(player.y1)
                        
                    for mur in self.murs + self.waters:
                        if mur.colliderect(player.rect):
                            player.shooting=False
                            player.hitwall=True
                            player.duration_bullet=self.ticks-capa[5]
                            player.unmove_x(player.tx1)
                            player.unmove_y(player.ty1)
                    if player.rect.x<0 or player.rect.y<0 or player.rect.x>WIDTH-self.block or player.rect.y>HEIGHT-self.block :
                        player.shooting=False
                        player.hitwall=True
                        player.duration_bullet=self.ticks-capa[5]
                        player.unmove_x(player.tx1)
                        player.unmove_y(player.ty1)

            elif pers=="Paper Dukook" :
                if player.shooting :
                    for mur in self.murs :
                        if mur.colliderect(bullet) :
                            player.shooting=False
                            player.hitwall=True
                            player.duration_bullet=self.ticks-capa[5]
                    if not player.hitwall :
                        bullet.update()
                        bullet.draw(self.screen)
                        if player_adv.rect.colliderect(bullet) :
                            player.canhit=False
                            player.hitwall=True
                            k_damage=1
                            if self.n==0 :
                                player.PV+=60   
                                player.ammo+=1 
                            elif self.n==1 :
                                k_damage=1.2
                            elif self.n==2 :
                                player.time_effect=self.ticks
                                k_damage=0.5
                            elif self.n==3 :
                                if randint(1,10)==1 :
                                    k_damage=5
                                else :
                                    k_damage=0
                            elif self.n==4 :
                                player.powerlift=round(player.powerlift*1.1, 1)
                                player_adv.powerlift=round(player_adv.powerlift*0.9,1)
                            elif self.n==5 :
                                k_damage=1.8
                            elif self.n==6 :
                                player.PV+=200   
                                player.ammo+=2
                            elif self.n==7 :
                                k_damage=2.5

                            player_adv.PV-=capa[1]*player.damage_boost*player.powerlift*k_damage
                            player_adv.i_death=3*self.block
                            if self.rumb :
                                player_adv.joy.rumble(1,1,1000)
                            player.duration_bullet=self.ticks-capa[5]
                            
                                

                if self.ticks-player.time_effect<1400 :
                    player_adv.modif=0
                    if self.rumb :
                        player.joy.rumble(1,1,1)
                    player.one_time=False
                else :
                    if not player.one_time :
                        player_adv.modif=1  
                        player.one_time=True

            elif pers=="MiraDraco" :
                if player.shooting :
                    for mur in self.murs :
                        if mur.colliderect(bullet) :
                            player.shooting=False
                            player.hitwall=True
                            player.duration_bullet=self.ticks-capa[5]
                    if not player.hitwall :
                        bullet.update()
                        bullet.draw(self.screen)
                        if player_adv.rect.colliderect(bullet) :
                            player.canhit=False
                            player.hitwall=True
                            player_adv.PV-=capa[1]*player.damage_boost*player.powerlift
                            player_adv.i_death=3*self.block
                            if self.rumb :
                                player_adv.joy.rumble(1,1,1000)
                            player.duration_bullet=self.ticks-capa[5]

                if self.ticks-player.time_effect<700 :
                    player.modif=0
                    if self.rumb :
                        player.joy.rumble(1,1,1)
                    player.one_time=False
                else :
                    if not player.one_time :
                        player.modif=1  
                        player.one_time=True

            elif pers=="Pyroxis" :
                if player.shooting :
                    for mur in self.murs :
                        if mur.colliderect(bullet) :
                            player.shooting=False
                            player.hitwall=True
                            player.duration_bullet=self.ticks-capa[5]
                    if not player.hitwall :
                        bullet.update()
                        bullet.draw(self.screen)
                        if player_adv.rect.colliderect(bullet) :
                            player.canhit=False
                            player.hitwall=True
                            percent=1+0.01/(max(player.PV/capa[0], 0.01))
                            player_adv.PV-=capa[1]*percent*player.damage_boost*player.powerlift
                            player_adv.i_death=3*self.block
                            if self.rumb :
                                player_adv.joy.rumble(1,1,1000)
                            player.duration_bullet=self.ticks-capa[5]
                            player.flames+=round(capa[1]*percent*player.damage_boost/1.5,1)
                            self.ticks_flammes=[int(self.ticks/1000), self.ticks%1000]

                if player.flames>0 :
                    if self.ticks_flammes[0]!=int((self.ticks-self.ticks_flammes[1])/1000) :
                        self.ticks_flammes[0]+=1
                        damage_f=max(round(player.flames/3,1), 15)
                        player_adv.PV-=damage_f
                        player.flames=round(player.flames-damage_f, 1)
                        if player.flames<0 :
                            player.flames=0
                        player_adv.i_death=1*self.block
                        if self.rumb :
                            player_adv.joy.rumble(0.7,0.7,500)

            elif pers=="..." :
                if player.shooting :
                    for mur in self.murs :
                        if mur.colliderect(bullet) :
                            player.shooting=False
                            player.hitwall=True
                            player.duration_bullet=self.ticks-capa[5]
                    if not player.hitwall :
                        bullet.update()
                        bullet.draw(self.screen)
                        if player_adv.rect.colliderect(bullet) :
                            player.canhit=False
                            player.hitwall=True
                            player_adv.PV-=capa[1]*player.damage_boost*player.powerlift
                            player_adv.i_death=3*self.block
                            if self.rumb :
                                player_adv.joy.rumble(1,1,1000)
                            player.duration_bullet=self.ticks-capa[5]
                            player.time_effect=self.ticks

                if self.ticks-player.time_effect<1200 :
                    player_adv.mute=0
                else :
                    player_adv.mute=1                    

            elif pers=="UIIA" :
                if player.shooting :
                    if not player.hitwall :
                        bullet.update()
                        bullet.draw(self.screen)
                        if player_adv.rect.colliderect(bullet) :
                            player.canhit=False
                            player.hitwall=True
                            player_adv.PV-=capa[1]*player.damage_boost
                            player_adv.i_death=3*self.block
                            if self.rumb :
                                player_adv.joy.rumble(1,1,1000)
                            player.duration_bullet=self.ticks-capa[5]
                            player.time_effect=self.ticks

                if self.ticks-player.time_effect<5000 :
                    player_adv.modif=0
                    if self.rumb :
                        player_adv.joy.rumble(1,1,1)
                        player.one_time=False
                else :
                    if not player.one_time :
                        player_adv.modif=1  
                        player.one_time=True
                    
    def display(self) :
        #écran fond noire
        
        self.screen.blit(self.background, (0,0))


        
        if self.plan=="play" :
            
            if self.pers=="Berry" :
                self.screen.blit(self.ice, self.ice_pos)
            elif self.pers2=="Berry" :
                self.screen.blit(self.ice, self.ice_pos)

            if self.pers=="Spookie" :
                if self.ticks-self.player.time_effect<300 :
                    self.screen.blit(self.cookie, self.cookie_pos)
            elif self.pers2=="Spookie" :
                if self.ticks-self.player2.time_effect<300 :
                    self.screen.blit(self.cookie, self.cookie_pos)

            if self.pers=="Chauss-être" or self.pers2=="Chauss-être" :
                self.screen.blit(self.smelt, self.smelt_pos)

            if self.player.bool_tp :
                self.screen.blit(self.tp, self.player.tp_pos)
            elif self.player2.bool_tp :
                self.screen.blit(self.tp, self.player2.tp_pos)
            
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
            elif self.map=="CG" :
                self.screen.blit(self.CG, (0,0))
            else :
                self.screen.blit(self.ZG, (0,0))
            
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
            self.screen.blit(font.render(pseudo_P1, True, (255, 255, 255)), (100, 10))
            t=font.render(pseudo_P2, True, (255, 255, 255))
            self.screen.blit(t, (WIDTH-110-t.get_width(), 10))
            t=font.render(self.name_event, True, (255, 255, 255))
            self.screen.blit(t, (WIDTH/2-t.get_width()/2, 10))

            if self.emt :
                self.screen.blit(self.down, (self.player.x1-self.block/2, self.player.y1-self.block/2))
            if self.emt2 :
                self.screen.blit(self.down, (self.player2.x1-self.block/2, self.player2.y1-self.block/2))
            

            #bullet
            """if self.shooting[0] :
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
                self.a_surge.draw(self.screen)"""
            

        elif self.plan=="end" :

            if self.winner=="blue" :
                t=font.render(pseudo_P1, True, (255, 255, 255))
                self.screen.blit(t, (400-t.get_width()/2, 10))
            elif self.winner=="green" :
                t=font.render(pseudo_P2, True, (255, 255, 255))
                self.screen.blit(t, (400-t.get_width()/2, 10))

            

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
            
                        
            self.screen.blit(font.render(pseudo_P1, True, (255, 255, 255)), (100, 10))
            t=font.render(pseudo_P2, True, (255, 255, 255))
            self.screen.blit(t, (800-110-t.get_width(), 10))
            
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
        
    def run(self) :
        while self.running :
            self.event()
            self.update()
            self.display()
            self.updraw_bullet(self.pers, self.player, self.player2, self.bullet_P1, self.capa)
            self.updraw_bullet(self.pers2, self.player2, self.player, self.bullet_P2, self.capa2)
            pygame.display.flip()
            
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