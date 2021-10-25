import pygame
from random import randint as r


class Character:
    def __init__(self, x, y, size):
        self.position = [x, y]
        self.size = size
        self.img = pygame.Surface((25, 25))
        self.img.fill((155, 105, 155))


class board:
    def __init__(self, width, height):
        self.board = list(list(0 for x in range(width)) for x in range(height))
        self.height = height
        self.width = width

    def genFirstTile(self):
        
        # First tile
        tile = r(1, 2)
        posX = r(1, self.width - 1)
        posY = r(1, self.height - 1)
        self.board[posY][posX] = tile

    def getNbTile(self,nbfirstTile):
        return  int(self.width * self.height * 0.33) - nbfirstTile




    def OneOtherTile(self):
        tile = r(1, 4)
        posX = r(1, self.width - 2)
        posY = r(1, self.height - 2)
        while not self.checkViability(1,posX, posY):
            posX = r(1, self.width - 2)
            posY = r(1, self.height - 2)
        self.board[posY][posX] = tile
    def genBoard(self):
        self.genFirstTile()
        nbTile = int(self.width * self.height * 0.33) - 1
        for tiles in range(nbTile-1):
            tile = r(1, 4)
            posX = r(1, self.width - 2)
            posY = r(1, self.height - 2)
            while not self.checkViability(tile,posX, posY):
                posX = r(1, self.width - 2)
                posY = r(1, self.height - 2)
            self.board[posY][posX] = tile

    def checkViability(self,typeT, x, y):
        if (
                self.board[y][x] == 0
                and (
                self.board[y - 1][x] != 0
                or self.board[y + 1][x] != 0
                or self.board[y][x - 1] != 0
                or self.board[y][x + 1] != 0
                )
        ):
            validy = False
            if typeT == 1 :
                validy = True
            elif typeT == 2 :
                validy = (self.board[y - 1][x] == 1
                or self.board[y + 1][x] == 1
                or self.board[y][x - 1] == 1
                or self.board[y][x + 1] == 1
                or self.board[y - 1][x] == 2
                or self.board[y + 1][x] == 2
                or self.board[y][x - 1] == 2
                or self.board[y][x + 1] == 2)
            elif typeT == 3 :
                validy = (self.board[y - 1][x] == 1
                or self.board[y + 1][x] == 1
                or self.board[y][x - 1] == 1
                or self.board[y][x + 1] == 1
                or self.board[y - 1][x] == 3
                or self.board[y + 1][x] == 3
                or self.board[y][x - 1] == 3
                or self.board[y][x + 1] == 3)
            elif typeT == 4 :
                validy = (self.board[y - 1][x] == 1
                or self.board[y + 1][x] == 1
                or self.board[y][x - 1] == 1
                or self.board[y][x + 1] == 1
                or self.board[y - 1][x] == 4
                or self.board[y + 1][x] == 4
                or self.board[y][x - 1] == 4
                or self.board[y][x + 1] == 4)
            return validy
        else:
            return False

    def checkBoard(self):
        for y in range(self.height):
            for x in (self.width):
                if self.board[y][x] != 0:
                    if self.board[y+1][x] == 0 and self.board[y-1][x] == 0 and self.board[y][x+1] == 0 and self.board[y][x-1] == 0 :
                        return self.board[y][x]
        return 0