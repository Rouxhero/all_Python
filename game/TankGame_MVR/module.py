# coding: utf-8 
import pygame
import os

def clss():
	os.system('cls')
def load_image():
	db_img = []
	db_img2 = []
	print 'getting image :',
	for i in range(10):
		print '.',
		db_img += pygame.image.load('img/'+str(i)+'.png'),
	for i in range(4):
		print '.',
		db_img2 += pygame.image.load('img/1'+str(i)+'.png'),
	print '\ngetting image : done'
	return db_img,db_img2

def new_scale(db,db2,scale):
	new_db = []
	new_db2 = []
	print 'preparing image :',
	for i in db :
		print '.',
		new_db += pygame.transform.scale(i,(scale,scale)),
	for i in db2 :
		print '.',
		new_db += pygame.transform.scale(i,(scale,scale/2)),
	print '\npreparing image : done'
	return new_db
def tourner(player,angle):
	return pygame.transform.rotate(player,angle)