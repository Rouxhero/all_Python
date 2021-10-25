# coding: utf-8 
from Tkinter import * 
from tkMessageBox import *
#Main Module

def Coming_soon():
	showinfo('Coming soon', 'Cette fonctionnalité arrive bientôt !!')

def New():
	def fct1():
		def ok():
			aa = a.get()
			bb = b.get()
			open('temp1','w').write(aa)
			open('temp2','w').write(bb)
			fct.destroy()
			ask.destroy()
		fct = Tk()
		fct.title('Entrez les valeur')
		Label(fct,text=' Vous avez choisi la fonction y=ax+b\n entrez les valeur de a et b').pack(pady=10)
		Label(fct,text='y=').pack(side=LEFT)
		a = Entry(fct, width=5)
		a.pack(side=LEFT)
		Label(fct,text='x +').pack(side=LEFT)
		b = Entry(fct, width=5)
		b.pack(side=LEFT)
		Button(fct,text='Valider',command=ok).pack(side=BOTTOM)
		fct.mainloop()
	ask = Tk()
	ask.title('Select a fonction')
	Label(ask,text="De nouvelle fonctions serons\n ajoutées ulterieurement").pack(side =TOP)
	Button(ask,text='  ',command=fct1).pack(side = LEFT,padx=10,pady=10)
	Label(ask,text="y = ax+b").pack(side = LEFT,padx=10,pady=10)
	ask.mainloop()


def Graph_Option():
	def okk():
		x = O_x.get()
		y = O_y.get()
		xx= S_x.get()
		yy = S_y.get()
		text = x+"\n"+y+"\n"+xx+"\n"+yy+"\n"
		open('Graph.option','w').write(text)
		ask.destroy()
	ask = Tk()
	ask.title('Graph Option')
	Label(ask,text="Entrez l'origine du graph et les scales").pack(side =TOP)
	fct1 = LabelFrame(ask,text='Option Origine')
	fct2 = LabelFrame(ask,text='Option Scale')
	Label(fct1,text='Origine X :').pack(side=LEFT,pady=20)
	O_x = Entry(fct1, width=5)
	O_x.pack(side=LEFT,padx=10)
	Label(fct1,text='Origine Y :').pack(side=LEFT)
	O_y = Entry(fct1, width=5)
	O_y.pack(side=LEFT,padx=10)
	Label(fct2,text='Scale X :').pack(side=LEFT,pady=20,padx=10)
	S_x = Entry(fct2, width=5)
	S_x.pack(side=LEFT,padx=10)
	Label(fct2,text='Scale X :').pack(side=LEFT)
	S_y = Entry(fct2, width=5)
	S_y.pack(side=LEFT)
	fct1.pack()
	fct2.pack()
	Button(ask,text='Valider',command=okk).pack()
	ask.mainloop()