import sys
import random
import pygame
from pygame.locals import *
from pygame.color import *
import math
import pymunk
from pymunk.vec2d import Vec2d
import pymunk.pygame_util


run1r = pygame.image.load('stick-sprite/run1.png')
run2r = pygame.image.load('stick-sprite/run2.png')
run3r = pygame.image.load('stick-sprite/run3.png')
run4r = pygame.image.load('stick-sprite/run4.png')
run5r = pygame.image.load('stick-sprite/run5.png')

run1l = pygame.image.load('stick-sprite/run1l.png')
run2l = pygame.image.load('stick-sprite/run2l.png')
run3l = pygame.image.load('stick-sprite/run3l.png')
run4l = pygame.image.load('stick-sprite/run4l.png')
run5l = pygame.image.load('stick-sprite/run5l.png')

static = pygame.image.load('stick-sprite/Static.png')

jump0l = pygame.image.load('stick-sprite/jump0l.png')
jump0r = pygame.image.load('stick-sprite/jump0.png')
jump1l = pygame.image.load('stick-sprite/jump1l.png')
jump1r = pygame.image.load('stick-sprite/jump1.png')

kick0l = pygame.image.load('stick-sprite/kick0l.png')
kick0r = pygame.image.load('stick-sprite/kick0.png')
kickr = pygame.image.load('stick-sprite/kick.png')
kickl = pygame.image.load('stick-sprite/kickl.png')

coup0r = pygame.image.load('stick-sprite/coup00.png')
coupr = pygame.image.load('stick-sprite/coup0.png')
coup0l = pygame.image.load('stick-sprite/coup00l.png')
coupl = pygame.image.load('stick-sprite/coup0l.png')

boulev =  pygame.image.load('stick-sprite/boule.png')

fond =  pygame.image.load('stick-sprite/fond.jpg')


"""Class Deplacement()
    def __init__(self):
        pass"""







