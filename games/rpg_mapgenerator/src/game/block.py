from src.function import *
from src.game.blockdata import tree,SIZE,load_image


class Block:

    def __init__(self,data:dict,pos:tuple,asset:dict):
        self.asset = asset
        self.image = asset[data["image"]]
        self.type  = data['type']
        self.pos   = pos
        self.element = []

    def display(self,screen):
        screen.blit(self.image,self.pos)
        for e in self.element:
            screen.blit(e,self.pos)

    def displayTo(self, screen, x, y, zoom):
        # On calcule les nouvelles dimensions de l'image en fonction du zoom
        new_width = int(SIZE * zoom)
        new_height = int(SIZE * zoom)
        # On redimensionne l'image
        resized_image = pygame.transform.smoothscale(self.image, (new_width, new_height))
        # On dessine l'image redimensionnée
        screen.blit(resized_image, (x, y))
        # On redimensionne les éléments et on les dessine à leurs nouvelles coordonnées
        for e in self.element:
            new_element = pygame.transform.smoothscale(e, (new_width, new_height))
            screen.blit(new_element, (x, y))



    def has_tree(self):
        self.element.append(self.asset[tree['image']])
