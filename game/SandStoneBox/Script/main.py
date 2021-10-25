from menu import *
from sandbox import *
#from Loading import *


mainG = Menu()
mainG.start()
choix = None
pygame.key.set_repeat(400, 30)
while mainG.continu :
	mainG.tick()
	for event in pygame.event.get():  
		if event.type == QUIT:    
				mainG.continu = False
				if mainG.type=="IA":
					if mainG.mainG.isStart:
						mainG.mainG.map.end = True
		if event.type == KEYDOWN:
			if event.key == 27:
				if mainG.mainG.Paused : 
					mainG.mainG.Paused = False
				else :
					mainG.mainG.Paused = True
			if event.key == K_e:
				mainG.mainG.map.stock[0] +=10
		if event.type == MOUSEMOTION :
				x = event.pos[0] 
				y = event.pos[1]
				if mainG.type=="IA" and event.buttons[0] == 1:
					if mainG.mainG.isStart:
						mainG.moveWindow(x,y)
				
		if event.type == MOUSEBUTTONDOWN and event.button == 1 :
				x = event.pos[0]
				y = event.pos[1]
				choix = mainG.Menu_Cursor(x,y)
	if mainG.type == "Menu":
		mainG.hover(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])

	if choix == 0:
		mainG = Sandbox()
		mainG.start()
		choix = None
	mainG.Show()