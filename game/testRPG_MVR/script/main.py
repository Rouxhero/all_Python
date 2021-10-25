import pygame
from pygame.locals import *
from mod import *
from maps import *

game = GameObject()
game.maps = Map()
game.maps.load_Sprit()
game.maps.MapGen()
pygame.init()
surface = pygame.display.set_mode(game.display)
clock = pygame.time.Clock()
game.png = []


def ground():
    mapS = game.maps.map
    for Y in range(len(mapS)):
        for X in range(len(mapS[Y])):
            surface.blit(game.maps.spritDB[1], (X * 64, 32 + Y * 64))


def show_map():
    mapS = game.maps.map
    for Y in range(len(mapS)):
        for X in range(len(mapS[Y])):
            surface.blit(game.maps.spritDB[mapS[Y][X]], (X * 64, Y * 64))


def add_citizen():
    game.png.append(Citizen(game.nbC))
    game.png[game.nbC].setWH = game.display
    game.png[game.nbC].setmapC = game.maps.mapC
    game.png[game.nbC].Load_Sprit()
    game.colision.append(game.png[game.nbC].ColisionBox)
    game.nbC += 1


def updateCitizen():
    for citi in game.png:
        citi.setmapC = game.maps.mapC


def update_colid(ids):
    game.colision[ids] = game.png[ids].ColisionBox


continu = True
while continu:
    for event in pygame.event.get():
        if event.type == QUIT:
            continu = 0
        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                add_citizen()
            if event.key == K_r:
                game.maps.MapGen()
                updateCitizen()
    clock.tick(10)
    ground()
    show_map()
    for citi in game.png:
        citi.think()
        print(citi.checkBlock())
        while citi.checkBorder():
        	citi.think(1)
        while citi.checkBlock():
          	citi.think(1)
        citi.walk()
        update_colid(citi.ID)

        surface.blit(citi.PlayerSprit, (citi.x, citi.y))

    pygame.display.update()
