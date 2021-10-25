import pygame
from pygame.locals import *
from tkinter import *
from pnj import *
from listeMap import *
from struc import *
import threading

class Map():
	"""docstring for Map"""
	def __init__(self):
		self.wett = 0
		self.db_img = []
		self.nb_pnj = 0
		self.deathpnj = []
		self.listepnj = []
		self.select = None
		self.tt = 10
		self.editor = None
		for i in range(4):
			self.db_img.append(pygame.image.load("../img/Out/"+str(i)+".png"))
		self.map_1 = empty_grass_ground
		self.map_2 = empty_grass_Struct
		self.MaptoShow = self.map_1
		pygame.init()
		self.display = pygame.display.set_mode((768,640)) 
		self.clock = pygame.time.Clock()
	def add_citizen(self):
		self.nb_pnj +=1
		self.listepnj.append(Citizen(self.nb_pnj))
		self.listepnj[self.nb_pnj-1].body.start(self.spawn)
	def add_killer(self):
		self.nb_pnj +=1
		self.listepnj.append(killer(self.nb_pnj))
		self.listepnj[self.nb_pnj-1].body.start(self.spawn)
	def add_farmer(self):
		self.nb_pnj +=1
		self.listepnj.append(Farmer(self.nb_pnj))
		self.listepnj[self.nb_pnj-1].body.start(self.spawn)
	def clear(self):
		self.display.fill((0,0,0))
		pygame.display.update()
	def init_Struct(self):
		self.map_st = empty_map
		for i in range(len(self.map_2)):
			for ii in range(len(self.map_2[i])):
				if self.map_2[i][ii] == 1:
					self.map_st[i][ii] = tree((ii,i))
				elif self.map_2[i][ii] == 2:
					self.map_st[i][ii] = bush((ii,i))
				elif self.map_2[i][ii] == 3:
					self.map_st[i][ii] = field((ii,i))
	def slowSpeed(self):
		self.tt = 5
	def normalpeed(self):
		self.tt = 10
	def Speed2(self):
		self.tt = 20
	def Speed4(self):
		self.tt = 40
	def show_map(self):
		for y in range(len(self.MaptoShow)):
			for x in range(len(self.MaptoShow[y])):
				sec = self.MaptoShow[y][x]
				if self.MaptoShow[y][x] == 2:
					self.spawn = [x*64,y*64]
					self.display.blit(self.db_img[0],(x*64,y*64))
				self.display.blit(self.db_img[sec],(x*64,y*64))
		for st in self.map_st:
			for stt in st:
				if stt != None:
					stt.live()
					self.display.blit(stt.img,(stt.x*64,stt.y*64))
	def show_dead_pnj(self):
		for i in self.listepnj:
			if i.body.id in self.deathpnj:
				citi = i.body
				self.affiche(citi.face,citi.coordX,citi.coordY)
	def show_pnj(self):
		for i in self.listepnj:
			if not i.body.id in self.deathpnj:
				i.live()
				citi =i.body
				self.affiche(citi.face,citi.coordX,citi.coordY)
	def update(self):
		pygame.display.update()
	def affiche(self,player,x,y):
		self.display.blit(player,(x,y))
	def tick(self):
		self.clock.tick(self.tt)

class Editor(threading.Thread):
	def __init__(self,mainG):
		threading.Thread.__init__(self)
		self.editor =  1
		self.mainG = mainG
	def run(self):
		self.root = Tk()
		self.root.title("Add/edit")
		self.ListeO=Label(self.root,text="No pnj yet")
		self.commands()
		self.speeds()
		self.Update_editor()
		self.show_editor()
	def show_editor(self):
		if self.editor==1:
			try:
				self.ListeOfCmd.pack()
				self.ListeOfspeed.pack()
				self.GridPnj.pack()
				self.ListeO.pack()
				self.root.mainloop()
			except TclError:
				pass
	def Update_editor(self):
		if self.editor == 1:
			self.ListeO.destroy()
			self.ListeO = Frame(self.root)
			self.GridPnj = Frame(self.ListeO)
			x=-1
			y=0
			for pnj in self.mainG.listepnj:
				x+=1
				if x>= 5:
					y+= 1
					x= 0
				
				if pnj.body.Alive :
					name = pnj.body.type+" "+str(pnj.body.id)+" : alive"
					Button(self.GridPnj,text=name,command=pnj.body.show_Info,bg="green").grid(row=y, column=x,padx=5,pady=5)
				else:
					name = pnj.body.type+" "+str(pnj.body.id)+" : dead"
					Button(self.GridPnj,text=name,command=pnj.body.show_Info,bg="red").grid(row=y, column=x,padx=5,pady=5)
			self.GridPnj.pack()
			self.ListeO.pack()
	def commands(self):
		if self.editor==1:
			self.ListeOfCmd = LabelFrame(self.root,text="Ajouter des pnj")
			Button(self.ListeOfCmd,text="Add Citizen",command=self.add_citizen).grid(row=0,column=0)
			Button(self.ListeOfCmd,text="Add Farmer",command=self.add_farmer).grid(row=0,column=1,padx=5)
			Button(self.ListeOfCmd,text="Add killer",command=self.add_killer).grid(row=0,column=2,padx=5)
	def speeds(self):
		if self.editor==1:
			self.ListeOfspeed = LabelFrame(self.root,text="Vitesse du jeux")
			Button(self.ListeOfspeed,text="Slow",command=self.mainG.slowSpeed).grid(row=0,column=0)
			Button(self.ListeOfspeed,text="Normal",command=self.mainG.normalpeed).grid(row=0,column=1,padx=5)
			Button(self.ListeOfspeed,text="Speedx2",command=self.mainG.Speed2).grid(row=1,column=0,padx=5)
			Button(self.ListeOfspeed,text="Speedx4",command=self.mainG.Speed4).grid(row=1,column=1,padx=5)
	def add_citizen(self):
		self.mainG.add_citizen()
		self.mainG.listepnj[self.mainG.nb_pnj-1].body.mainG = self.mainG
		self.Update_editor()
		self.show_editor()
	def add_farmer(self):
		self.mainG.add_farmer()
		self.mainG.listepnj[self.mainG.nb_pnj-1].body.mainG = self.mainG
		self.Update_editor()
		self.show_editor()
	def add_killer(self):
		self.mainG.add_killer()
		self.mainG.listepnj[self.mainG.nb_pnj-1].body.mainG = self.mainG
		self.Update_editor()
		self.show_editor()
