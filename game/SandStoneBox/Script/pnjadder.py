from random import choice as good , randint as rand
from ListePr import listePrenom
from Function import *
from struc import *

class DefaultPnj  :
	gotoX = 0
	gotoY = 0
	gotoQ = False
	ids = 0
	Alive = True
	db_img = []
	idface = 0
	coordX = 64
	coordY = 64
	gotoX = 0
	gotoY = 0
	gotoQ = False
	dirs=0
	select = False
	infoB = []
	spawn = []
	optd = [[0,1],[0,-1],[1,0],[-1,0]]
	nbT = 0
	maps = None
	def __init__ (self):
		pass
	def checkcolid(self):
		x = self.coordX + self.optd[self.dirs][0]*5
		y = self.coordY + self.optd[self.dirs][1]*5
		caseX = (x+32)//64
		caseY = (y+32)//64
		strc = self.maps.struct[caseY][caseX]
		if strc == None:
				return True
		elif strc.colideBox():
			return True
		return False
	def goto(self,x,y):
		self.gotoX = x
		self.gotoY = y
		self.gotoQ = True
	def start(self,maps):
		print(self.type+" "+str(self.ids)+' added !')
		self.coordX = maps.spawn[0]
		self.coordY = maps.spawn[1]
		self.maps = maps
		self.idface = rand(0,len(self.db_img)-1)
		self.name = good(listePrenom[self.idface%2])
		self.face = self.db_img[self.idface]
		self.sexe = ["femmale","male"][self.idface%2]
	def Think(self):
		if self.Alive:
			self.dir = good([0,1,2,3])
			self.nbT = rand(15,20)
		else:
			self.nbT=0
	def ThinkGoto(self):
		if self.Alive:
			xx = self.gotoX//64-self.coordX//64
			yy = self.gotoY//64-self.coordY//64
			if xx < 0:
				self.dir = 3
			elif xx > 0:
				self.dir = 2
			elif yy < 0:
				self.dir = 1
			elif yy>0 :
				self.dir = 0
			else:
				self.gotoQ=False
			self.nbT = 12
		else:
			self.nbT=0
	def walk(self):
		if not self.gotoQ:
			if self.nbT>0 and self.checkcolid():
				self.coordX += self.optd[self.dir][0]*5
				self.coordY += self.optd[self.dir][1]*5
				self.nbT-=1
			else :
				self.Think()
		else :
			if self.nbT>0 and self.checkcolid():
				self.coordX += self.optd[self.dir][0]*5
				self.coordY += self.optd[self.dir][1]*5
				self.nbT-=1
			else :
				self.ThinkGoto()
	def Death(self):
		print(self.type+" "+str(self.id)+" killed")
		self.face =pygame.image.load("../img/Pnj/death.png")
		self.maps.deathpnj.append(self.ids)
		self.Alive = False
		self.nbT = 0
	def Live(self):
		print(self.type+" "+str(self.id)+" Resurrect")
		self.Alive = True
		self.nbT = 2
		self.maps.deathpnj.pop(self.mainG.deathpnj.index(self.ids))
		self.walk()
class Citizen(DefaultPnj) :
	def __init__(self,i):
		self.ids = i
		self.type = "Citizen"
		self.db_img = []
		for i in range(6):
			self.db_img.append(pygame.image.load("../img/Pnj/Citizen/"+str(i)+".png"))
	def live(self):
		pass
class Farmer(DefaultPnj) :
	def __init__(self,i):
		self.ids = i
		self.type = "Farmer"
		self.doIcreate = 20
		self.create = False
		self.pause = 0
		self.nbFields = 0
		self.fieldsPos = []
		self.db_img = []
		self.infoB = [self.nbFields,self.fieldsPos]
		for i in range(4):
			self.db_img.append(pygame.image.load("../img/Pnj/Farmer/"+str(i)+".png"))
	def live(self):
		self.create_field()
		self.check_fields()
	def create_field(self):
		if self.doIcreate !=5 and not self.create :
			self.doIcreate = rand(0,250)
		elif self.doIcreate == 5 and not self.create and self.nbFields<=4 :
			print("Farmer want to create field !")
			locaOk = False
			for line in self.maps.struct:
				if None in line :
					while not locaOk:
						self.lox = rand(1,11)
						self.loy = rand(1,9)
						if self.maps.struct[self.loy][self.lox] == None:
							locaOk = True
					self.goto(self.lox*64,self.loy*64)
					self.pause = 0
					self.create = True
		elif self.create :
			if not self.gotoQ :
				if self.pause<= 0:
					self.pause = 10
				elif self.pause>110 :
					print("Now Create fields")
					self.maps.struct[self.loy][self.lox] = field((self.lox,self.loy))
					self.nbFields += 1
					self.fieldsPos.append([self.lox*64,self.loy*64])
					self.infoB = [self.nbFields,self.fieldsPos]
					self.create = False
					self.doIcreate = 40
					self.pause = 0
				else :
					self.pause+=5
		if self.pause <= 0:
			self.walk()
	def check_fields(self):
		for fields in self.fieldsPos:
			if self.maps.struct[fields[1]//64][fields[0]//64].glow>=20:
				winwet = self.maps.struct[fields[1]//64][fields[0]//64].capacity
				if self.maps.stock[0]+winwet <= self.maps.Storage[0]:
					self.maps.stock[0]+=winwet
					self.maps.struct[fields[1]//64][fields[0]//64].cut()

class killer(DefaultPnj) :
	def __init__(self,i):
		self.ids = i
		self.type = "Killer"
		self.db_img = [pygame.image.load("../img/Pnj/Killer/0.png")]
		self.pause = 0
		self.cible = ""
		self.infoB = ""
	def live(self):
		if self.pause>250:
			self.kill()
		else :
			self.pause += 1
		self.walk()
	def kill(self):
		if len(self.mainG.listepnj)>1 and (len(self.mainG.listepnj)-1)>len(self.mainG.deathpnj):
			if self.cible =="":
				print('Killer will kille !',self.mainG.deathpnj)
				self.cible = good(self.mainG.listepnj)
				while self.cible.ids == self.ids and not self.cible.ids in self.mainG.deathpnj :
					self.cible = good(self.mainG.listepnj)
			x = self.cible.coordX
			y = self.cible.coordY
			self.goto(x,y)
			self.infoB = self.cible.type+" "+str(self.cible.id)
			if x//64 == self.coordX//64 and y//64 == self.coordY//64 :
				self.cible.Death()
				self.cible=""
				self.pause = 0
				self.infoB = ""
		else :
			self.pause = 0
			print('No to kill')
				


listeJobs = [[],["Citizen","Farmer"],["Killer"]]
Nb_img = {"Citizen":6,"Farmer":4,"Killer":1}
Pnj = {"Citizen":Citizen,"Farmer":Farmer,"Killer":killer}