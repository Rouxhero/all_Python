import pygame


def createSurface(name, size):
    print(name)
    if type(name) == str:
        img = pygame.image.load(name)
        img = pygame.transform.scale(img, size)
    else :
        img = pygame.Surface(size)
        img.fill(name)
    return img


sandColor = (10, 0, 0)
rockColor = (0, 10, 10)
woodColor = (20, 0, 0)
wheatColor = (0, 20, 20)
DesertColor = "img/desert.png"
HillsColor = "img/hills.png"
PlainColor = "img/plain.png"
ForestColor = "img/tree.png"
seaColor = "img/sea.png"


resourcesSize = (15, 15)
resources = {
    "Wheat": [
        5,  # Food
        2,  # Price
        createSurface(wheatColor,resourcesSize)
    ],
    "Wood": [
        1,  # Food
        2,  # Price
        createSurface(woodColor,resourcesSize)
    ],
    "Sand": [
        0,  # Food
        2,  # Price
        createSurface(sandColor,resourcesSize)
    ],
    "Rock": [
        0,  # Food
        2,  # Price
        createSurface(rockColor,resourcesSize)
    ],

}

Tiles = {
    3: [
       "Hills",
        3,  # Coef
        createSurface(HillsColor, tileSize)
    ],
    2: [
        "Forest",
        1,  # Co,ef
        createSurface(ForestColor, tileSize)
    ],
    0: [
       "Sea",
        1,  # Coef
        createSurface(seaColor, tileSize)
    ],
    1: [
        "Plain",
        1,  # Coef
        createSurface(PlainColor, tileSize)
    ],
    4: [
        "Desert",
        1,  # Coef
        createSurface(DesertColor, tileSize)
    ],


}
