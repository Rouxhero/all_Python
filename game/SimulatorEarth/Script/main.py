
# coding: utf-8
from utile import *
from pop import *	 
from core import *
import re


create_reg = re.compile(r"[C][r][e][a][t][e].*")
def showH():
	clear()
	MainCore.show_info()
	for hi in MainCore.history:
		if type(hi)!=(str):
			for i in hi:
				print(i)
		else :
			print(hi)
def Create_Civ(*arg):
	if len(arg) == 1:
		MainCore.history.append("#>>Create "+arg[0])
		name = arg[0]
		showH()
	else :
		MainCore.history.append("#>>Create")
		showH()
		name = input("£ Input Name : ")
		MainCore.history.append("0 Input Name : "+name)
	pop  = Population(name,MainCore)
	MainCore.addPop(pop)
	MainCore.history.append("--> Civilation : "+name+" Added")
	print("--> Civilation : "+name+" Added")
def end():
	MainCore.history.append("#>>end")
	showH()
	print("Killing all civilation !")
	for i in MainCore.listePoP:
		i.end = True
		i.terminate() 

	exit()
def Show():
	MainCore.history.append("#>>Show")
	showH()
	MainCore.Show()

def Test():
	MainCore.history.append("#>>Test")
	showH()
	time = int(input("$ Input Number of year for Test : "))
	MainCore.history.append("0 Input Number of year for Test : "+str(time))
	pa = 0.05
	showH()
	MainCore.history.append("--> Finish")
	MainCore.Test(time,pa)
	showH()
def helps():
	MainCore.history.append("#>>help")
	showH()
	table = [("Commande","Argument","Info"),("Create","[name]","Create a new civilation"),("ClearH"," ","Clear History of cmd"),("Show","","Show All civilation"),("Test","","Test the Earth"),("end","","Leave the simulation")]
	MainCore.history.append(table_to_str(table))
	afficheTableau(table)
def ClearH():
	MainCore.ClearH()
	showH()
def command(choix):
	if choix=="":
		return 0
	if create_reg.match(choix) is not None and len(choix) != 6:
		name = choix[7:]
		Create_Civ(name)
	else :
		if choix in listeOfCommand:
			listeOfCommand[choix]()
		else :
			MainCore.history.append("/!\\ Unknow commande ! use \'help\' to get all command/!\\")
			print('/!\\ Unknow commande ! use \'help\' to get all command/!\\')
clear()
print("""
#################################
#                               #
#         Earh Simulator !      #
#                               #
#                               #
#           Good Game :)        #
#################################
Create by Rouxhero
			""")
print("Input Name for your Earth :")
choix = input(">>> ")
MainCore = core(choix)
listeOfCommand = {"Create":Create_Civ,"Test":Test,"Show":Show,"help":helps,"end":end,"ClearH":ClearH}
choix = ""

while choix != "end":
	showH()
	command(choix)	
	choix = input(">>> ")
end()