import json
import pygame
from src.game.player import Player
from src.core.scene import Scene
from src.game.map import Map
from src.game.blockdata import SIZE
from src.variable import CONFIG_PATH, ZOOM_FACTOR, ZOOM_MAX, ZOOM_MIN

class GameInstance(Scene):

    def __init__(self,game,path=None):
        super(GameInstance,self).__init__(game)
        self.game = game
        self.map_x = 0
        self.map_y = 0
        self.key_press = False
        self.pause = False
        self.border  = lambda mx,x,s,z: -(((mx*int(s*z))-x)/2)
        self.player = Player(self.game.config.get('width') // 2, self.game.config.get('height') // 2,game.asset)
        # Définition des constantes de zoom
        self.zoom = 1
        if path is None:
            self.__init_map(game.display,game.asset)
        else:
            with open(path, 'r') as f:
                self.map = Map(game.asset,game.display,map = json.load(f))
        self.map_surface = pygame.Surface((self.game.config.get('map_width')*SIZE, self.game.config.get('map_height')*SIZE))

    def __init_map(self,screen,asset):
        self.map = Map(asset,screen,width = self.game.config.get('map_width'),height = self.game.config.get('map_height'))

    def catch(self,event)->None:
        """
        Catch pygame events

        Args:
            event (Event): The pygame Event to cactch
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.start_x,self.start_y = event.pos
                self.key_press = True
            elif event.button == 5:  # molette de la souris vers le haut
                self.zoom = round(max(self.zoom - ZOOM_FACTOR, ZOOM_MIN),2)
            elif event.button == 4:  # molette de la souris vers le bas
                self.zoom = round(min(self.zoom + ZOOM_FACTOR, ZOOM_MAX),2)

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self.key_press = False
            
        elif event.type == pygame.MOUSEMOTION:
                if self.key_press:
                    end_x, end_y = event.pos
                    self.map_x += end_x - self.start_x
                    self.map_y += end_y - self.start_y
                    self.start_x, self.start_y = event.pos
                if self.map_x > 0:
                    self.map_x = 0
                if self.map_y > 0:
                    self.map_y = 0
                border_bottom = self.border(self.game.config.get("map_height"),self.game.config.get('height'),SIZE,self.zoom)
                border_right = self.border(self.game.config.get("map_width"),self.game.config.get('width'),SIZE,self.zoom)
                # print(f"Calculate : \nwx = {self.game.config.get('map_height')}\nx = {self.game.config.get('height')}\ns = {SIZE}\nz = {self.zoom}")
                # print(f"Check  : {self.map_x}-{self.map_y} to {border_right}-{border_bottom}")
                if self.map_y < border_bottom:
                    self.map_y = border_bottom
                if self.map_x < border_right:
                    self.map_x = border_right
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.pause = not self.pause
            elif event.key == pygame.K_UP:
                self.player.move(0, -1)
            elif event.key == pygame.K_DOWN:
                self.player.move(0, 1)
            elif event.key == pygame.K_LEFT:
                self.player.move(-1, 0)
            elif event.key == pygame.K_RIGHT:
                self.player.move(1, 0)


    def play(self)->None:
        """
        Play the scene on tick
        """
        
        self.game.display.fill((0, 0, 0))
        if not self.pause:
            self.map_surface.fill((0, 0, 0))
            # Dessin de la map sur la surface map_surface
            for x in range(self.game.config.get("map_width")):
                for y in range(self.game.config.get("map_height")):
                    block = self.map.get_block(x, y)
                    x_pos = (x * int(SIZE * self.zoom)) + self.map_x
                    y_pos = (y * int(SIZE * self.zoom)) + self.map_y
                    block.displayTo(self.map_surface, x_pos, y_pos, self.zoom)
            
            # Dessin de la surface map_surface sur l'écran à la position map_x, map_y
            self.game.display.blit(self.map_surface, (self.map_x, self.map_y))
            self.player.display(self.game.display)
        else:
            self.game.display.blit(self.titleT,(250,140))
            self.game.display.blit(self.playT,(250,240))
            self.game.display.blit(self.settingT,(250,340))
            self.game.display.blit(self.quitT,(250,440))