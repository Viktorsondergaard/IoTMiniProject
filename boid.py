# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 10:26:59 2020

@author: Tobias
"""


import vector
import numpy as np
import matplotlib.pyplot as plt

class boid:
    
    def __init__(self, x, y):
        self.position = vector.Vector(x,y)
        vec = (np.random.rand(2) - 0.5)*5
        self.velocity = vector.Vector(*vec)

# http://www.vergenet.net/~conrad/boids/pseudocode.html
              
def cohesion(boid):    
    perceived_centre = vector.Vector(0,0)
    number_in_flock = 0
    for b in flock:
        number_in_flock += 1
        if b != boid:
            perceived_centre = perceived_centre + boid.position
    perceived_centre = (perceived_centre / (number_in_flock-1))
    
    return ((perceived_centre-boid.position) / 100)

def separation(boid):    
    displacement = vector.Vector(0,0)    
    for b in flock:
        if b != boid:
            if ((abs(b.position - boid.position)) < 25):
                displacement = displacement - (b.position - boid.position)                 
    return displacement

def alignment(boid):
    perceived_velority = vector.Vector(0,0)
    number_in_flock = 0
    for b in flock:
        number_in_flock += 1
        if b != boid:
            perceived_velority = perceived_velority + b.velocity
            
    perceived_velority = (perceived_velority / (number_in_flock-1))
    return ((perceived_velority - boid.velocity) / 8)    

def bound_position(boid):
    V = vector.Vector(0,0)
    if boid.position.x < 0:
        V.x = 10
    elif boid.position.x > 1000:
        V.x = -10
        
    if boid.position.y < 0:
        V.y = 10        
    elif boid.position.y > 1000:
        V.y = -10 
    return V
    
def tend_to_position(boid,number): 
    place = vector.Vector(900,900)
    if number > 100:
        place = vector.Vector(200,200)
    return ((place - boid.position) / 100)   

def limit_velority(boid):
    velocity_limit = 25
    if (abs(boid.velocity) > velocity_limit):
        boid.velocity = ((boid.velocity / abs(boid.velocity)) / velocity_limit)
        
                
def move_all_boids_to_new_positions(boids, number):  
    for b in boids:
        v1 = cohesion(b)
        v2 = separation(b)
        v3 = alignment(b) 
        v4 = bound_position(b)
        v5 = tend_to_position(b, number)        
        b.velocity = b.velocity + v1 + v2 + v3 + v4 + v5
        limit_velority(b)
        b.position = b.position + b.velocity
        
def draw_boids(boids, number):
    list_of_boid_x, list_of_boid_y = [], []
    axes = plt.gca()
    axes.set_xlim([0,1500])
    axes.set_ylim([0,1500])
    for boid in boids:
        list_of_boid_x.append(boid.position.x)
        list_of_boid_y.append(boid.position.y)

    plt.scatter(list_of_boid_x, list_of_boid_y)
    plt.title('After k: ' + str(number) + ' iterations')
    plt.pause(0.1)
    plt.show()

import random

flock = [boid(random.randint(0,1500),random.randint(0,1500)) for _ in range(30)]

x = 0
number = 500

while x < number:
    move_all_boids_to_new_positions(flock, x)
    x += 1
    draw_boids(flock, x)
    
    


