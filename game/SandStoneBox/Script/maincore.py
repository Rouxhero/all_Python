from Function import *
from pnj import *
class mainGame :


	def __init__(self):
		self.clock = pygame.time.Clock()
		self.config = open("setting.cfg","r").read().split(';')
		print("Done!")
		self.config_display = (int(self.config[0]),int(self.config[1]))
		if self.config[2] == "True":
			self.display = pygame.display.set_mode(self.config_display,FULLSCREEN)
		else :
			self.display = pygame.display.set_mode(self.config_display)
		self.map = None
		self.isStart= False
		self.Paused = False
		self.added = True
		self.stora = True
		self.citAdd = False
		self.PreviewIndice = 0
		self.listeClique = []
		self.CliqueSora = []
		self.listeCliqueAdd =[]
		self.listePnj = []
		self.NbPnj = 0
		self.speed = 100
	def start(self,maps):
		self.map = maps
		pygame.init()
		pygame.font.init()
		self.header = pygame.font.Font('../Libs/head.ttf', 50)
		self.submenu = pygame.font.Font('../Libs/menu.ttf', 35)
		self.crose = pygame.font.Font('../Libs/menu.ttf', 20)
		self.litle = pygame.font.Font('../Libs/menu.ttf', 15)
		pygame.display.set_caption("SandStoneBox-SandBox mode-Map :"+self.map.name)
		pygame.display.set_icon(PyImgLoad("../img/logo.png"))
		self.db_ui = []
		for i in range(9):
			self.db_ui.append(PyImgLoad("../img/UI/"+str(i)+".png"))
		self.isStart = True
		self.map.start(self.display)
		self.coordAdd = (0,64)
		self.coordStora = (640,64)
		self.adderPage = 1
	def Show(self):
		self.display.fill((0,0,0))
		self.map.Show()
		for i in range(self.NbPnj):
			citi = self.listePnj[i]
			self.display.blit(citi.string()[0],citi.string()[1])
		for y in self.map.struct:
			for x in y:
				if x!= None:
					x.live()
		if self.Paused:
			self.showMenu()
		self.showAdd()
		self.ShowStorage()
		if self.citAdd :
			self.showAddCiti()
		pygame.display.update()
	def showMenu(self):
		self.display.blit(PyPrint("Menu-Option",(80,80,36),self.header),(200,80))
		self.display.blit(PyPrint("Menu-Option",(198,198,116),self.header),(200,60))
		self.display.blit(PyPrint("Save",(198,198,116),self.submenu),(200,150))
		self.display.blit(PyPrint("Setting",(198,198,116),self.submenu),(200,250))
		self.display.blit(PyPrint("Quit",(198,198,116),self.submenu),(200,350))
		pygame.display.update()
	def showAdd(self):
		if self.added :
			self.display.blit(self.db_ui[0],self.coordAdd)
			self.display.blit(PyPrint("-",(30,30,16),self.crose),(self.coordAdd[0]+7,self.coordAdd[1]+7))
			self.display.blit(PyPrint("Add Pnj",(30,30,16),self.crose),(self.coordAdd[0]+27,self.coordAdd[1]+7))
			self.display.blit(PyPrint("Create",(30,30,16),self.crose),(self.coordAdd[0]+17,self.coordAdd[1]+37))
			self.display.blit(PyPrint("Random",(30,30,16),self.crose),(self.coordAdd[0]+17,self.coordAdd[1]+67))
			self.listeClique =[]
			self.listeClique.append([[self.coordAdd[0]+30,self.coordAdd[0]+100],[self.coordAdd[1],self.coordAdd[1]+84]])
			self.listeClique.append([[self.coordAdd[0]+7,self.coordAdd[0]+27],[self.coordAdd[1]+7,self.coordAdd[1]+27]])
			self.listeClique.append([[self.coordAdd[0]+17,self.coordAdd[0]+87],[self.coordAdd[1]+37,self.coordAdd[1]+90]])
		else :
			self.display.blit(self.db_ui[1],self.coordAdd)
			self.display.blit(PyPrint("+",(30,30,16),self.crose),(self.coordAdd[0]+7,self.coordAdd[1]+7))
			self.display.blit(PyPrint("Add Pnj",(30,30,16),self.crose),(self.coordAdd[0]+27,self.coordAdd[1]+7))
			self.listeClique = []
			self.listeClique.append([[self.coordAdd[0]+30,self.coordAdd[0]+100],[self.coordAdd[1],self.coordAdd[1]+84]])
			self.listeClique.append([[self.coordAdd[0]+7,self.coordAdd[0]+27],[self.coordAdd[1]+7,self.coordAdd[1]+27]])
			self.listeClique.append([[0,0],[0,0]])
		pygame.display.update()
	def moveAdd(self,x,y):
		if x-50<0 :
			x = 50
		if y-10<0:
			y = 10
		self.coordAdd = (x-50,y-10)
		self.listeClique[0] =[[self.coordAdd[0]+30,self.coordAdd[0]+100],[self.coordAdd[1],self.coordAdd[1]+84]]
		self.listeClique[1] = [[self.coordAdd[0]+7,self.coordAdd[0]+27],[self.coordAdd[1]+7,self.coordAdd[1]+27]]
		self.showAdd()
	def closeAdd(self):
		if self.added :
			self.added = False
		else :
			self.added = True
		self.showAdd()
	def addCitizen(self):
		self.citAdd = True
		self.jobs = "Farmer"
	def showAddCiti(self):
		self.listeCliqueAdd =[]
		self.display.blit(self.db_ui[2],(300,300))
		self.display.blit(self.db_ui[3],(410,315))
		self.display.blit(self.db_ui[1],(350,420))
		self.PreviewIndice = (self.PreviewIndice+1)%Nb_img[self.jobs]
		preview = PyImgLoad('../img/Pnj/'+self.jobs+'/'+str(self.PreviewIndice)+'.png')
		self.display.blit(PyPrint("Preview",(30,30,16),self.crose),(305,320))
		self.display.blit(preview,(310,330))
		self.display.blit(PyPrint(self.jobs,(30,30,16),self.crose),(305,390))
		self.display.blit(PyPrint("No name",(30,30,16),self.litle),(315,302))
		self.display.blit(PyPrint("Jobs",(30,30,16),self.crose),(418,320))
		self.display.blit(PyPrint(str(self.adderPage)+"/"+str(len(listeJobs)-1),(30,30,16),self.crose),(478,320))
		for i in range(len(listeJobs[self.adderPage])):
			name = listeJobs[self.adderPage][i]
			txt = PyPrint(name,(30,30,16),self.crose)
			self.display.blit(txt,(420,345+i*30))
			self.listeCliqueAdd.append([[420,420+txt.get_size()[0]],[345+i*30,(345+i*30)+txt.get_size()[1]]])
		if self.adderPage< len(listeJobs)-1:
			txt = PyPrint(">",(30,30,16),self.crose)
			self.display.blit(txt,(490,395))
			self.listeCliqueAdd.append([[490,490+txt.get_size()[0]],[395,395+txt.get_size()[1]]])
		else :
			txt = PyPrint("",(30,30,16),self.crose)
			self.display.blit(txt,(490,395))
			self.listeCliqueAdd.append([[490,490+txt.get_size()[0]],[395,395+txt.get_size()[1]]])

		if self.adderPage>1 :
			txt = PyPrint("<",(30,30,16),self.crose)
			self.display.blit(txt,(415,395))
			self.listeCliqueAdd.append([[415,415+txt.get_size()[0]],[395,395+txt.get_size()[1]]])
		else :
			txt = PyPrint("",(30,30,16),self.crose)
			self.display.blit(txt,(415,395))
			self.listeCliqueAdd.append([[415,415+txt.get_size()[0]],[395,395+txt.get_size()[1]]])
		txt = PyPrint("Add !",(30,30,16),self.crose)
		self.display.blit(txt,(375,425))
		self.listeCliqueAdd.append([[375,375+txt.get_size()[0]],[425,425+txt.get_size()[1]]])

		pygame.display.update()
	def PlayCiti(self):
		self.NbPnj +=1
		pnj = Pnj[self.jobs](self.NbPnj,self.map)
		pnj.start()
		self.listePnj.append(pnj)
		self.citAdd = False 
	def ShowStorage(self):
		if self.stora:
			self.display.blit(self.db_ui[0],self.coordStora)
			self.display.blit(PyPrint("-",(30,30,16),self.crose),(self.coordStora[0]+7,self.coordStora[1]+7))
			self.display.blit(PyPrint("Storage",(30,30,16),self.crose),(self.coordStora[0]+27,self.coordStora[1]+7))
			for i in range(2):
				self.display.blit(PyPrint(self.map.capa[i]+str(self.map.stock[i])+"/"+str(self.map.Storage[i]),(30,30,16),self.litle),(self.coordStora[0]+7,self.coordStora[1]+30+i*38))
				if self.map.Storage[i] != 0 :
					ca = int(((self.map.stock[i]*100)/self.map.Storage[i])//20)
					if ca == 0:
						ca = 1
					for x in range(ca):
						if ca <= 2:
							self.display.blit(self.db_ui[5],(self.coordStora[0]+7+x*18,self.coordStora[1]+45+i*38))
						elif ca > 2 and ca <= 4 :
							self.display.blit(self.db_ui[8],(self.coordStora[0]+7+x*18,self.coordStora[1]+45+i*38))
						elif ca >= 5:
							self.display.blit(self.db_ui[6],(self.coordStora[0]+7+x*18,self.coordStora[1]+45+i*38))


			self.CliqueSora=[]
			self.CliqueSora.append([[self.coordStora[0]+30,self.coordStora[0]+100],[self.coordStora[1],self.coordStora[1]+84]])
			self.CliqueSora.append([[self.coordStora[0]+7,self.coordStora[0]+27],[self.coordStora[1]+7,self.coordStora[1]+27]])
		else :
			self.display.blit(self.db_ui[1],self.coordStora)
			self.display.blit(PyPrint("+",(30,30,16),self.crose),(self.coordStora[0]+7,self.coordStora[1]+7))
			self.display.blit(PyPrint("Storage",(30,30,16),self.crose),(self.coordStora[0]+27,self.coordStora[1]+7))
			self.CliqueSora=[]
			self.CliqueSora.append([[self.coordStora[0]+30,self.coordStora[0]+100],[self.coordStora[1],self.coordStora[1]+84]])
			self.CliqueSora.append([[self.coordStora[0]+7,self.coordStora[0]+27],[self.coordStora[1]+7,self.coordStora[1]+27]])
		pygame.display.update()
	def moveStora(self,x,y):
		if x-50<0 :
			x = 50
		if y-10<0:
			y = 10
		self.coordStora = (x-50,y-10)
		self.CliqueSora[0] =[[self.coordStora[0]+30,self.coordStora[0]+100],[self.coordStora[1],self.coordStora[1]+84]]
		self.ShowStorage()
	def closeStora(self):
		if self.stora :
			self.stora = False
		else :
			self.stora = True
		self.ShowStorage()






