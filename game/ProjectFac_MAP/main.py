import pygame
from pygame.locals import *
from game import *
from time import sleep as pause
from random import randint as r

DesertColor = "img/desert.png"
HillsColor = "img/hills.png"
PlainColor = "img/plain.png"
ForestColor = "img/tree.png"
seaColor = "img/sea.png"



pygame.init()
boardWith = 8
boardHeight = 8
surface = pygame.display.set_mode((900, 900))
pygame.key.set_repeat(400, 30)
boards = board(boardWith,boardHeight)
tileSize = (900//boardWith,900//boardHeight)

def createSurface(name, size):
    print(name)
    if type(name) == str:
        img = pygame.image.load(name)
        img = pygame.transform.scale(img, size)
    else :
        img = pygame.Surface(size)
        img.fill(name)
    return img
Tiles = {
    3: [
       "Hills",
        3,  # Coef
        createSurface(HillsColor, tileSize)
    ],
    2: [
        "Forest",
        1,  # Co,ef
        createSurface(ForestColor, tileSize)
    ],
    0: [
       "Sea",
        1,  # Coef
        createSurface(seaColor, tileSize)
    ],
    1: [
        "Plain",
        1,  # Coef
        createSurface(PlainColor, tileSize)
    ],
    4: [
        "Desert",
        1,  # Coef
        createSurface(DesertColor, tileSize)
    ],


}


def drawBoard():
    posY = -tileSize[1]
    for y in boards.board:
        posY += tileSize[1]
        posX = 0
        for x in y:
            surface.blit(Tiles[x][2], (posX, posY))
            posX += tileSize[0]

drawBoard()
pygame.display.update()
nbFirst = r(2,6)
for i in range(nbFirst):
    boards.genFirstTile()
    drawBoard()
    pygame.display.update()
for i in range(boards.getNbTile(nbFirst)-1):
    boards.OneOtherTile()
    drawBoard()
    pygame.display.update()
    pause(0.01)

play = True
while play:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = True
            exit()
   
