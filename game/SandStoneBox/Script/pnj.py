from random import choice as good, randint as rand
import threading
from time import sleep as pause
from ListePr import listePrenom
from Function import *
from struc import *
from mapping import *


class DefaultPnj():

	def __init__(self):
		self.Vital = {"Alive": True, "Id": 0, "Face": None, "Name": None, "Sexe": None, "Type": None}
		self.Move = {"X": 0, "Y": 0, "NbD": 0, "Direct": 0, "Speed": 0.05, "Movem": [[0, 1], [0, -1], [1, 0], [-1, 0]]}
		self.Goto = {"DoI": False, "X": 0, "Y": 0}
		self.db_img = []
		self.maps = None
		print("New Pnj Added !")
	def checkcolid(self):
		x = self.Move["X"] + self.Move["Movem"][self.Move["Direct"]][0] * 5
		y = self.Move["Y"] + self.Move["Movem"][self.Move["Direct"]][1] * 5
		caseX = (x + 32) // 64
		caseY = (y + 32) // 64

		strc = self.maps.struct[caseY][caseX]
		if strc == None:
			return True
		elif strc.colideBox():
			return True
		return False

	def goto(self, x, y):
		self.Goto["X"] = x
		self.Goto["Y"] = y
		self.Goto["DoI"] = True

	def load(self, maps):
		self.Move["X"] = maps.spawn[0]
		self.Move["Y"] = maps.spawn[1]
		self.maps = maps
		idface = rand(0, len(self.db_img) - 1)

		self.Vital["Name"] = good(listePrenom[idface % 2])
		self.Vital["Face"] = self.db_img[idface]
		self.db_img = None
		self.Vital["Sexe"] = ["femmale", "male"][idface % 2]

	def Think(self):
		if not self.Goto["DoI"]:
			if self.Vital["Alive"]:
				self.Move["Direct"] = good([0, 1, 2, 3])
				self.Move["NbD"] = rand(15, 20)
			else:
				self.Move["NbD"] = 0

	def ThinkGoto(self):
		if self.Goto["DoI"]:
			if self.Vital["Alive"]:
				xx = self.Goto["X"] // 64 - self.Move["X"] // 64
				yy = self.Goto["Y"] // 64 - self.Move["Y"] // 64
				if xx < 0:
					self.Move["Direct"] = 3
				elif xx > 0:
					self.Move["Direct"] = 2
				elif yy < 0:
					self.Move["Direct"] = 1
				elif yy > 0:
					self.Move["Direct"] = 0
				else:
					self.Goto["DoI"] = False
				self.Move["NbD"] = 12
			else:
				self.Move["NbD"] = 0

	def walk(self):
		if self.Move["NbD"] > 0 and self.checkcolid():
			self.Move["X"] += self.Move["Movem"][self.Move["Direct"]][0] * 5
			self.Move["Y"] += self.Move["Movem"][self.Move["Direct"]][1] * 5
			self.Move["NbD"] -= 1
		else:
			self.ThinkGoto()
			self.Think()

	def Death(self):
		print(self.Vital["Type"] + " " + str(self.Vital["Id"]) + " killed")
		self.self.Vital["Face"] = pygame.image.load("../img/Pnj/death.png")
		self.maps.deathpnj.append(self.Vital["Id"])
		self.Vital["Alive"] = False
		self.Move["NbD"] = 0

	def Live(self):
		print(self.Vital["Type"] + " " + str(self.Vital["Id"]) + " Resurrect")
		self.Vital["Alive"] = True
		self.Move["NbD"] = 10
		self.maps.deathpnj.pop(self.mainG.deathpnj.index(self.Vital["Id"]))
		self.walk()


