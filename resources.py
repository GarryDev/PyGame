import os
from pyglet import image

if __debug__:
    FILE_NAME = "resouces: "

HOME_DIR = os.getenv("LOCALAPPDATA") + "\\PyGame\\"
SPRITE_PATH = HOME_DIR + "sprites\\"
SPRITE_SOURCE = SPRITE_PATH + "tile_set.png"
TILE_WIDTH  = 32
TILE_HEIGHT = 32

sprite_grid = None

def initialize():
    global sprite_grid

    if not os.path.exists(HOME_DIR):
        os.mkdir("Folder missing " + HOME_DIR)

    if not os.path.exists(SPRITE_PATH):
        raise Exception("Folder missing " + SPRITE_PATH)

    if not os.path.exists(SPRITE_PATH):
        raise Exception("File missing " + SPRITE_SOURCE)

    source = image.load(SPRITE_SOURCE)
    sprite_grid = image.ImageGrid(source, 48, 64)

    if __debug__:
        print("{}Tile.WIDTH:       {}".format(FILE_NAME, TILE_WIDTH))
        print("{}Tile.HEIGHT:      {}".format(FILE_NAME, TILE_WIDTH))
        print("{}source.width:     {}".format(FILE_NAME, source.width))
        print("{}source.height:    {}".format(FILE_NAME, source.height))
        print("{}sprite_grid len:  {}".format(FILE_NAME, len(sprite_grid)))