# -*- coding: utf-8 -*-
from random import choice as good , randint as rand
from ListePr import listePrenom
from Function import *
class DefaultPnj  :

	def __init__ (self,i):
		self.type = ""
		self.id = i
		self.Alive = True
		self.db_img = []
		self.name ="Bot"
		self.idface = 0
		self.coordX = 64
		self.coordY = 64
		self.gotoX = 0
		self.gotoY = 0
		self.gotoQ = False
		self.dir=0
		self.select = False
		self.infoB = []
		self.spawn = []
		self.optd = [[0,1],[0,-1],[1,0],[-1,0]]
		self.nbT = 0
		self.mainG = None
		
	def checkcolid(self):
		x = self.coordX + self.optd[self.dir][0]*5
		y = self.coordY + self.optd[self.dir][1]*5
		caseX = (x+32)//64
		caseY = (y+32)//64
		strc = self.mainG.struct[caseY][caseX]
		if strc == None:
				return True
		elif strc.colideBox():
			return True
		return False
	def goto(self,x,y):
		self.gotoX = x
		self.gotoY = y
		self.gotoQ = True
	def show_Info(self):
		self.root2 = Tk()
		self.select=True
		self.root2.title("Edite")
		self.face=pygame.image.load('../img/Pnj/select.png')
		texte="Name : "+self.name+' | Sexe :'+self.sexe+ "?| Job : "+self.type
		Label(self.root2,text=texte).pack()
		if self.Alive :
			path = "../img/Pnj/"+self.type+"/"+str(self.idface)+".png"
			photo = PhotoImage(master=self.root2,file=path)
			self.KilB = Button(self.root2,text="kill",command=self.Death)
		else :
			path = "../img/Pnj/death.png"
			photo = PhotoImage(master=self.root2,file=path)
			self.KilB = Button(self.root2,text="Resurrect",command=self.Live)
		self.canvas = Canvas(self.root2,width=64, height=64)
		self.mini = self.canvas.create_image(0,0,anchor=NW, image=photo)
		Button(self.root2,text="quit",command=self.leaveE).pack()
		self.mainG.select = self.id-1
		self.canvas.pack()
		self.KilB.pack()
		self.Info = LabelFrame(self.root2,text="Info :")
		if self.type == "Farmer":
			textee = "Fields : "+str(self.infoB[0])+"/4"
			Label(self.Info,text=textee).pack()
		if self.type == "Killer":
			textee = "Victime : "+self.infoB
			Label(self.Info,text=textee).pack()
		self.Info.pack()
		self.root2.mainloop()
	def leaveE(self):
		if self.Alive:
			self.face = self.db_img[self.idface]
		else :
			self.face =pygame.image.load("../img/Pnj/death.png")
		self.select= False
		self.mainG.select = None
		self.root2.destroy()
	def start(self,spawn):
		print(self.type+" "+str(self.id)+' added !')
		self.coordX = spawn[0]
		self.coordY = spawn[1]

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
		self.mainG.deathpnj.append(self.id)
		self.Alive = False
		self.nbT = 0
		if self.select == True:
			photo = PhotoImage(master=self.root2,file="../img/Pnj/death.png")
			self.mini = self.canvas.create_image(0,0,anchor=NW, image=photo)
			self.canvas.pack()
			self.mainG.show_map()
			self.mainG.show_dead_pnj()
			self.mainG.display.blit(self.face,(self.coordX,self.coordY))
			self.mainG.show_pnj()
			self.mainG.update()
		self.mainG.editor.Update_editor()
	def Live(self):
		print(self.type+" "+str(self.id)+" Resurrect")
		self.Alive = True
		self.nbT = 2
		self.mainG.deathpnj.pop(self.mainG.deathpnj.index(self.id))
		if self.select==True:
			path = "../img/Pnj/"+self.type+"/"+str(self.idface)+".png"
			photo = PhotoImage(master=self.root2,file=path)
			self.mini = self.canvas.create_image(0,0,anchor=NW, image=photo)
			self.canvas.pack()
			self.face =self.db_img[self.idface]
			self.canvas.pack()
			self.mainG.show_map()
			self.mainG.show_dead_pnj()
			self.mainG.display.blit(self.face,(self.coordX,self.coordY))
			self.mainG.show_pnj()
			self.mainG.update()
		self.mainG.editor.Update_editor()
		self.walk()