class Jeu():
    jump=True
    jump1=True
    pygame.init()
    running = True
    width, height = 1750,1000
    fps=60
    black=[0,0,0]
    white=[250,250,250]
    x1=50
    y1=800
    
    x2=50
    y2=50
    cpt_anime=0
    se_deplace=False 
    Right=False 
    saut=(0,100)

    jump_anime=False
    cpt_jump=0
    charge_saut=False
    cpt_kick=1
    kick=False
    charge_kick=False
    kick_pwr=0
    poing=False
    cpt_poing=0
    ######################################################################""
    cpt_anime1=0
    se_deplace1=False 
    Right1=False 
    saut1=(0,100)

    jump_anime1=False
    cpt_jump1=0
    charge_saut1=False
    cpt_kick1=1
    kick1=False
    charge_kick1=False
    kick_pwr1=0
    poing1=False
    cpt_poing1=0


    

    def __init__(self):



        self.Main()
    def add_personnage(self,space,x,y):
        mass =1
        radius =3
        moment = pymunk.moment_for_circle(mass, 1, radius) # 1
        body = pymunk.Body(mass, moment) # 2
        x = 0
        y=300
        body.position = x, y # 3
    
        shape = pymunk.Circle(body, radius) # 4
        
        shape.elasticity=0
        
        space.add(body, shape) # 5
        
        return shape

    def add_ball(self,space):
        mass = 1
        radius = 20
        
        moment = pymunk.moment_for_circle(mass, 1, radius) # 1
        body = pymunk.Body(mass, moment) # 2
        x = 500
        y=600
        body.position = x, y # 3
    
        shape = pymunk.Circle(body, radius) # 4
        
        shape.elasticity=0.9
        
        space.add(body, shape) # 5
        
        return shape

    def add_segment(self,space,vertice):
        mass=1000
        radius=16
        moment = pymunk.moment_for_segment(mass,(0,0),(0,10),radius)
        body = pymunk.Body(mass, moment)
        
        shape = pymunk.Poly(body,vertice,None,radius)
    
        shape.elasticity=0.9
        
        
        space.add(shape)
        
        return shape
    def add_tete(self,space):
        mass = 1000
        radius = 20
        
        moment = pymunk.moment_for_circle(mass, 1, radius) # 1
        body = pymunk.Body(mass, moment) # 2
        x = 500
        y=900
        body.position = x, y # 3
    
        shape = pymunk.Circle(body, radius) # 4
        
        shape.elasticity=0.9
        
        space.add(shape) # 5
        
        return shape
    def puissance_saut(self,cpt_jump,saut):
        if cpt_jump<1200:
            cpt_jump+=200
        elif cpt_jump<2200 and cpt_jump>=1200:
            cpt_jump+=15
        saut=(0,cpt_jump)
        return saut,cpt_jump

    def animation_jump(self,screen,Right,x,y):
        
        if Right:
            
            
            screen.blit(jump1r,(x,y))
        else:
            
            
            screen.blit(jump1l,(x,y))


    def deplace(self,screen,poing,charge_kick,kick,se_deplace,Right,x,y,jump_anime,charge_saut,cpt_anime,cpt_poing):
        if charge_saut and not jump_anime:
            if Right:
                screen.blit(jump0r,(x,y))
            else:
                screen.blit(jump0l,(x,y))

        elif charge_kick :
            if Right:
                screen.blit(kick0r,(x,y))
            else:
                screen.blit(kick0l,(x,y))
        
        elif kick and not charge_kick:
            if Right:
                screen.blit(kickr,(x,y))
            else:
                screen.blit(kickl,(x,y))
        elif poing:

            cpt_poing+=1
            if cpt_poing>10:
                cpt_poing=0
                poing=False
            if Right:
                if cpt_poing<5:
                    screen.blit(coup0r,(x,y))
                else:
                    screen.blit(coupr,(x,y))
                if se_deplace:
                    x+=8
            else:
                if cpt_poing<5:
                    screen.blit(coup0l,(x,y))
                else:
                    screen.blit(coupl,(x,y))
                if se_deplace:
                    x-=8

        else:

            if not se_deplace and not jump_anime:
                screen.blit(static,(x,y))
            elif not se_deplace and jump_anime:
                self.animation_jump(screen,Right,x,y)
            else:
                if Right and not jump_anime:
                    x+=8
                    cpt_anime+=9
                    if cpt_anime<50:
                        screen.blit(run1r,(x,y))
                    elif cpt_anime<100 and cpt_anime>=50:
                        screen.blit(run2r,(x,y))
                    elif cpt_anime<150 and cpt_anime>=100:
                        screen.blit(run3r,(x,y))
                    elif cpt_anime<200 and cpt_anime>=150:
                        screen.blit(run4r,(x,y))
                    elif cpt_anime<250 and cpt_anime>=200:
                        screen.blit(run5r,(x,y))
                    
                    if cpt_anime>=240:
                        cpt_anime=0
                    
                elif not Right and not jump_anime:
                    x-=8
                    
                    cpt_anime+=9
                    if cpt_anime<50:
                        screen.blit(run1l,(x,y))
                    elif cpt_anime<100 and cpt_anime>=50:
                        screen.blit(run2l,(x,y))
                    elif cpt_anime<150 and cpt_anime>=100:
                        screen.blit(run3l,(x,y))
                    elif cpt_anime<200 and cpt_anime>=150:
                        screen.blit(run4l,(x,y))
                    elif cpt_anime<250 and cpt_anime>=200:
                        screen.blit(run5l,(x,y))
                    
                    if cpt_anime>=240:
                        cpt_anime=0
                elif Right and jump_anime:
                    x+=8
                    self.animation_jump(screen,Right,x,y)
                elif not Right and jump_anime:
                    x-=8
                    self.animation_jump(screen,Right,x,y)
        return x,y,cpt_anime,cpt_poing,poing
    def Main(self):
        
        # PyGame init
        tps0=0
        tps00=0
        screen = pygame.display.set_mode((self.width,self.height)) 
        clock = pygame.time.Clock()
        
        # Physics stuff
        space = pymunk.Space()   
        space.gravity = 0,-2500
    
        draw_options = pymunk.pygame_util.DrawOptions(screen)
        j1=self.add_personnage(space,self.x1,self.y1)
        j2=self.add_personnage(space,self.x2,self.y2)
        sol = pymunk.Segment(space.static_body, (50, 80), (1750, 70), 80)
        sol.elasticity=0.7
        sol.friction=0.7
        space.add(sol)       
        

        tete=self.add_tete(space)
        tete1=self.add_tete(space)
        cotés= [pymunk.Segment(space.static_body, (0, 50), (0, 1000), 20)
                ,pymunk.Segment(space.static_body, (1750, 50), (1750, 1000), 20)
                ,pymunk.Segment(space.static_body, (50, 1020), (1750, 1020), 20)
                ]  
        space.add(cotés)
        for coté in cotés:
            coté.elasticity=0.9
        
        boule=self.add_ball(space)
        boule.friction=0.5

        ver_corp=[(0,-0),(0,10),(-0,-50)]
        corp= self.add_segment(space,ver_corp)
        corp1=self.add_segment(space,ver_corp)
        
        

        while self.running:
            """ screen.fill(self.white)"""
            clock.tick(self.fps)
            keys = pygame.key.get_pressed()

            

            for event in pygame.event.get():
                if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:  
                    self.running = False
            ########################################j1
            self.se_deplace=False
            self.charge_saut=False



            if self.kick:
                self.cpt_kick+=1

            if self.cpt_kick>=15:
                self.cpt_kick=0
                self.kick=False

            self.charge_kick=False
            

            if  keys[pygame.K_s] :
                self.charge_kick=True
                if self.kick_pwr<60:
                    self.kick_pwr+=1


            elif not keys[pygame.K_s]:

                if keys[pygame.K_d]:
                    self.se_deplace=True
                    self.Right=True

                if keys[pygame.K_q]:
                    self.se_deplace=True
                    self.Right=False

                if event.type == KEYDOWN and keys[pygame.K_z]:
                    self.charge_saut=True
                    self.saut,self.cpt_jump= self.puissance_saut(self.cpt_jump,self.saut)
                if event.type == KEYUP and keys[pygame.K_z] and self.jump:

                    j1.body.apply_impulse_at_world_point(self.saut,j1.body.position)
                    self.cpt_jump=200

                if (keys[pygame.K_a] or keys[pygame.K_e]) and tps0<(pygame.time.get_ticks()-500):
                    tps0=pygame.time.get_ticks()
                    self.poing=True
            if  event.type == KEYUP and keys[pygame.K_s] and not event.type==KEYDOWN:

                self.kick=True

                w1,z1=boule.body.position
                
                angle = (abs(z1-1000)-self.y1-40)*2


                vecr=(40*self.kick_pwr,angle*self.kick_pwr)
                vecl=(-40*self.kick_pwr,angle*self.kick_pwr)
                if self.Right:
                    if w1 < self.x1+130 and w1 >self.x1+50 and z1< abs(self.y1-1000) and z1>abs(self.y1-1000)-100:

                        boule.body.apply_impulse_at_world_point(vecr,boule.body.position)
                else:
                    if w1 < self.x1 and w1 >self.x1-80 and z1< abs(self.y1-1000)+50 and z1>abs(self.y1-1000)-100:

                        boule.body.apply_impulse_at_world_point(vecl,boule.body.position)
                self.kick_pwr=4
                

            
            
            
            
            if self.y1 > 720:
                self.jump=True
            else :
                self.jump=False
            
            #si il ne peut pas sauter c'est qu'il est en saut 
            self.jump_anime = not self.jump

            #####################################j2
            self.se_deplace1=False
            self.charge_saut1=False



            if self.kick1:
                self.cpt_kick1+=1

            if self.cpt_kick1>=15:
                self.cpt_kick1=0
                self.kick1=False

            self.charge_kick1=False
            

            if  keys[pygame.K_KP2] :
                self.charge_kick1=True
                if self.kick_pwr1<60:
                    self.kick_pwr1+=1


            elif not keys[pygame.K_KP2]:

                if keys[pygame.K_KP3]:
                    self.se_deplace1=True
                    self.Right1=True

                if keys[pygame.K_KP1]:
                    self.se_deplace1=True
                    self.Right1=False

                if event.type == KEYDOWN and keys[pygame.K_KP5]:
                    self.charge_saut1=True
                    self.saut1,self.cpt_jump1= self.puissance_saut(self.cpt_jump1,self.saut1)
                if event.type == KEYUP and keys[pygame.K_KP5] and self.jump1:

                    j2.body.apply_impulse_at_world_point(self.saut1,j2.body.position)
                    self.cpt_jump1=200

                if (keys[pygame.K_KP4] or keys[pygame.K_KP6]) and tps00<(pygame.time.get_ticks()-500):
                    tps00=pygame.time.get_ticks()
                    self.poing1=True
            if  event.type == KEYUP and keys[pygame.K_KP2] and not event.type==KEYDOWN:

                self.kick1=True

                w1,z1=boule.body.position
                
                angle = (abs(z1-1000)-self.y2-40)*2


                vecr=(40*self.kick_pwr1,angle*self.kick_pwr1)
                vecl=(-40*self.kick_pwr1,angle*self.kick_pwr1)
                if self.Right1:
                    if w1 < self.x2+130 and w1 >self.x2+50 and z1< abs(self.y2-1000) and z1>abs(self.y2-1000)-100:

                        boule.body.apply_impulse_at_world_point(vecr,boule.body.position)
                else:
                    if w1 < self.x2 and w1 >self.x2-80 and z1< abs(self.y2-1000)+50 and z1>abs(self.y2-1000)-100:

                        boule.body.apply_impulse_at_world_point(vecl,boule.body.position)
                self.kick_pwr1=4
                

            
            
            
            
            if self.y2 > 720:
                self.jump1=True
            else :
                self.jump1=False
            
            #si il ne peut pas sauter c'est qu'il est en saut 
            self.jump_anime1 = not self.jump1
            ##############""
           
                
            space.debug_draw(draw_options)
            dt = 1./self.fps
            space.step(dt)
            
            
            
            #hitbox
            a,b=j1.body.position
            self.y1=abs(b-880)
            j1.body.position=(self.x1+20,b-5)
            tete.body.position=(self.x1+25,abs(self.y1-1000)-17)
            corp.body.position=(self.x1+30,abs(self.y1-1000)-65)

            a,b=j2.body.position
            self.y2=abs(b-880)
            j2.body.position=(self.x2+20,b-5)
            tete1.body.position=(self.x2+25,abs(self.y2-1000)-17)
            corp1.body.position=(self.x2+30,abs(self.y2-1000)-65)





            v,w=boule.body.position
            screen.blit(fond,(0,0))
            screen.blit(boulev,(v-15,abs(w-1000)-15))





            self.x1,self.y1,self.cpt_anime,self.cpt_poing,self.poing=self.deplace(screen,self.poing,self.charge_kick,self.kick,self.se_deplace,self.Right,self.x1,self.y1,self.jump_anime,self.charge_saut,self.cpt_anime,self.cpt_poing)


            self.x2,self.y2,self.cpt_anime1,self.cpt_poing1,self.poing1=self.deplace(screen,self.poing1,self.charge_kick1,self.kick1,self.se_deplace1,self.Right1,self.x2,self.y2,self.jump_anime1,self.charge_saut1,self.cpt_anime1,self.cpt_poing1)


            
            
            pygame.display.flip()
class Goal():
    def __init__(self):
        pass
    @staticmethod
    def funcname(parameter_list):
        pass
Jeu()