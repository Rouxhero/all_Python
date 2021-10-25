# coding: utf-8 

from Tkinter import * 
from tkMessageBox import *
from module import *
root = Tk()
screenW = int(root.winfo_screenwidth()*0.75)
screenH = int(root.winfo_screenheight()*0.75)
root.destroy()
Main = Tk()
Main.title('MaTh')

Head =LabelFrame(Main, text="Graph",borderwidth=2,width=screenW, height=screenH, relief=GROOVE)

menubar = Menu(Main)

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="New",command=New )
menu1.add_command(label="Open",command=Coming_soon  )
menu1.add_separator()
menu1.add_command(label="Quitter",  command=Main.quit)
menubar.add_cascade(label="Fichier", menu=menu1)

menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="Fonction",command=Coming_soon  )
menu2.add_command(label="Graph" ,command=Graph_Option  )
menu2.add_command(label="value",command=Coming_soon )
menubar.add_cascade(label="Tools", menu=menu2)

menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="A propos",command=Coming_soon    )
menubar.add_cascade(label="Aide", menu=menu3,)

Main.config(menu=menubar)
def graph_get():
	O_x = 0
	O_y = 0
	S_x = 1
	S_y = 1
	opt = open('Graph.option','r').readlines()
	for i in range(0,4):
		text = ''
		for ii in range(0,(len(opt[i])-1)):
			text += opt[i][ii]
			print text
		opt[i] = int(text)
	if opt[0] != '' and  opt[1] != '' and  opt[2] != '' and  opt[3] != '':
		O_x = opt[0]
		O_y = opt[1]
		S_x = opt[2]
		S_y = opt[3]
	return O_x,	O_y,S_x,S_y
# Graph
graph = Canvas(Head,width=screenW, height=screenH, background='beige')
O_x,	O_y,S_x,S_y=graph_get()
axeY = graph.create_line(screenW, screenH-20, 0, screenH-20)
axeX = graph.create_line(20, screenH,20, 0)
origineX = graph.create_text(30, screenH-5,text=str(O_x), font="Arial 12 ", fill="blue")
origineY = graph.create_text(10, screenH-30, text=str(O_y), font="Arial 12 ", fill="blue")
graph.pack(padx=10,pady=10)
def actu():
	O_x,	O_y,S_x,S_y=graph_get()
	clear = graph.create_rectangle(0,0,screenW+10,screenH+10,fill='beige')
	axeY = graph.create_line(screenW, screenH-20, 0, screenH-20)
	axeX = graph.create_line(20, screenH,20, 0)
	origineX = graph.create_text(30, screenH-5,text=str(O_x), font="Arial 12 ", fill="blue")
	origineY = graph.create_text(10, screenH-30, text=str(O_y), font="Arial 12 ", fill="blue")
	graph.pack(padx=10,pady=10)
def clavier(event):
    touche = event.keysym
    if touche =='F5':
    	actu()

graph.focus_set()
graph.bind("<Key>", clavier)


Head.pack(side=TOP)

Main.mainloop()
