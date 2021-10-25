# coding: utf-8
# Main Game Scipte
# Made by LL's Games !
# Dev : Rouxhero
# 26/01/2020

# Import :
import tkinter
import pygame
from pygame.locals import *
from module import *
from mape import *

player = newplayer("Rouxhero")
db = load_img()
db_inv = load_img_inv()
fps = pygame.time.Clock()
fps.tick()

allow,maps,mapsc,mapsc2 = map1()
def draw_map(map):
	for i in range(len(map)):
		for ii in range(len(map[0])):
			surface.blit(db[map[i][ii]], (ii * 64 + 20, i * 64 + 10))


def draw_mapc(map):
	for i in range(len(map)):
		for ii in range(len(map[0])):
			surface.blit(db[map[i][ii]], (ii * 64 + 20, i * 64 + 10))


def draw_inv():
	case = pygame.transform.scale(db_inv[4], (80, 80))
	for ii in range(4):
		for i in range(5):
			surface.blit(case, (i * 90 + 64, ii * 140 + 50))
			surface.blit(
				db_inv[int(player.inv[ii * 5 + i][0])], (i * 95 + 64, ii * 140 + 50)
			)
			if player.inv[ii * 5 + i][1] != 0:
				surface.blit(
					inv_font_draw(str(player.inv[ii * 5 + i][1])),
					(i * 95 + 64, ii * 140 + 140),
				)


def game():
	surface.fill((0, 0, 0))
	draw_map(maps)
	draw_mapc(mapsc)
	surface.blit(player.img, (player.x, player.y))
	draw_mapc(mapsc2)
	fps.tick()
	surface.blit(inv_font_draw(str(int(fps.get_fps()))), (0, 0))

	pygame.display.update()

def maping():
	surface.fill((0, 0, 0))
	fond = pygame.transform.scale(
				pygame.image.load("../img/map.jpeg"), (800, 600)
			)
	surface.blit(fond,(0,0))
	pygame.display.update()

def inven():
	surface.fill((0, 0, 0))
	draw_inv()
	pygame.display.update()

def pausee():
	surface.fill((0, 0, 0))
	curseur = pygame.transform.scale(
				pygame.image.load("../img/p1.png"), (32,32)
			)
	font1 = pygame.font.Font("foot.otf", 100)
	font2 = pygame.font.Font("foot.otf", 50)
	head = font1.render("Pause", False, (255, 255, 255))
	conti = font2.render("Continue", False, (255, 255, 255))
	new = font2.render("New Game", False, (255, 255, 255))
	setting = font2.render("Setting", False, (255, 255, 255))
	exits = font2.render("Exit", False, (255, 255, 255))
	surface.blit(head,(260,40))
	surface.blit(conti,(300,170))
	surface.blit(new,(290,270))
	surface.blit(setting,(310,370))
	surface.blit(exits,(350,470))
	print(pygame.mouse.get_pos())
	if pygame.mouse.get_pos() >= (293, 171) and pygame.mouse.get_pos() <= (527, 217) :
		surface.blit(curseur,(250,170))
	if pygame.mouse.get_pos() >= (284, 273) and pygame.mouse.get_pos() <= (537, 320) :
		surface.blit(curseur,(250,290))
	if pygame.mouse.get_pos() >= (289, 369) and pygame.mouse.get_pos() <= (535, 421) :
		surface.blit(curseur,(250,400))
	if pygame.mouse.get_pos() >= (308, 459) and pygame.mouse.get_pos() <= (473, 515) :
		surface.blit(curseur,(250,480))
	pygame.display.update()
	
pygame.init()
pygame.font.init()

surface = pygame.display.set_mode((800, 600))

pygame.key.set_repeat(400, 30)

continu = True
while continu:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			continu = True
			pygame.quit()
			quit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_z:
				if i == 1:
					x, y = player.cases(0, 0)
					if not mapsc[y][x] in allow:
						player.up()	
			if event.key == pygame.K_s:
				if i == 1:
					x, y = player.cases(0, 64)
					if not mapsc[y][x] in allow:
						player.down()
			if event.key == pygame.K_q:
				x, y = player.cases(-16, 0)
				if not mapsc[y][x] in allow:
					player.left()
			if event.key == pygame.K_d:
				x, y = player.cases(64, 0)
				if not mapsc[y][x] in allow:
					player.right()
			if event.key == pygame.K_RETURN:
				if i == -1 or i==1:
					i = i * -1
			if event.key == pygame.K_m:
				if i == 1:
					i = 2 
				elif i == 2:
					i = 1
			if event.key == pygame.K_p:
				if i == 1:
					i = 3
				elif i == 3:
					i = 1

	if i == 1:
		game()
	elif i == -1:
		inven()
	elif i == 2 :
		maping()
	elif i == 3:
		pausee()
