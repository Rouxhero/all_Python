from Function import *
from mapping import *
from maincore import *

class Sandbox :

	def __init__(self):
		self.type="IA"
		printl("Loading setting:")
		self.clock = pygame.time.Clock()
		self.config = open("setting.cfg","r").read().split(';')
		print("Done!")
		self.config_display = (int(self.config[0]),int(self.config[1]))
		if self.config[2] == "True":
			self.display = pygame.display.set_mode(self.config_display,FULLSCREEN)
		else :
			self.display = pygame.display.set_mode(self.config_display)
		self.map = None
		self.continu = True
		self.mainG = mainGame()
	def tick(self):
		self.mainG.clock.tick(15)
	def start(self):
		pygame.init()
		pygame.font.init()
		self.header = pygame.font.Font('../Libs/head.ttf', 50)
		self.submenu = pygame.font.Font('../Libs/menu.ttf', 35)
		self.info = pygame.font.Font('../Libs/menu.ttf', 25)
		pygame.display.set_caption("SandStoneBox-Chose Map")
		pygame.display.set_icon(PyImgLoad("../img/logo.png"))
	def Show(self):
		if self.map == None:
			self.chose_map()
		else :
			if not self.mainG.isStart :
				self.mainG.start(self.map)
			else :
				self.mainG.Show()
	def chose_map(self):
		self.choix = None
		self.display.fill((0,0,0))
		self.display.blit(PyPrint("Select Map :",(198,198,116),self.header),(200,40))
		y = 0
		x = 0
		self.coord_map = []
		for maps in ListeMap:
			txt = PyPrint(maps[0],(158,255,218),self.submenu)
			undertxt = PyPrint(maps[1],(152,218,120),self.info)
			coordx = [50+x,60+x+max(txt.get_size()[0],undertxt.get_size()[0])]
			coordy = [200+y,220+y+max(txt.get_size()[1],undertxt.get_size()[1])]
			self.coord_map.append([coordx,coordy])
			self.display.blit(txt,(50+x,200+y))
			self.display.blit(undertxt,(60+x,225+y))
			y += 60
			if y > 400:
				x = 250
				y = 0
		pygame.display.update()
	def Menu_Cursor(self,x,y):
		if self.map == None:
			for i in range(len(self.coord_map)):
				xmin = self.coord_map[i][0][0]
				xmax = self.coord_map[i][0][1]
				ymin = self.coord_map[i][1][0]
				ymax = self.coord_map[i][1][1]
				if x > xmin	and x < xmax :
					if y > ymin and y < ymax:
						self.choix = i
			if self.choix != None:
				if self.choix == 0:
					self.map = empty_Map()
				if self.choix == 1:
					self.map = Forest()
		if self.mainG.isStart:
			for i in range(len(self.mainG.listeClique)):
				xmin = self.mainG.listeClique[i][0][0]
				xmax = self.mainG.listeClique[i][0][1]
				ymin = self.mainG.listeClique[i][1][0]
				ymax = self.mainG.listeClique[i][1][1]
				if x > xmin	and x < xmax :
					if y > ymin and y < ymax:
						if i == 1:
							self.mainG.closeAdd()
						if i == 2 and not self.mainG.citAdd:
							self.mainG.addCitizen()
			for i in range(len(self.mainG.CliqueSora)):
					xmin = self.mainG.CliqueSora[i][0][0]
					xmax = self.mainG.CliqueSora[i][0][1]
					ymin = self.mainG.CliqueSora[i][1][0]
					ymax = self.mainG.CliqueSora[i][1][1]
					if x > xmin	and x < xmax :
						if y > ymin and y < ymax:
							if i == 1:
								self.mainG.closeStora()

		if self.mainG.citAdd:
			for i in range(len(self.mainG.listeCliqueAdd)):
				xmin = self.mainG.listeCliqueAdd[i][0][0]
				xmax = self.mainG.listeCliqueAdd[i][0][1]
				ymin = self.mainG.listeCliqueAdd[i][1][0]
				ymax = self.mainG.listeCliqueAdd[i][1][1]
				if x > xmin	and x < xmax :
					if y > ymin and y < ymax:
						if i < 2 :
							self.mainG.jobs = listeJobs[self.mainG.adderPage][i]
							self.mainG.showAddCiti()
						if i == len(self.mainG.listeCliqueAdd)-3 and self.mainG.adderPage+1 < len(listeJobs):
							self.mainG.adderPage+=1
						if i == len(self.mainG.listeCliqueAdd)-2 and self.mainG.adderPage-1>0:
							self.mainG.adderPage -= 1
						if i == len(self.mainG.listeCliqueAdd)-1:
							self.mainG.PlayCiti()
	def moveWindow(self,x,y):
		if self.mainG.isStart:
			for i in range(len(self.mainG.listeClique)):
				xmin = self.mainG.listeClique[i][0][0]
				xmax = self.mainG.listeClique[i][0][1]
				ymin = self.mainG.listeClique[i][1][0]
				ymax = self.mainG.listeClique[i][1][1]
				if x > xmin	and x < xmax :
					if y > ymin and y < ymax:
						if i == 0:
							self.mainG.moveAdd(x,y)
			for i in range(len(self.mainG.CliqueSora)):
				xmin = self.mainG.CliqueSora[i][0][0]
				xmax = self.mainG.CliqueSora[i][0][1]
				ymin = self.mainG.CliqueSora[i][1][0]
				ymax = self.mainG.CliqueSora[i][1][1]
				if x > xmin	and x < xmax :
					if y > ymin and y < ymax:
						if i == 0:
							self.mainG.moveStora(x,y)


