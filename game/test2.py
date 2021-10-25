# -*- coding: utf-8 -*-
 
import pygame
from pygame.locals import *
from Tkinter import *
from random import randint as r
root = Tk()
screenW = int(root.winfo_screenwidth()/2)
root.destroy()
scale = int(screenW/14)
surface = pygame.display.set_mode([scale*14,scale*15])
pygame.key.set_repeat(400, 30)
pygame.font.init()
font=pygame.font.Font(None, scale)


bg = (  13,113,15)
wall = (  83, 0,   0)
outs = ((0,0,0))
play= (5, 5,  255)
gravite = scale*0.5
mx = 0
key = 0
levels = 0
x, y = scale, scale
vx,vy = scale ,scale
des = 5

joueur = pygame.Surface((scale, scale))
joueur.fill(play)
mur = pygame.Surface((scale, scale))
mur.fill(wall)
out = pygame.Surface((scale, scale))
out.fill(outs)
out2 = pygame.Surface((scale*0.45, scale*0.15))
out2.fill((0,0,0))
ke = pygame.Surface((scale*0.5, scale*0.25))
ke2 = pygame.Surface((scale*0.5, scale*0.25))
ke.fill((255, 255,   0))
ke2.fill((255, 255,   0))
def gene_level():
    niveau = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],]
    for i in range(0,12):
        ligne = [1,]
        for ii in range(0,12):
        	case = r(0,100)
        	if case <= 25 :
        		ligne.append(1)
        	if case > 25 :
        		ligne.append(0)
        ligne.append(1)
        niveau.append(ligne)
    niveau.append([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
    ok = 0
    while ok == 0:
	    KEYx,KEYy = r(1,13),r(1,13)
	    KK = niveau[KEYy][KEYx]
	    if KK == 0:
	    	niveau[KEYy][KEYx] = 5
	    	ok = 1
    ok = 0
    while ok == 0:
	    KEYx,KEYy = r(1,13),r(1,13)
	    KK = niveau[KEYy][KEYx]
	    if KK == 0:
	    	niveau[KEYy][KEYx] = 2
	    	ok = 1
    return niveau
def level(nb):
	if nb == 0:
		return [
			[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
			[1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1],
			[1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1],
			[1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1],
			[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
			[1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
			[1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
			[1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
			[1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
			[1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
			[1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
			[1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
			[1, 2, 1, 0, 0, 0, 1, 5, 0, 0, 0, 0, 0, 1],
			[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
			] ,  (  83, 0,   0) , 0
	else :
		return gene_level() ,(r(0,255),r(0,255),r(0,255)),0
niveau ,wall,key = level(0)
mur.fill(wall)
def dessiner_niveau(surface, niveau):
	for j in range(0,len(niveau)):
		for i in range (0,14):
			case = niveau[j][i]
			if case == 1:  
				surface.blit(mur, (i*scale,j*scale))
			if case == 2:  
				surface.blit(out, (i*scale,j*scale))
				surface.blit(out2, (i*scale*1.1,j*scale*1.035))
			if case == 5:  
				surface.blit(ke, (i*scale*1.05,j*scale))
continuer = True
while continuer:
	for event in pygame.event.get():
		if event.type == QUIT:
			continuer = False
		if event.type == KEYDOWN:
			if event.key == K_RETURN :
				case = niveau[(y/scale)-1][x/scale]
				if case == 1 and des>0:
					niveau[(y/scale)-1][x/scale] = 0
					des -= 1
			if event.key == K_UP:
				case = niveau[(y-vy)/scale][x/scale] 
				if case != 1 and case!= 4:
					if case == 2 and outs ==  ((0,0,0)) or case == 0 or case == 5:
		   				y -= vy
			if event.key == K_RIGHT :
				case = niveau[y/scale][(x+vx)/scale]
		   		if case != 1 and case != 4 :
		   			if case == 2 and outs ==  ((0,0,0)) or case == 0 or case == 5:
		   				x += vx
		   	if event.key == K_DOWN:
		   		case = niveau[(y+vy)/scale][x/scale]
		   		if case != 1 and case != 4 :
		   			if case == 2 and outs ==  ((0,0,0)) or case == 0 or case == 5:
		   				y += vy 
			if event.key == K_LEFT :
				case = niveau[y/scale][(x-vx)/scale]
		   		if case != 1 and case !=4  :
		   			if case == 2 and outs ==  ((0,0,0)) or case == 0 or case == 5:
		   				x -= vx
	case = niveau[y/scale][x/scale]
	if case == 5 :
		key = 1
	surface.fill(bg)
	if key == 1 :
		outs = ((0,0,0))
		out.fill(outs)
		ke.fill((bg))
	else :
		outs = ((113,65,13))
		out.fill(outs)
		ke.fill((255, 255,   0))
	if case == 2 :
		levels += 1
		niveau ,wall,key = level(levels)
	dessiner_niveau(surface, niveau)
	surface.blit(joueur, (x, y))
	surface.blit(ke2,(scale*0.25,scale*14.25))
	m = font.render(str(key)+"       hit : "+str(des),1,(222,10,10))
	surface.blit(m,(scale,scale*14))
	pygame.display.flip()
 
pygame.quit()