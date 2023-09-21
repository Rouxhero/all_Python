from src.game.block import Block
from src.game.blockdata import *
from noise import pnoise2
import pygame

from src.variable import *

load = ["/","|","\\","--"]


class Map:
    def __init__(self,asset,screen, width=0, height=0, map=None):
        self.width = width
        self.height = height
        self.grid = []
        self.asset = asset
        if map is None:
            self.__init_map(screen)
        else:
            self.grid = map

    def __init_map(self,screen):
        step =100/(self.width*self.height)
        # Création d'une police pour le titre
        font = pygame.font.Font(None, 36)

        # Initialisation de la barre de progression
        progress_rect = pygame.Rect(100, 200, 600, 20)
        progress_color = pygame.Color('green')
        progress = 0
        index = 0
        
        for x in range(self.width):
            row = []
            title_text = 'Génération de la carte '+load[index]
            title_surface = font.render(title_text, True, pygame.Color('white'))
            for y in range(self.height):
                screen.fill((0, 0, 0))
                screen.blit(title_surface, (100, 150))
                pygame.draw.rect(screen, pygame.Color('white'), progress_rect, 2)
                pygame.draw.rect(screen, progress_color, (progress_rect.x, progress_rect.y, progress_rect.width * progress / 100, progress_rect.height)) 
                pygame.display.flip()
                progress += step
                value = pnoise2(x * SCALE, y * SCALE, OCTAVES, PERSISTENCE, LACUNARITY)
                if value < -0.4:
                    b = Block(water,(x*SIZE,y*SIZE),self.asset)
                elif value < 0.2:
                    b = Block(grass,(x*SIZE,y*SIZE),self.asset)
                else:
                    b = Block(stone,(x*SIZE,y*SIZE),self.asset)
                trees_value = pnoise2(x * SCALE_TREES, y * SCALE_TREES, OCTAVES_TREES, PERSISTENCE_TREES, LACUNARITY_TREES)
                if trees_value > TREE_DENSITY and b.type == "grass":
                    b.has_tree()
                row.append(b)
            self.grid.append(row)
            index = (index+1)%4

    def get_block(self, x, y):
        return self.grid[x][y]

    def set_block(self, x, y, block):
        self.grid[x][y] = block

    def render(self, display):
        for x in range(self.width):
            for y in range(self.height):
                self.grid[x][y].display(display)
                