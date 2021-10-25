import pygame
from pygame.locals import *

pygame.init()
surface = pygame.display.set_mode((700, 600))
pygame.key.set_repeat(400, 30)


def drawn_particul():
	surface.fill((0,0,0))
	for i in player.part :
		surface.blit(i[0],i[1])

class jeux():
	def __init__(self):
		self.sand = pygame.Surface((4, 4))
		self.sand.fill((115,102,105))
		self.part = [[self.sand,(10,10)]]
		self.put = 0
		self.gravite = 5
		self.fps = 150
	def gravity(self):	
		for i in self.part :
			i[1] = (i[1][0] ,i[1][1] + self.gravite)
	def destroy(self):
		for i in self.part :
			if i[1][1] > 586:
				self.part.pop(self.part.index(i))
		
player = jeux()
continu = True
PartType = player.sand
while continu:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			continu = False
			exit()
		if event.type == MOUSEMOTION and event.buttons[0] == 1:
			player.part.append([PartType,(event.pos[0],event.pos[1])])
	player.gravity()
	player.destroy()
	drawn_particul()
	pygame.time.Clock().tick(player.fps)
	# print(player.part)
	pygame.display.update()