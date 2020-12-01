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
def rule1(boid):    
    pcj = vector.Vector(0,0)
    N = 0
    for b in flock:
        N += 1
        if b != boid:
            pcj = pcj + boid.position
    pcj = (pcj / (N-1))
    
    return ((pcj-boid.position) / 100)

def rule2(boid):    
    c = vector.Vector(0,0)    
    for b in flock:
        if b != boid:
            if ((abs(b.position - boid.position)) < 100):
                c = c - (b.position - boid.position)                 
    return c

def rule3(boid):
    pvj = vector.Vector(0,0)
    N = 0
    for b in flock:
        N += 1
        if b != boid:
            pvj = pvj + b.velocity
            
    pvj = (pvj / (N-1))
    return ((pvj - boid.velocity) / 8)    

def bound_position(boid):
    V = vector.Vector(0,0)
    if boid.position.x < -3000:
        V.x = 10
    elif boid.position.x > 3000:
        V.x = -10
        
    if boid.position.y < -3000:
        V.y = 10        
    elif boid.position.y > 3000:
        V.y = -10 
    return V
    
def tend_to_position(boid):
    place = vector.Vector(2000,2000)
    return ((place - boid.position) / 100)           
                
def move_all_boids_to_new_positions(boids):    
    for b in boids:
        v1 = rule1(b)
        v2 = rule2(b)
        v3 = rule3(b)
        v4 = bound_position(b)
        v5 = tend_to_position(b)        
        b.velocity = b.velocity + v1 + v2 + v3 + v4 + v5
        b.position = b.position + b.velocity
        
def draw_boids(boids):
    list_of_boid_x, list_of_boid_y = [], []
    axes = plt.gca()
    axes.set_xlim([-5000,5000])
    axes.set_ylim([-5000,5000])
    for boid in boids:
        list_of_boid_x.append(boid.position.x)
        list_of_boid_y.append(boid.position.y)

    plt.scatter(list_of_boid_x, list_of_boid_y)
    plt.pause(0.1)
    plt.show()



flock = [boid(*np.random.rand(2)*1000) for _ in range(30)]

x = 0
number = 500

while x < number:
    move_all_boids_to_new_positions(flock)
    x += 1
    draw_boids(flock)
    
    


