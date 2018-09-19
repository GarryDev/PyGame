import pyglet
import resources as res
import traceback
import sys

try:
    res.initialize()
except Exception as e:
    sys.exit(traceback.format_exc())

# window subclass
class MainWindow(pyglet.window.Window):
    def __init__(self):
        pyglet.window.Window.__init__(self)
        self.set_size(800, 600)
        self.set_caption('Window subclass')

window = MainWindow()

label = pyglet.text.Label('Hello, world',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')



@window.event
def on_draw():
    window.clear()
    res.sprite_grid[0].blit(0,0,0)

pyglet.app.run()