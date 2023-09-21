

from pygame import MOUSEMOTION, MOUSEBUTTONDOWN
from src.core.gameInstance import GameInstance
from src.function import BLACK, CENTERX, RED, title
from src.core.scene import Scene


class MainMenu(Scene):

    def __init__(self,game)->None:
        """
        Constructor for MainMenu class

        Args:
            game (Game): The father
        """
        super(MainMenu,self).__init__(game)
        self.titleT = title("RPG PyGame",45)
        self.playT = title("Play",25)
        self.settingT = title("Setting",25)
        self.quitT = title("Quit",25)


    def catch(self, event) -> None:
        """
        Catch pygame events

        Args:
            event (Event): Event
        """
        if event.type == MOUSEMOTION:
            x,y = event.pos
            if x >= 250 and x <= 250+self.playT.get_width() and y >= 240 and y <= 240+self.playT.get_height():
                self.playT = title("Play",25,RED)
            else:
                self.playT = title("Play",25) 
            if x >= 250 and x <= 250+self.settingT.get_width() and y >= 340 and y <= 340+self.settingT.get_height():
                self.settingT = title("Setting",25,RED)
            else:
                self.settingT = title("Setting",25)
            if x >= 250 and x <= 250+self.quitT.get_width() and y >= 440 and y <= 440+self.quitT.get_height():
                self.quitT = title("Quit",25,RED)
            else:
                self.quitT = title("Quit",25)
        if event.type == MOUSEBUTTONDOWN :
            x,y = event.pos
            if x >= 250 and x <= 250+self.playT.get_width() and y >= 240 and y <= 240+self.playT.get_height():
                self.game.current_scene = self.game.scene[1]
            if x >= 250 and x <= 250+self.settingT.get_width() and y >= 340 and y <= 340+self.settingT.get_height():
                self.game.scene = [self.game.settingScene]
                self.game.current_scene = self.game.scene[0]
            if x >= 250 and x <= 250+self.quitT.get_width() and y >= 440 and y <= 440+self.quitT.get_height():
                self.game.running = False

    def play(self)->None:
        """
        Play the scene on tick
        """
        self.game.display.fill((BLACK))
        self.game.display.blit(self.titleT,(250,140))
        self.game.display.blit(self.playT,(250,240))
        self.game.display.blit(self.settingT,(250,340))
        self.game.display.blit(self.quitT,(250,440))