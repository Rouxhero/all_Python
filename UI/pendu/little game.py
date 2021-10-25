# coding: utf-8 
from Tkinter import *
from tkMessageBox import *
from os import system
from random import randint as r
dico = []
print 'loading data :',
f=open('dico.txt','r')
while 1:
	data=f.readline()
	if not data:
		break
	dico += data,
print 'ok'
def cls():
	system('cls')

def commingsoon():
	showinfo('Comming soon !','Comming soon !')

def getW():
	return dico[r(0,len(dico))]


def game():
	loadingM.destroy()
	word = getW()
	words = []
	for i in word :
		words += i,
	trys = 0
	entre =  Entry(loading, width=30)

	def chek():
		entres =entre.get()
		if entres in words :
			x,y = True,1
		else :
			x,y = False,1
		print x,y

	txt = '_ '*(len(word)-1)
	txt += '  ' +str(len(word)-1)+word
	text = Label(loading,text=txt)
	Button(loading,text='chek',command=chek).pack()
	text.pack()
	entre.pack()
	main.update()
	


system('@echo off')

main = Tk()
main.title('TeSt')

loading = LabelFrame(main,text='made by LL\'s games')
loadingM = Frame(loading)


Button(loadingM,text='Start',command=game).pack(padx=10,pady=20)
Button(loadingM,text='LeaderBord',command=commingsoon).pack(padx=10,pady=5)
Button(loadingM,text='Option',command=commingsoon).pack(padx=10,pady=20)

loading.pack()
loadingM.pack()
main.mainloop()
