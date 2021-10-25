#Class to display info
import threading
import pygame
from pygame.locals import *
from utile import *
from time import sleep as pause
from pop import *
from time import sleep as pause

class Interface(threading.Thread):


	def __init__(self,core):
		threading.Thread.__init__(self)
		pygame.init()
		pygame.font.init()
		self.clock = pygame.time.Clock()
		self.display = pygame.display.set_mode((500,250))
		self.header = pygame.font.Font('../Libs/menu.ttf', 20)
		self.continu = True
		self.core = core

	def run(self):
		while self.continu :
			pause(0.1)
			for event in pygame.event.get():  
					if event.type == QUIT:    
							self.continu = False
							exit()
			self.clock.tick(10)
			self.display.fill((0,0,0))
			self.affichePoP()
			pygame.display.update()
	def affichePoP(self):
		Affichage = [("Nom","Age","Citoyen")]
		for pop in self.core.listePoP:
			Affichage.append(pop.toString())
		text = table_to_str(Affichage)
		for i in range(len(text)):
			txt = self.header.render(text[i], False, (14,188,40))
			self.display.blit(txt,(5,i*20))


