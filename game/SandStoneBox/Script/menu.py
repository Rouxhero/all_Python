from Function import *

class Menu :
	"""docstring for Map"""
	def __init__(self):
		self.type="Menu"
		self.clock = pygame.time.Clock()
		self.y = 0
		self.up = True
		self.ym = 20
		self.upm = True
		self.continu = True
	def start(self):
		pygame.init()
		pygame.font.init()
		self.header = pygame.font.Font('../Libs/head.ttf', 64)
		self.submenu = pygame.font.Font('../Libs/menu.ttf', 42)
		self.display = pygame.display.set_mode((768,640))
		pygame.display.set_caption("SandStoneBox")
		pygame.display.set_icon(PyImgLoad("../img/logo.png"))
	def anime_title(self):
		if self.up :
			self.y += 1
		else :
			self.y -= 1
		if self.y > 20:
			self.up = False
		elif self.y < 0 :
			self.up = True
	def anime_menu(self):
		if self.upm :
			self.ym += 1
		else :
			self.ym -= 1
		if self.ym > 20:
			self.upm = False
		elif self.ym < 0 :
			self.upm = True

	def Show(self):
		self.anime_title()
		self.fond = PyImgLoad("../img/menu.png")
		self.display.blit(self.fond,(0,0))
		self.display.blit(PyPrint("SandStoneBox",(80, 80, 36),self.header),(140,158))
		self.display.blit(PyPrint("SandStoneBox",(198,198,116),self.header),(140,128-self.y))
		self.display.blit(PyPrint("Start SandBox mode",(80,80,36),self.submenu),(220,248))
		self.display.blit(PyPrint("Start SandBox mode",(158,255,218),self.submenu),(220,235))
		self.display.blit(PyPrint("Start Level mode",(80,80,36),self.submenu),(240,348))
		self.display.blit(PyPrint("Start Level mode",(158,255,218),self.submenu),(240,335))
		self.display.blit(PyPrint("Setting",(80,80,36),self.submenu),(300,448))
		self.display.blit(PyPrint("Setting",(158,255,218),self.submenu),(300,435))
		self.display.blit(PyPrint("Quit",(80,80,36),self.submenu),(320,548))
		self.display.blit(PyPrint("Quit",(158,255,218),self.submenu),(320,535))
		pygame.display.update()
	def Menu_Cursor(self,x,y):
		if x > 209 and x < 609:
			if y > 228 and y < 264:
				return 0
		if x > 233 and x < 558 :
			if y > 335 and y < 361:
				return 1
		if x > 295 and x < 443:
			if y > 443 and y < 467:
				return 2
		if x > 310 and x < 402:
			if y > 528 and y < 561:
				self.continu = False
		else :
			return None
	def hover(self,x,y):
		self.anime_menu()
		if x > 209 and x < 609:
			if y > 228 and y < 264:
				self.display.blit(PyPrint("Start SandBox mode",(80,80,36),self.submenu),(220,248))
				self.display.blit(PyPrint("Start SandBox mode",(198,198,116),self.submenu),(220,235))
		if x > 233 and x < 558 :
			if y > 335 and y < 361:
				self.display.blit(PyPrint("Start Level mode",(80,80,36),self.submenu),(240,348))
				self.display.blit(PyPrint("Start Level mode",(198,198,116),self.submenu),(240,335))
		if x > 295 and x < 443:
			if y > 443 and y < 467:
				self.display.blit(PyPrint("Setting",(80,80,36),self.submenu),(300,448))
				self.display.blit(PyPrint("Setting",(198,198,116),self.submenu),(300,435))
		if x > 310 and x < 402:
			if y > 528 and y < 561:
				self.display.blit(PyPrint("Quit",(80,80,36),self.submenu),(320,548))
				self.display.blit(PyPrint("Quit",(198,198,116),self.submenu),(320,535))
		else :
			return None
		pygame.display.update()

	def tick(self):
		self.clock.tick(15)