class Citizen :
	def __init__(self,i):
		self.body = DefaultPnj(i)
		self.body.type = "Citizen"
		for i in range(6):
			self.body.db_img.append(pygame.image.load("../img/Pnj/Citizen/"+str(i)+".png"))
	def live(self):
		self.body.walk()
class Farmer :
	def __init__(self,i):
		self.body = DefaultPnj(i)
		self.body.type = "Farmer"
		self.doIcreate = 20
		self.create = False
		self.pause = 0
		self.nbFields = 0
		self.fieldsPos = []
		self.body.infoB = [self.nbFields,self.fieldsPos]
		for i in range(4):
			self.body.db_img.append(pygame.image.load("../img/Pnj/Farmer/"+str(i)+".png"))
	def live(self):
		self.create_field()
		self.check_fields()

	def create_field(self):
		if self.doIcreate !=5 and not self.create :
			self.doIcreate = rand(0,250)
		elif self.doIcreate == 5 and not self.create and self.nbFields<=4 :
			print("Farmer want to create field !")
			locaOk = False
			for line in self.body.mainG.map_st:
				if None in line :
					while not locaOk:
						self.lox = rands(1,11)
						self.loy = rands(1,9)
						if self.body.mainG.map_st[self.loy][self.lox] == None:
							locaOk = True
					self.body.goto(self.lox*64,self.loy*64)
					self.pause = 0
					self.create = True
		elif self.create :
			if not self.body.gotoQ :
				if self.pause<= 0:
					self.pause = 10
				elif self.pause>110 :
					print("Now Create fields")
					self.body.mainG.map_st[self.loy][self.lox] = field((self.lox,self.loy))
					self.nbFields += 1
					self.fieldsPos.append([self.lox*64,self.loy*64])
					self.body.infoB = [self.nbFields,self.fieldsPos]
					self.create = False
					self.doIcreate = 40
					self.pause = 0
				else :
					self.pause+=5
		if self.pause <= 0:
			self.body.walk()
	def check_fields(self):
		for fields in self.fieldsPos:
			if self.body.mainG.map_st[fields[1]//64][fields[0]//64].glow>=20:
				self.body.mainG.map_st[fields[1]//64][fields[0]//64].cut()
				self.body.mainG.wett+= 10
class killer :
	def __init__(self,i):
		self.body = DefaultPnj(i)
		self.body.type = "Killer"
		self.body.db_img = [pygame.image.load("../img/Pnj/Killer/0.png")]
		self.pause = 0
		self.cible = ""
		self.body.infoB = ""
	def live(self):
		if self.pause>250:
			self.kill()
		else :
			self.pause += 1
		self.body.walk()
	def kill(self):
		if len(self.body.mainG.listepnj)>1 and (len(self.body.mainG.listepnj)-1)>len(self.body.mainG.deathpnj):
			if self.cible =="":
				print('Killer will kille !',self.body.mainG.deathpnj)
				self.cible = good(self.body.mainG.listepnj)
				while self.cible.body.id == self.body.id and not self.cible.body.id in self.body.mainG.deathpnj :
					self.cible = good(self.body.mainG.listepnj)
			x = self.cible.body.coordX
			y = self.cible.body.coordY
			self.body.goto(x,y)
			self.body.infoB = self.cible.body.type+" "+str(self.cible.body.id)
			if x//64 == self.body.coordX//64 and y//64 == self.body.coordY//64 :
				self.cible.body.Death()
				self.cible=""
				self.pause = 0
				self.body.infoB = ""
		else :
			self.pause = 0
			print('No Body to kill')
				


listeJobs = [[],["Citizen","Farmer"],["Killer"]]
Nb_img = {"Citizen":6,"Farmer":4,"Killer":1}
Pnj = {"Citizen":Citizen,"Farmer":Farmer,"Killer":killer}