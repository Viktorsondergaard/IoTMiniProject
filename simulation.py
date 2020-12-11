import random
import pyglet
import math
import numpy as np 
from pyglet.gl import (
    Config,
    glEnable, glBlendFunc, glLoadIdentity, glClearColor,
    GL_BLEND, GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA, GL_COLOR_BUFFER_BIT)
from pyglet.window import key
from boid import *
from simulation_world import *


window = pyglet.window.Window(640, 360,
    fullscreen=False,
    caption="IoT Boids Simulation")

glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

fps_display = pyglet.window.FPSDisplay(window=window)

flock = [boid(random.randint(0,640), random.randint(0,360)) for _ in range(10)]

""" def update(dt):
    world.updateLocalBoids()
    world.updateBoidPos(1/15) """

def update(dt):
    boid.move_all_boids_to_new_positions()

# schedule world updates as often as possible
#pyglet.clock.schedule(update)


@window.event
def on_draw():
    glClearColor(0.1, 0.1, 0.1, 1.0)
    window.clear()
    glLoadIdentity()


    batch = pyglet.graphics.Batch()
    """ vl = world.getVetexBatch()
    cl = world.getColourBatch()
    for i in range(0, len(vl)):
        batch.add(3, pyglet.gl.GL_TRIANGLES, None, ('v2f', (vl[i][0], vl[i][1], vl[i][2], vl[i][3], vl[i][4], vl[i][5])), ('c3B', (cl[i][0], cl[i][1], cl[i][2], cl[i][0], cl[i][1], cl[i][2], cl[i][0], cl[i][1], cl[i][2])))
     """

    for boid in flock:
        boid.draw()
        #batch.add(1, pyglet.gl.GL_TRAINGLES, None, ('v2f', (0.0, 1.0, 1.0, 0.0)),('c4B', (255, 255, 255, 255) * 2))
        #boid.position.x
        #boid.position.y

    
    #batch.add(1, pyglet.gl.GL_TRIANGLES, None, ('v2f', (0.0, 1.0, 1.0, 0.0)),('c4B', (255, 255, 255, 255) * 2))
    """ batch.add(1, pyglet.gl.GL_TRIANGLES, None, # <---- add None
        ('v2f', (0,0, 400,50, 200,300)),
        ('c3B', (255,0,0) * 3)
    ) """
    batch.draw()

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.Q:
        sns.lineplot(x=np.arange(0,len(fps)), y=fps)
        matplotlib.pyplot.show() 
        pyglet.app.exit()
        self.close()
    

pyglet.app.run()