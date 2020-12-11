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
from goal import *

def run():
    boids = []
    goals = []
    mouse_location = (0, 0)
    window = pyglet.window.Window(800, 640,
        fullscreen=False,
        caption="IoT Boids Simulation")

    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    fps_display = pyglet.window.FPSDisplay(window=window)

    flock = [boid(random.randint(0, 640), random.randint(0, 360)) for _ in range(10)]

    def update(dt):
        move_all_boids_to_new_positions(dt, flock, goals)

    pyglet.clock.schedule_interval(update, .001)
    #pyglet.clock.schedule(update)

    @window.event
    def on_draw():
        glClearColor(0.1, 0.1, 0.1, 1.0)
        window.clear()
        glLoadIdentity()

        for boid in flock:
            boid.draw()
        
        for goal in goals:
            goal.draw()

    @window.event
    def on_key_press(symbol, modifiers):
        if symbol == key.G:
            goals.append(Goal(position=mouse_location))

        elif symbol == key.Q:
            sns.lineplot(x=np.arange(0,len(fps)), y=fps)
            matplotlib.pyplot.show() 
            pyglet.app.exit()
            self.close()
        elif symbol == key.B:
            flock.append(boid(random.randint(0, 640), random.randint(0, 360)))
    
    @window.event
    def on_mouse_drag(x, y, *args):
        nonlocal mouse_location
        mouse_location = x, y

    @window.event
    def on_mouse_motion(x, y, *args):
        nonlocal mouse_location
        mouse_location = x, y

    pyglet.app.run()

new_position_number = 0
run()