from map import *
from pnj import *
from menu import *
import os

def clear():
	if os.name=='posix':
		os.system('clear')
	else:
		os.system('cls')

main = Map()
continu = True
main.init_Struct()
main.show_map()	
edi = Editor(main)	
main.editor = edi
edi.start()
clear()
while continu :
	main.tick()
	for event in pygame.event.get():  
		if event.type == QUIT:    
			continu = 0 
		if event.type == KEYDOWN:
			if event.key == K_e:
				print('e')
		if event.type == MOUSEBUTTONDOWN and event.button == 1 :
			x = event.pos[0] 
			y = event.pos[1]
			if main.map_st[y//64][x//64] != None:
				main.map_st[y//64][x//64].cut()
			if main.select != None:
				main.listepnj[main.select].body.goto(x,y)
	
	main.show_map()
	main.show_dead_pnj()
	main.show_pnj()
	main.update()	