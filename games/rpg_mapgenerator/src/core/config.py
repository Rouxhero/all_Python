


class GameConfig:

    def __init__(self,config):
        self.config = config

    def get(self, key):
        if key in self.config:
            return self.config[key]
        else:
            return key
        
    def set(self,key,value):
        self.config[key] = value