class Citizen(threading.Thread):
	def __init__(self, i, maps):
		self.core = DefaultPnj()
		threading.Thread.__init__(self)
		print(i)
		self.core.Vital["Id"] = i
		self.core.Vital["Type"] = "Citizen"
		for i in range(6):
			self.core.db_img.append(pygame.image.load("../img/Pnj/Citizen/" + str(i) + ".png"))
		self.core.load(maps)

	def run(self):
		while not self.core.maps.end :
			pause(self.core.Move['Speed'])
			self.core.walk()

	def string(self):
		return self.core.Vital["Face"], (self.core.Move["X"], self.core.Move["Y"])


class Farmer(threading.Thread):
	def __init__(self, i, maps):
		threading.Thread.__init__(self)
		self.core = DefaultPnj()
		self.core.Vital["Id"] = i
		print(i)
		self.core.Vital["Type"] = "Farmer"
		self.Jobs = {"DoI": 20, "Create": False, "FieldsL": []}
		for i in range(4):
			self.core.db_img.append(pygame.image.load("../img/Pnj/Farmer/" + str(i) + ".png"))
		self.core.load(maps)

	def run(self):
		while not self.core.maps.end :
			pause(self.core.Move['Speed'])
			self.core.walk()
			self.create_field()
			self.check_fields()

	def string(self):
		return self.core.Vital["Face"], (self.core.Move["X"], self.core.Move["Y"])

	def create_field(self):
		if self.Jobs["DoI"] != 5 and not self.Jobs["Create"]:
			self.Jobs["DoI"] = rand(0, 250)
		if self.Jobs["DoI"] == 5 and not self.Jobs["Create"] and len(self.Jobs["FieldsL"]) < 4:
			print('Go to create a fields !')
			locaOk = False
			for line in self.core.maps.struct:
				if None in line:
					while not locaOk:
						self.lox = rand(1, 11)
						self.loy = rand(1, 9)
						if self.core.maps.struct[self.loy][self.lox] == None:
							locaOk = True
					self.core.goto(self.lox * 64, self.loy * 64)
					self.Jobs["Create"] = True
		elif self.Jobs["Create"]:
			if not self.core.Goto["DoI"]:
				pause(1)
				self.core.maps.struct[self.loy][self.lox] = field((self.lox, self.loy))
				self.Jobs["FieldsL"].append([self.lox * 64, self.loy * 64])
				self.Jobs["Create"] = False
				self.Jobs["DoI"] = 40

	def check_fields(self):
		for fields in self.Jobs["FieldsL"]:
			if self.core.maps.struct[fields[1] // 64][fields[0] // 64].glow >= 20:
				self.core.goto(fields[0]-32,fields[1]-32)
				while self.core.Goto["DoI"]:
					if self.core.maps.end :
						self.core.Goto["DoI"]  = False
					pause(self.core.Move['Speed'])
					self.core.walk()
				winwet = self.core.maps.struct[fields[1] // 64][fields[0] // 64].capacity
				if self.core.maps.stock[0] + winwet <= self.core.maps.Storage[0]:
					pause(1)
					self.core.maps.stock[0] += winwet
					self.core.maps.struct[fields[1] // 64][fields[0] // 64].cut()
					pause(1)


class Killer(threading.Thread):


	def __init__(self, i, maps):
		threading.Thread.__init__(self)
		self.core = DefaultPnj()
		self.core.Vital["Id"] = i
		print(i)
		self.core.Vital["Type"] = "Killer"
		self.core.db_img = [pygame.image.load("../img/Pnj/Killer/0.png")]
		self.core.load(maps)

	def run(self):
		while not self.core.maps.end :
			pause(self.core.Move['Speed'])
			self.core.walk()

	def string(self):
		return self.core.Vital["Face"], (self.core.Move["X"], self.core.Move["Y"])


listeJobs = [[], ["Citizen", "Farmer"], ["Killer"]]
Nb_img = {"Citizen": 6, "Farmer": 4, "Killer": 1}
Pnj = {"Citizen": Citizen, "Farmer": Farmer, "Killer": Killer}
