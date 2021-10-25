from Function import *
from random import randint as rand

class tree :
	def __init__(self,coord):
		self.x = coord[0]
		self.y = coord[1]
		self.unbreak = False
		self.colide = False
		self.glow = 10
		self.db_img = [pygame.image.load('../img/Structure/0.png'),pygame.image.load('../img/Structure/3.png'),pygame.image.load('../img/Structure/4.png')]
		self.img = self.db_img[0]
		self.type = "Element"
	def colideBox(self):
		return self.colide
	def cut(self):
		if not self.unbreak and self.glow > 10:
			self.glow = 0
			self.colide = True
			self.img=self.db_img[1]
	def live(self):
		self.glow+=rand(0,100)/1000
		if self.glow >= 5 and self.glow<9:
			self.img = self.db_img[2]
			self.colide = False
		if self.glow >= 10:
			self.img = self.db_img[0]
class bush :
	def __init__(self,coord):
		self.x = coord[0]
		self.y = coord[1]
		self.unbreak = False
		self.colide = True
		self.glow = 1
		self.db_img = [pygame.image.load('../img/Structure/1.png'),pygame.image.load('../img/Structure/2.png')]
		self.img = self.db_img[0]
		self.type = "Element"
	def colideBox(self):
		return self.colide
	def cut(self):
		if not self.unbreak and self.glow > 5:
			self.glow = 0
			self.colide = True
			self.img=self.db_img[0]
	def live(self):
		self.glow+=rand(0,100)/1000
		if self.glow >= 5:
			self.img = self.db_img[1]
class field :
	def __init__(self,coord):
		self.x = coord[0]
		self.y = coord[1]
		self.unbreak = False
		self.colide = True
		self.glow = 0
		self.db_img = []
		for i in range(5,10):
			self.db_img.append(pygame.image.load('../img/Structure/'+str(i)+'.png'))
		self.img = self.db_img[0]
		self.type = "Element"
		self.capacity = 150
	def colideBox(self):
		return self.colide
	def cut(self):
		if not self.unbreak and self.glow > 20:
			self.glow = 0
			self.colide = True
			self.img=self.db_img[0]
	def live(self):
		self.glow+=rand(0,100)/1000
		if self.glow >= 5 and self.glow<10:
			self.img = self.db_img[1]
		elif self.glow >= 10 and self.glow<15:
			self.img = self.db_img[2]
		elif self.glow >= 15 and self.glow<20:
			self.img = self.db_img[3]
		elif self.glow>=20:
			self.img = self.db_img[4]
class barn :
	def __init__(self,coord):
		self.x = coord[0]
		self.y = coord[1]
		self.unbreak = False
		self.colide = False
		self.glow = 0
		self.db_img = []
		self.db_img.append(pygame.image.load('../img/Structure/10.png'))
		self.img = self.db_img[0]
		self.type = "Storage"
		self.storagetype = 0 # 0 -> ble , 1 -> corne
		self.capacity = 1500
	def colideBox(self):
		return self.colide
	def live(self):
		pass

ListeStructure = [None,tree,bush,field,barn]
