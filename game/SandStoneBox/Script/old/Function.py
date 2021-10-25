import os
import pygame
from pygame.locals import *


	
def clear():
	if os.name=="posix":
		os.system('cls')
	else :
		os.system('clear')

def printl(text):
	print(text,end="")

def PyImgLoad(path):
	return pygame.image.load(path)

def PyPrint(text,color,font):
	return font.render(text, False, color)

