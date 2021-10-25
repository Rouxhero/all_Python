#Class Population
import threading
from random import randint
from time import sleep as pause
from utile import *
from math import floor
class Population(threading.Thread) :
	def __init__(self,Name,Liste):
		threading.Thread.__init__(self)
		self.name = Name
		self.age = 0 #Year
		self.ListOfPop = Liste
		self.pop = 2
		self.end = False
		self.birth = 2
		self.death = 0.05
		self.LaunchSim = False
		self.ParamSim = False
		self.enfant=0
		self.mort=0
	def toString(self):
		return (self.name,Convert(self.age),Convert(self.pop),Convert(self.enfant),Convert(self.mort))
	def terminate(self): 
		self._running = False
		self.end = True
	def run(self):
		while not self.end:
			if self.LaunchSim == True :
				if self.ParamSim == False:
					self.age = 0 #Year
					self.pop = 2
					self.birth = 2
					self.enfant =0
					self.mort=randint(2,15)/100
					self.ParamSim = True
				self.enfant = floor(self.birth*(self.pop*0.3))
				self.mort = floor(self.pop*self.death)
				self.pop += self.enfant - self.mort
				self.age += 1
				
			else:
				
				if self.ParamSim:
					self.ParamSim = False
			pause(0.5)