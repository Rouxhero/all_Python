# Class map for gameObject
# Made By Rouxhero*
import pygame
from random import randint as r


class Map:
    def __init__(self):
        self.idL = 0
        self.map = []
        self.mapC = []
        self.spritDB = []

    def load_Sprit(self):
        for i in range(2):
            self.spritDB.append(
                pygame.image.load("../img/map/block_" + str(i) + ".png")
            )

    def MapGen(self):
        self.idL += 1
        self.map = []
        self.map.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        line = []
        for Y in range(6):
            line.append(0)
            for X in range(8):
                if Y == 0 and X == 0:
                    line.append(1)
                else:
                    pr = r(0, 100)
                    if pr < 20:
                        line.append(0)
                        self.mapC.append(
                            [
                                (X + 1) * 64,
                                (Y + 1) * 64,
                            ]
                        )
                    else:
                        line.append(1)
            line.append(0)
            self.map.append(line)
            line = []
        self.map.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
