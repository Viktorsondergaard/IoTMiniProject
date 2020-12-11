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

def run():
    boids = []
    mouse_location = (0, 0)
    window = pyglet.window.Window(1000, 1000,
        fullscreen=False,
        caption="IoT Boids Simulation")

    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    fps_display = pyglet.window.FPSDisplay(window=window)

    flock = [boid(random.randint(0, 640), random.randint(0, 360)) for _ in range(10)]

    def update(dt):
        global new_position_number
        move_all_boids_to_new_positions(flock, new_position_number)
        new_position_number += 1

    pyglet.clock.schedule_interval(update, .05)
    #pyglet.clock.schedule(update)

    @window.event
    def on_draw():
        glClearColor(0.1, 0.1, 0.1, 1.0)
        window.clear()
        glLoadIdentity()

        for boid in flock:
            boid.draw()

    @window.event
    def on_key_press(symbol, modifiers):
        if symbol == key.Q:
            sns.lineplot(x=np.arange(0,len(fps)), y=fps)
            matplotlib.pyplot.show() 
            pyglet.app.exit()
            self.close()
    

    pyglet.app.run()

new_position_number = 0
run()