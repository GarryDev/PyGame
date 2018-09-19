import pyglet
import resources as res
import traceback
import sys
import tile
import chunk_gen

WINDOW_WIDTH    = 800
WINDOW_HEIGHT   = 600

chunk_size = 32
chunk_span = chunk_size//4

# window subclass
class MainWindow(pyglet.window.Window):
    def __init__(self):
        pyglet.window.Window.__init__(self)
        self.set_size(WINDOW_WIDTH, WINDOW_HEIGHT)
        self.set_caption('Window subclass')

window = MainWindow()

try:
    res.initialize()
except Exception as e:
    sys.exit(traceback.format_exc())

x_offset = 0
y_offset = 0
x_center = (WINDOW_WIDTH //2) - ((chunk_span//2) * tile.WIDTH)
y_center = (WINDOW_HEIGHT//2) - ((chunk_span//2) * tile.HEIGHT)

chunk = chunk_gen.create_chunk(chunk_gen.TerrainType.FOREST, chunk_size)

main_batch = pyglet.graphics.Batch()
sprites = []

for y in range(0, chunk_span):
    for x in range(0, chunk_span):
        sprites.append(pyglet.sprite.Sprite(
            img = res.sprite_grid[chunk[(y * chunk_span) + x].id],
            x = x_center + x_offset + (y * tile.WIDTH),
            y = y_center + y_offset + (x * tile.WIDTH),
            batch=main_batch))

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