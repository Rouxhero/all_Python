
import json
import pygame
from src.game.blockdata import load_asset
from src.components.load import LoadMenu

from src.components.mainmenu import MainMenu
from src.core.config import GameConfig
from src.variable import CONFIG_PATH



class Game:

    def __init__(self):
        self.config = None
        self.__load_config()
        self.__set_pygame()
        self.scene = [MainMenu(self),LoadMenu(self)]
        self.current_scene = self.scene[0]  
        self.running = True  
        self.run()

    def __set_pygame(self):
        pygame.init()
        pygame.transform.set_smoothscale_backend('MMX')  # Choisissez la méthode de lissage appropriée
        pygame.display.set_caption(self.config.get('title'))
        self.display = pygame.display.set_mode((self.config.get('width'),self.config.get('height')))
        self.clock = pygame.time.Clock()
        self.asset = load_asset()
        

    def __load_config(self):
        with open(CONFIG_PATH,'r') as f:
            self.config = GameConfig(json.load(f))

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                self.current_scene.catch(event)
            self.current_scene.play()
            pygame.display.flip()
            self.clock.tick(self.current_scene.tick)


