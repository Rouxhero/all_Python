from Function import *
from struc import *

ListeMap=[["Empty Grass","Just grass ..."],["Forest","A lot of trees !"],["Village","Simple village "],["Lava Wolrd","Hum.. Realy ?"]]
class empty_Map :

	def __init__ (self):
		print('Empty')
		self.name="Empty Grass"
		self.capa = ["Wet :","Corn :"]
		self.Storage = [1500,0]
		self.stock = [10,0]
		self.end = False
		self.map = [
		[3,0,0,0,0,0,0,0,0,0,0,3],
		[0,2,0,0,0,0,1,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,1,0],
		[0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,1,0,0,0,0,0,0,0,0,0],
		[3,0,0,0,0,0,0,0,0,0,0,3],
		]
		self.struct = [
		[None,None,None,None,None,None,None,None,None,None,None,None],
		[None,None,None,None,None,None,None,None,None,None,None,None],
		[None,None,None,None,None,None,None,None,None,None,None,None],
		[None,None,None,None,None,None,None,None,None,None,None,None],
		[None,None,None,None,None,None,None,None,None,None,None,None],
		[None,None,None,None,None,None,None,None,None,None,None,None],
		[None,None,None,None,None,None,None,None,None,None,None,None],
		[None,None,None,None,None,None,None,None,None,None,None,None],
		[None,None,None,None,None,None,None,None,None,None,None,None],
		[None,None,None,None,None,None,None,None,None,None,None,None],
		]
		self.struct_pos = [
		[1,1,1,1,1,1,1,1,1,1,1,1],
		[1,0,0,0,0,0,0,0,0,0,0,1],
		[1,0,0,0,0,0,0,0,0,0,0,1],
		[1,0,0,0,0,0,0,0,0,0,0,1],
		[1,0,0,0,0,0,0,0,0,0,0,1],
		[1,0,0,0,0,0,0,0,0,0,0,1],
		[1,0,0,0,0,0,0,0,0,0,0,1],
		[1,0,0,0,0,0,0,0,0,0,0,1],
		[1,0,0,0,0,0,0,0,0,0,0,1],
		[1,1,1,1,1,1,1,1,1,1,1,1],
		]
		self.db_img = []
		for i in range(4):
			self.db_img.append(PyImgLoad("../img/Out/"+str(i)+".png"))
		self.spawn = []
	def start(self,display):
		self.display = display
		for y in range(len(self.map)):
			for x in range(len(self.map[y])):
				sec = self.map[y][x]
				if self.struct_pos[y][x] != 0:
					self.struct[y][x] = ListeStructure[self.struct_pos[y][x]]((x,y))
					if self.struct[y][x].type =="Storage":
						self.Storage[self.struct[y][x].storagetype] += self.struct[y][x].capacity
				if sec == 2:
					self.spawn = [x*64,y*64]
	def Show(self):
		for y in range(len(self.map)):
			for x in range(len(self.map[y])):
				sec = self.map[y][x]
				if sec == 2:
					self.display.blit(self.db_img[0],(x*64,y*64))
				self.display.blit(self.db_img[sec],(x*64,y*64))
		for st in self.struct:
			for stt in st:
				if stt != None:
					self.display.blit(stt.img,(stt.x*64,stt.y*64))
class Forest :

	def __init__ (self):
		print('Empty')
		self.name="Forest"
		self.capa = ["Wet :","Corn :"]
		self.Storage = [0,0]
		self.stock = [0,0]
		self.end = False
		self.map = [
		[0,0,0,0,0,0,0,0,0,0,0,0],
		[0,2,3,0,0,0,1,0,3,3,3,0],
		[0,3,3,0,0,0,0,0,3,3,3,0],
		[0,14,8,5,5,5,10,0,0,4,0,0],
		[0,0,0,0,0,0,4,0,0,4,0,0],
		[0,3,3,3,3,0,4,0,0,4,0,0],
		[0,3,3,3,3,5,12,0,0,4,0,0],
		[0,3,3,3,3,0,4,0,0,4,0,0],
		[0,3,3,3,3,0,14,5,5,15,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,0],
		]
		self.struct = [
		[None,None,None,None,None,None,None,None,None,None,None,None],
		[None,None,None,None,None,None,None,None,None,None,None,None],
		[None,None,None,None,None,None,None,None,None,None,None,None],
		[None,None,None,None,None,None,None,None,None,None,None,None],
		[None,None,None,None,None,None,None,None,None,None,None,None],
		[None,None,None,None,None,None,None,None,None,None,None,None],
		[None,None,None,None,None,None,None,None,None,None,None,None],
		[None,None,None,None,None,None,None,None,None,None,None,None],
		[None,None,None,None,None,None,None,None,None,None,None,None],
		[None,None,None,None,None,None,None,None,None,None,None,None],
		]
		self.struct_pos = [
		[1,1,1,1,1,1,1,1,1,1,1,1],
		[1,0,0,1,1,1,1,1,0,0,0,1],
		[1,0,0,1,1,1,1,1,0,0,0,1],
		[1,0,0,0,0,0,0,1,1,0,1,1],
		[1,1,1,1,1,1,0,1,1,0,1,1],
		[1,0,0,0,0,1,0,1,1,0,1,1],
		[1,0,0,0,0,0,0,1,1,0,1,1],
		[1,0,0,0,0,1,0,1,2,0,1,1],
		[1,0,0,0,0,1,0,0,0,0,1,1],
		[1,1,1,1,1,1,1,1,1,1,1,1],
		]
		self.db_img = []
		for i in range(19):
			self.db_img.append(PyImgLoad("../img/Out/"+str(i)+".png"))
		self.spawn = []
	def start(self,display):
		self.display = display
		for y in range(len(self.map)):
			for x in range(len(self.map[y])):
				sec = self.map[y][x]
				if self.struct_pos[y][x] != 0:
					self.struct[y][x] = ListeStructure[self.struct_pos[y][x]]((x,y))
					if self.struct[y][x].type =="Storage":
						self.Storage[self.struct[y][x].storagetype] += self.struct[y][x].capacity
				if sec == 2:
					self.spawn = [x*64,y*64]
	def Show(self):
		for y in range(len(self.map)):
			for x in range(len(self.map[y])):
				sec = self.map[y][x]
				if sec == 2:
					self.display.blit(self.db_img[3],(x*64,y*64))
				self.display.blit(self.db_img[sec],(x*64,y*64))
		for st in self.struct:
			for stt in st:
				if stt != None:
					self.display.blit(stt.img,(stt.x*64,stt.y*64))


MapList = [None,None,empty_Map,Forest]