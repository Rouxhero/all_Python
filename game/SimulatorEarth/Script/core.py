from pop import *
from utile import *

class core:

	def __init__(self,Name):
		self.name = Name
		self.listePoP = []
		self.year = 0
		self.history = []
		self.nbtest = 0
		clear()
	def addPop(self,pop):
	    self.listePoP.append(pop)
	    pop.start()
	def ClearH(self):
		self.history = []
	def show_info(self):
		nam = [("Earth : "+self.name,"Number of Test"+ str(self.nbtest)),("Nb of Civilisation : "+str(len(self.listePoP)),"X")]
		afficheTableau(nam)
	def Test(self,time,p):
		ii = 0
		for pop in self.listePoP:
			pop.LaunchSim= True
		for i in range(time*5):
			Affichage = [("Nom","Age","Citoyen","Birth","Death")]
			for pop in self.listePoP:
				Affichage.append(pop.toString())
			afficheTableau(Affichage)
			print(["/","-","\\","|"][ii]+["... ","..  ",".   ","...."][ii]+str((time)-i//5)+"year(s) left")
			ii = (ii+1)%4		
			pause(p)
			clear()
		for i in self.listePoP:
			i.LaunchSim = False
		Affichage = [("Nom","Age","Citoyen","Birth","Death")]
		for pop in self.listePoP:
			Affichage.append(pop.toString())
		afficheTableau(Affichage)
		input("Test finish, press Return to quit")
	def Show(self):
		Affichage = [("Number","Name")]
		for pop in range(len(self.listePoP)):
			Affichage.append((str(pop),self.listePoP[pop].name))
		self.history.append(table_to_str(Affichage))
		afficheTableau(Affichage)
