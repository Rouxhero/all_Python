import pygame
from random import randint as r


class NewMap():
	def __init__(self):
		self.map = []
		self.img = []
	def DoImport(self):
		self.img = []
		for i in range(6):
			self.img.append(pygame.transform.scale(pygame.image.load("../img/"+str(i)+".png"),(64,64)))
	def create(self):
		self.map = []
		
		for i in range(8):
			row = []
			for ii in range(10):
				case = r(0,100)
				if case <=5 :
					row.append(3)
				else :
					row.append(r(0,2))
			self.map.append(row)
