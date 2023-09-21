

import pygame,os
from src.game.blockdata import SIZE,IMAGE_PATH


WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,255,0)
GREEN = (0,0,255)

CENTERX = lambda surface,config,px,py : ((config.get("width") - surface.get_width()) / 2,py)
CENTERY = lambda surface,config,px,py : (px,(config.get("height") - surface.get_height()) / 2)

def title(text:str,size:int=15,color:tuple=WHITE,font:str=None):
    font = pygame.font.Font(font, size)
    return font.render(text, True,color)


