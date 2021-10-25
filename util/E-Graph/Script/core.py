# -*- coding: utf-8 -*-

class Core :

	def __init__(self):
		self.board = []

	def initBoard(self,maxs):
		a = []
		for i in range(maxs):
			a.append(None)
		for i in range(maxs):
			self.board.append(list(a))
	def insertValue(self,x,y,value):
		try : 
			self.board[y][x] = value;
		except IndexError :
			print('Error')

	def getValue(self,x,y):
		try : 
			return self.board[y][x];
		except IndexError :
			print('Error')


















if __name__ == "__main__":
	body = Core()
	body.initBoard(30)
	body.insertValue(0,0,"3 + 5")
	body.insertValue(1,0,eval(body.getValue(0,0)))
	for i in body.board:
		for ii in i:
			print(ii,end='|')
		print('')