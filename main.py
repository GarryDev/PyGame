import pyglet
from pyglet.window import mouse
import resources as res
import traceback
import sys
import tile
import chunk_gen

WINDOW_WIDTH    = 800
WINDOW_HEIGHT   = 600

chunk_size = 256
chunk_span = chunk_size//4

x_offset = 0
y_offset = 0
x_center = (WINDOW_WIDTH //2) - ((chunk_span//2) * tile.WIDTH)
y_center = (WINDOW_HEIGHT//2) - ((chunk_span//2) * tile.HEIGHT)

zoom_level = 0


# window subclass
class MainWindow(pyglet.window.Window):
    def __init__(self):
        pyglet.window.Window.__init__(self)
        self.set_size(WINDOW_WIDTH, WINDOW_HEIGHT)
        self.set_caption('Window subclass')

    def on_mouse_press(self, x, y, button, modifiers):
        if button == mouse.LEFT:
            print('The left mouse button was pressed.')

    def on_mouse_release(self, x, y, button, modifiers):
        print('The mouse button was released.')


    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        global x_offset, y_offset

        x_offset += dx
        y_offset += dy

    #def on_mouse_motion(self, x, y, dx, dy):
        #print("mouse moved")

window = MainWindow()

#window.push_handlers(pyglet.window.event.WindowEventLogger())

try:
    res.initialize()
except Exception as e:
    sys.exit(traceback.format_exc())

chunk = chunk_gen.create_chunk(chunk_gen.TerrainType.FOREST, chunk_size)

main_batch = pyglet.graphics.Batch()
sprites = []

for y in range(0, chunk_span):
    for x in range(0, chunk_span):

        i = (y * chunk_span) + x

        sprites.append(pyglet.sprite.Sprite(
            img = res.sprite_grid[chunk[i].id],
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

    for y in range(0, chunk_span):
        for x in range(0, chunk_span):
            i = (y * chunk_span) + x
            sprites[i].position = (x_center + x_offset + (y * tile.WIDTH), y_center + y_offset + (x * tile.WIDTH))

    main_batch.draw()

pyglet.app.run()