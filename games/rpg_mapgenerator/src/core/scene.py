


class Scene:
    """
    Scene class is the base class for all scenes in the game.
    """
    def __init__(self,game)->None:
        """
        Constructor for Scene class

        Args:
            game (Game): Father
        """
        self.game = game
        self.config = game.config
        self.display = game.display
        self.clock = game.clock
        self.tick = 60
    
    def catch(self,event)->None:
        """
        Catch pygame events

        Args:
            event (Event): The pygame Event to cactch
        """
        pass

    def play(self)->None:
        """
        Play the scene on tick
        """
        pass