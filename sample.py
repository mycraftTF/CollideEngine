import sys
import pygame as pg
from pygame.locals import *
import numpy as np

import CollideEnginev2 as CE

m1 = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
      [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
      [0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
      [0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0],
      [0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

m2 = [[1,1,1,1,1,1,1,1,1,1],
      [0,0,0,0,0,0,0,0,0,0]]


# Initialize Pygame
pg.init()


FPS = 60
clock = pg.time.Clock()

BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)






size = [200, 200]
space = CE.Space(size[0],size[1])
GameDisplay = pg.display.set_mode(size)
GameDisplay.fill(WHITE)

pg.display.set_caption("Collide Engine v2")

done = False




def pixel(surface, color, pos):
    surface.fill(color, (pos, (1, 1)))
#def pixel(surface, color, pos):
#    pos2 = (pos[0]*10, pos[1]*10)
#    surface.fill(color, (pos, (10, 10)))

def drawCons():
    for x in range (len(space.coord)):
        for y in range (len(space.coord[0])):
            print(space.coord[x][y], end = '')
        print()

def draw_screen():
    GameDisplay.fill(WHITE)
    for x in range (len(space.coord)):
        for y in range (len(space.coord[0])):
            if space.coord[x][y] == 1:
                pixel(GameDisplay, BLUE, (x,y))
            elif space.coord[x][y] == 2:
                pixel(GameDisplay, RED, (x,y))
            elif space.coord[x][y] == 3:
                pixel(GameDisplay, GREEN, (x,y))
        
en1 = CE.Entity(1,20,20,100,100)
#en2 = CE.Entity(2,5,5,20,20)
en2 = CE.Entity2(2,m1,20,20)


space.setEntity(en1)
space.setEntity(en2)

moveVec = CE.Vector(0,0)

wVec = CE.Vector(270,2)
aVec = CE.Vector(180,2)
sVec = CE.Vector(90,2)
dVec = CE.Vector(0,2)

while not done:
    clock.tick(FPS)
    timer = 0

    # Main Event Loop
    for event in pg.event.get():
        if event.type == QUIT:
            done = True
        if event.type == KEYDOWN:
            if event.key == K_w:
                moveVec.addVec(wVec)
            if event.key == K_a:
                moveVec.addVec(aVec)
            if event.key == K_s:
                moveVec.addVec(sVec)
            if event.key == K_d:
                moveVec.addVec(dVec)
        if event.type == KEYUP:
            if event.key == K_w:
                moveVec.addVec(sVec)
            if event.key == K_a:
                moveVec.addVec(dVec)
            if event.key == K_s:
                moveVec.addVec(wVec)
            if event.key == K_d:
                moveVec.addVec(aVec)

    
    en2.move(moveVec)
    

    
    space.setSpace()

    draw_screen()
    #drawCons()

    pg.display.update()

pg.quit()

