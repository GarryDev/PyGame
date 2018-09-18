import os
from PIL import Image

homeDir = os.getenv("LOCALAPPDATA") + "\\PyGame\\"
spritePath = homeDir + "\\spirtes\\"
spriteSource = spritePath + "tileset.png"
spriteImage = PIL.Image.load(spriteSource)

def config():
    global settings

    if not os.path.exists(homeDir):
        os.mkdir(homeDir)

    if not os.path.exists(spritePath):
        print("The sprite path: " + spritePath + " does not exist. Creating it now.")
        os.mkdir(spritePath)

    if not os.path.exists(spriteSource):
        print("The sprite image files does not exist. Did the installer fail?")

def initialize():
    sprite_count = 3072

    sprites = [None] * 3072

    sprite_x_count = spriteImage.() / 32
    sprite_y_count = spriteImage.getHeight() / 32

        """ for (int y = 0 y < sprite_y_count y++) 
            for (int x = 0 x < sprite_x_count x++) 
                sprites[(y*sprite_x_count) + x] = Bitmap.createBitmap(source, x * Tile.WIDTH, y * Tile.HEIGHT, Tile.WIDTH, Tile.HEIGHT)
        """

    for y in range(0, sprite_count):

        PIL.Image.new(RGBA, (32, 32))

    print("Sprites", "Tile.WIDTH: " + "32")
    print("Sprites", "Tile.HEIGHT: " + "32")

    print("Sprites", "source.width: " + spriteImage.PIL.width())
    print("Sprites", "source.height: " + spriteImage.PIL.height())

    print("Sprites", "sprite_x_count: " + sprite_x_count)
    print("Sprites", "sprite_y_count: " + sprite_y_count)

