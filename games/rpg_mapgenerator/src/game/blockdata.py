import os

import pygame


IMAGE_PATH = "img/"
SIZE   = 16

dirt  = {"image":"dirt","type":"dirt"}
grass = {"image":"grass","type":"grass"}
stone = {"image":"stone","type":"stone"}
water = {"image":"water","type":"water"}
tree  = {"image":"tree","type":"tree"}

load_image = lambda path : pygame.transform.scale(pygame.image.load(path),(SIZE,SIZE)).convert_alpha()
def load_asset():
    assets = {}
    for path,_,files in os.walk(IMAGE_PATH):
        for f in files:
            name = f.split(".")[0]
            assets[name] = load_image(path+"/"+f)

    return assets

