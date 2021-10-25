# coding: utf-8 
from Tkinter import *
import pygame
from pygame.locals import *
from module import *
from map import *
from math import tan
root = Tk()
scale = int(root.winfo_screenheight()/8)
root.destroy()
angle = 30
x_player = scale
y_player = scale
x_coef,y_coef = 0,1
vitesse = 10
db1,db2 =load_image()
db = new_scale(db1,db2,scale)
player = db[9]
map_1 = map1()
map_1_cover = map1_cover()
def draw_map(map):
    for i in range (len(map)):
        for ii in range(len(map[0])):
            surface.blit(db[map[i][ii]],(ii*scale,i*scale))
def draw_map_cover(map):
    for i in range (len(map)):
        for ii in range(len(map[0])):
            if map[i][ii] != 0 :
            	surface.blit(db[map[i][ii]],(ii*scale,i*scale))

surface = pygame.display.set_mode((8*scale,6*scale))

pygame.key.set_repeat(400, 30)

continu = True
while continu :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continu = True
            pygame.quit()
            quit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
            	if  x_player+(x_coef*vitesse) > 0 and  x_player+(x_coef*vitesse)< 7*scale :
            		if  y_player+(y_coef*vitesse) > 0 and  y_player+(y_coef*vitesse)< 5*scale :
            			x_player,y_player = x_player+(x_coef*vitesse),y_player+(y_coef*vitesse)
            			
            if event.key == K_UP:
                player = tourner(db[9],180)
                y_coef = -1
                x_coef = 0
            if event.key == K_DOWN:
                player = tourner(db[9],0)
                y_coef = 1
                x_coef = 0
            if event.key == K_LEFT:
                player = tourner(db[9],270)
                x_coef = -1
                y_coef = 0
            if event.key == K_RIGHT:
                player = tourner(db[9],90)
                x_coef = 1
                y_coef = 0
    draw_map(map_1)
    surface.blit(player,(x_player,y_player))
    pygame.display.update()
