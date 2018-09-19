import pyglet
import resources as res
import traceback
import sys
import tile

import chunk_gen

try:
    res.initialize()
except Exception as e:
    sys.exit(traceback.format_exc())

chunk_size = 32
chunk_span = 8
chunk = chunk_gen.create_chunk(chunk_gen.TerrainType.FOREST, chunk_size)

main_batch = pyglet.graphics.Batch()
sprites = []

# for x in range(0, tile.WIDTH):
#     for y in range(0, tile.HEIGHT):
#         sprites.append(pyglet.sprite.Sprite(img = res.sprite_grid[chunk[(x*y) + x].tile_id], x = tile.WIDTH * x, y = tile.WIDTH * y, batch=main_batch))

# for x in range(0, 5):
#     for y in range(0, 5):
#         sprites.append(pyglet.sprite.Sprite(img = res.sprite_grid[chunk[(x*y) + x].tile_id], x = tile.WIDTH * x, y = tile.WIDTH * y, batch=main_batch))

size = tile.WIDTH

for y in range(0, chunk_span):
    for x in range(0, chunk_span):
        sprites.append(pyglet.sprite.Sprite(img = res.sprite_grid[chunk[(y * chunk_span) + x].id], x = x * size, y = y * size, batch=main_batch))

# window subclass
class MainWindow(pyglet.window.Window):
    def __init__(self):
        pyglet.window.Window.__init__(self)
        self.set_size(800, 600)
        self.set_caption('Window subclass')

window = MainWindow()

#batch = pyglet.graphics.Batch()
#background = pyglet.graphics.OrderedGroup(0)
#foreground = pyglet.graphics.OrderedGroup(1)

@window.event
def on_draw():
    window.clear()
    #res.sprite_grid[0].blit(0,0,0)
    #batch.draw()

    main_batch.draw()

pyglet.app.run()