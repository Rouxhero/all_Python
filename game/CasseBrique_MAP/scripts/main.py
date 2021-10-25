import pygame
from pygame.locals import *
from mod import *

pygame.init()
surface = pygame.display.set_mode((640,840))
pygame.display.set_caption("Casse Brique")

map = NewMap()
map.DoImport()
map.create()
print(map.map)
def draw_map():
	for i in range(8):
		for ii in range(10):
			surface.blit(map.img[map.map[i][ii]],(ii*64,i*64))
			pygame.display.update()
continu = False
while not continu:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			continu = True
	draw_map()
	surface.blit(map.img[4],(80,766))
	pygame.display.update()