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

player = newplayer("Rouxhero")
db = load_img()
db_inv = load_img_inv()
fps = pygame.time.Clock()
fps.tick()


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


def inven():
	surface.fill((0, 0, 0))
	draw_inv()
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
			if event.key == pygame.K_UP:
				x, y = player.cases(0, 0)
				if not mapsc[y][x] in allow:
					player.up()
			if event.key == pygame.K_DOWN:
				x, y = player.cases(0, 64)
				if not mapsc[y][x] in allow:
					player.down()
			if event.key == pygame.K_LEFT:
				x, y = player.cases(-16, 0)
				if not mapsc[y][x] in allow:
					player.left()
			if event.key == pygame.K_RIGHT:
				x, y = player.cases(64, 0)
				if not mapsc[y][x] in allow:
					player.right()
			if event.key == pygame.K_RETURN:
				i = i * -1
	if i == 1:
		game()
	elif i == -1:
		inven()
