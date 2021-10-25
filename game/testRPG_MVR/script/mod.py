# Script by Rouxhero
import pygame
from random import choice, randint


class Citizen:
    """"""

    def __init__(self, i):
        self.ID = i
        self.x = 70
        self.y = 70
        self.Sprit = []
        self.setWH = []
        self.setMapC = []
        self.PlayerSprit = pygame.image.load("../img/citizen/player_1.png")
        self.face = [[0, 10, 11], [1, 2, 3], [7, 8, 9], [4, 5, 6]]
        self.pat = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        self.WI = 0
        self.dir = 0
        self.choix = [0, 1, 2, 3]
        self.nb = 1
        self.ColisionBox = [[20, 20], [84, 84]]

    def Load_Sprit(self):
        for i in range(1, 13):
            self.Sprit.append(
                pygame.image.load("../img/citizen/player_" + str(i) + ".png")
            )

    def walk(self):
        self.PlayerSprit = self.Sprit[self.face[self.dir][self.WI]]
        self.WI = (self.WI + 1) % 3
        self.x, self.y = (
            self.x + self.pat[self.dir][0] * 5,
            self.y + self.pat[self.dir][1] * 5,
        )
        self.ColisionBox = [[self.x, self.y], [self.x + 64, self.y + 64]]

    def think(self, *args):
        if self.nb == 0 or args != ():
            self.dir = choice(self.choix)
            self.nb = randint(30, 100)
        else:
            self.nb -= 1
            self.dir = choice(self.choix)
            self.nb = randint(30, 100)
    def checkBorder(self):
        newx, newy = (
            self.x + self.pat[self.dir][0] * 5,
            self.y + self.pat[self.dir][1] * 5,
        )
        if newx > 64 and newx < self.setWH[0] - 128:
            if newy > 32 and newy < self.setWH[1] - 128:
                return False
        return True

    def checkBlock(self):
        newx, newy = (
            self.x + self.pat[self.dir][0] * 5,
            self.y + self.pat[self.dir][1] * 5+32,
        )
        for i in self.setMapC :
        	if newx > i[0] and newx < i[0]+64:
        		return True
        return False

class GameObject:
    def __init__(self):
        self.display = (640, 480)
        self.nbC = 0
        self.png = []
        self.colision = []
        self.maps = None
