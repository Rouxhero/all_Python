


class Player:

    def __init__(self, x,y,asset):
        self.x = x
        self.y = y
        self.image = asset["idle"]
        self.asset = asset
        self.speed = 5

    def display(self, display):
        display.blit(self.image, (self.x,self.y))

    def move(self, x, y):
        self.x += x * self.speed
        self.y += y * self.speed